---
title: "Diffusion Policy + RL: An Underrated Insight"
date: 2026-03-12
description: "Why diffusion policies fine-tuned with reinforcement learning work better than expected, through the lens of structured exploration, on-manifold search, and the geometry behind DPPO."
---

# Diffusion Policy + RL: An Underrated Insight

Something that shouldn't have worked... actually did?

[DPPO](https://arxiv.org/abs/2409.00588) shows dramatically better sample efficiency across multiple benchmarks, and the training is stable. That's surprising. Diffusion likelihoods are intractable; standard Policy Gradient shouldn't work directly. So how is it this smooth?

I recently came across a question on Zhihu: can diffusion policy be combined with RL?

On the surface, the story seems straightforward: Diffusion can imitate but not improve; RL can improve but explores inefficiently. Put them together and they complement each other. But the more I looked into it, the more I felt that "complementary" was too shallow an explanation. Something deeper might be going on.

The authors of DPPO found that directly fine-tuning a Diffusion Policy with Policy Gradient worked far better than expected. Theoretically this shouldn't work, since Diffusion likelihoods are intractable and standard PG methods can't be applied directly. But they found that, well, if you just apply PG to the denoising process anyway, it turns out to be surprisingly stable.

Why?

I'm increasingly convinced the answer is hiding in an underappreciated concept: **structured exploration**.

Why "underappreciated"? Because when papers talk about Diffusion + RL, they tend to emphasize technical contributions: new algorithms, new losses, benchmark gains. Very few clearly explain *why* this combination works. Of the dozen or so related papers I've read, only the DPPO authors explicitly touched on it, with the phrase "on-manifold exploration." A systematic treatment is almost nowhere to be found (though I may have missed some).

## What Is Diffusion Policy, Anyway?

*(If you're already familiar with Diffusion Policy, skip ahead to "Why Combine Them?")*

Before going further, let me clarify what Diffusion Policy is actually doing.

A traditional robot policy works like this: given a state, output an action. Simple and direct. The problem is that many tasks have more than one correct answer. Take picking up a cup: you could grab it from the left, or from the right. Both work. But a traditional policy can only output one action, so it averages the two possibilities and reaches for the middle. That's actually wrong.

Diffusion Policy says: don't output a single action; output a *distribution* over actions. That distribution can be multimodal: one peak for grabbing from the left, one for the right, nothing in the middle.

How? With a diffusion model.

Here's a way to think about diffusion models: imagine you have a clear photograph, and you keep pouring sand over it until you can no longer make out anything. A diffusion model learns to sweep that sand away, step by step, until the original photo is restored.

For the mathematically inclined: it defines a forward process and a reverse process. The forward process adds noise progressively. Given original data $x_0$, after $T$ steps of noising you get $x_T \approx \mathcal{N}(0, I)$, essentially pure noise. The reverse process learns to denoise: a neural network is trained to predict the noise added at each step, then removes it. The training objective is surprisingly simple: just MSE loss between the predicted and actual noise. This loss is equivalent to score matching, i.e., learning $\nabla \log p(x)$. That'll come up again later.

![Diffusion denoising: restoring an action sequence from pure noise, step by step](/figures/diffusion-policy-meets-rl/diffusion-denoising.svg)

Applied to robotics, the "photo" is an action sequence. During training, the model sees a bunch of human demonstrations and learns to denoise: starting from pure noise, iteratively recovering plausible actions.

More concretely: a Diffusion Policy takes in the current observation (images, joint angles, etc.) and outputs a sequence of future actions. [Chi et al. (2023)](https://arxiv.org/abs/2303.04137) introduced a clever design called *action chunking*: rather than predicting one action per timestep, predict an entire action sequence and execute it smoothly. This captures temporal dependencies between actions. Picking up a cup isn't one action; it's a whole chain: reach, open fingers, approach, close, lift. Predicting these one at a time tends to be jittery; predicting them together is smooth.

![Action Chunking: predicting an entire action sequence rather than individual steps](/figures/diffusion-policy-meets-rl/action-chunking.svg)

Chi et al.'s 2023 work made this concrete, and the results were strong. But there's a fundamental limitation: it can only *imitate*, not *improve*. If an action isn't in the demonstration data, the model simply won't produce it.

That's why we want to combine it with RL.

But before moving on, I want to flag something that's easy to miss: Diffusion Policy's inability to go beyond demonstrations isn't a bug; it's a feature. Precisely *because* it strictly learns the data distribution, it can guarantee that generated actions are "reasonable." If it could freely generate actions outside the data distribution, the "structure" it learned would be meaningless.

The issue is that "reasonable" doesn't mean "optimal." The actions in demonstration data may be reasonable, but not necessarily the best. Human demonstrators have their own habits, preferences, and even mistakes. Diffusion Policy faithfully learns all of that, including the suboptimal parts.

That's the problem RL needs to solve: given a foundation of "reasonable," find "better."

## Why Combine Them?

RL's strength is autonomous optimization. Give it a reward signal and it can find better policies through trial and error, no human demonstrations needed.

But RL has a well-known Achilles' heel: exploration is wildly inefficient.

A robot's action space can easily be dozens of dimensions. Random exploration in such a high-dimensional space is basically searching for a needle in a haystack. The vast majority of attempts are meaningless: either the action itself is physically unreasonable (joint angles out of range), or it's completely at odds with the current state (the cup is on the left, but you're reaching right).

How bad is this? Let's do the math. A 7-DOF robotic arm, with 10 possible velocities per joint, gives $10^7 = 10{,}000{,}000$ combinations. The probability of finding a good action via random noise exploration drops exponentially with dimensionality. Worse, in high-dimensional spaces, "good actions" tend to cluster on a low-dimensional manifold. Picture a 10-million-dimensional space where good actions occupy a 100-dimensional sliver. The odds of random sampling hitting that sliver are essentially zero.

![Low-dimensional manifold in a high-dimensional action space: good actions cluster in a thin subspace](/figures/diffusion-policy-meets-rl/action-manifold.svg)

This is why traditional RL has always struggled in robotics. Sample efficiency is too low; real robots can't afford it.

There's a very practical concern here: every attempt on a real robot has costs. Time, energy, wear, and safety risk. An algorithm that needs a million attempts to learn a task might finish in a few hours in simulation, but on a real robot, that could take years. Not an exaggeration. Many RL algorithms that look great in simulation completely fall apart on real hardware, precisely because of sample efficiency.

So what if we combine Diffusion and RL?

Intuitively, the combination makes sense: use Diffusion to learn a distribution of "reasonable actions," then use RL to find the best one within that distribution. Diffusion handles "what's reasonable," RL handles "what's best."

But is that too superficial?

What actually makes this combination work isn't just "complementarity"; it's that the Diffusion generation process itself provides a *special kind* of exploration.

## The Core Idea: What Is Structured Exploration?

How does traditional RL explore? It adds noise to actions, randomly perturbs them, and sees what happens.

The problem is that this exploration is *unstructured*. You're jumping around the entire action space, and most jumps land in unreasonable territory.

Diffusion's exploration is different.

Diffusion generates actions iteratively: starting from pure noise, denoising step by step until an action emerges. Each denoising step makes a small adjustment; it's not jumping around the full space. More importantly, the direction of adjustment is meaningful: it inherently drifts toward the region of "reasonable actions."

The word "manifold" here is literal. Suppose the training data (human demonstrations) concentrates on a low-dimensional submanifold of the action space. The score function that Diffusion learns will point toward that manifold in its vicinity. Why? Because the score function is $\nabla \log p(x)$, pointing in the direction of steepest increase in probability density. All the data is on the manifold; probability drops off away from it; so the score naturally pulls you back. The denoising process walks along that gradient, staying close to the manifold.

This is **structured exploration**: exploration isn't random, it has structure. You're still trying different possibilities, but the search is constrained to reasonable territory.

![Structured exploration vs. random exploration: traditional RL wanders blindly in the fog, most samples landing off-manifold; Diffusion + RL follows the valley floor, with the score function pulling samples back onto the manifold](/figures/diffusion-policy-meets-rl/structured-exploration.png)

Think of it this way: traditional RL exploration is like sprinting blindfolded through a foggy plain, mostly running into dead ends. Diffusion + RL exploration is like walking along a river at the valley floor (the data manifold). You can still probe left and right to explore, but the steep slopes on either side (the score function gradient) act like gravity, always pulling you back toward the navigable path at the bottom. You never stray too far, and every probe lands on solid ground.

Let me clear up a potential confusion: structured exploration is *not* the same thing as the "constrained exploration" in constrained RL or safe RL. Constrained RL uses *explicit* constraints: you define a constraint set (e.g., "velocity cannot exceed some threshold") and enforce it during optimization. These constraints are human-designed and require prior domain knowledge. Structured exploration uses *implicit* constraints that emerge from the data distribution itself. The manifold Diffusion learns isn't designed by you; it *grows* from the demonstration data. Both are complementary, not alternatives.

Another analogy: a painter. Nobody starts with a blank canvas, makes random brushstrokes, and hopes to accidentally produce the *Mona Lisa*. A painter first sketches a rough draft, establishing overall composition and proportions, then refines from there. The draft is the "structure"; the refinement is the "exploration." Diffusion + RL works similarly: use imitation learning to establish a "draft" (the distribution of reasonable actions), then use RL to "refine" that draft (find better actions).

This is why Policy Gradient is surprisingly effective with Diffusion: exploration is constrained near the manifold, so each gradient update is more meaningful, with less wasted on unreasonable directions. And Diffusion's iterative structure is naturally suited to incremental optimization. PG's philosophy is "small steps"; denoising is inherently "small adjustments." They fit together well.

### Why Does the Score Function Naturally Point Toward the Manifold?

There's a beautiful piece of mathematical intuition here.

Diffusion models learn the score function: $\nabla \log p(x)$. Geometrically, this has an interesting property: when data concentrates on a low-dimensional manifold, the score function near the manifold points *toward* the manifold itself.

Why? Because the score function points in the direction of steepest increase in probability density. If data lives on the manifold, moving away from it means probability collapses, so the score naturally pulls you back.

[Stanczuk et al. (2022)](https://arxiv.org/abs/2212.12611) put it this way: when data concentrates near a low-dimensional manifold, in the small-noise limit, the score function points in the normal direction to the manifold.

In plain language: Diffusion doesn't just know "what data looks like"; it also knows "which direction leads away from the data." Imagine a sphere: at every point on the surface, there's a direction perpendicular to the surface, pointing outward. Diffusion learns exactly those "away" directions, which means it can pull deviant points back in.

![Score function pointing toward the manifold: arrows show the direction of ∇log p(x)](/figures/diffusion-policy-meets-rl/score-to-manifold.svg)

This sounds abstractly mathematical, but the practical implication is direct: when noise is small, the denoising step tends to pull samples back toward high-probability territory, i.e., closer to the data manifold.

Strictly speaking, this isn't the same as a precise "projection onto the manifold." But as geometric intuition, it's enough to explain why Diffusion's update directions aren't arbitrary.

So when we say "structured exploration," the "structure" doesn't come from thin air; it is the geometric structure of the data itself. By learning the score function, Diffusion implicitly learns the shape of the data manifold.

There's a useful mathematical analogy here: structured exploration can be roughly understood as **KL-Regularized RL**. Diffusion Policy provides an extremely powerful prior distribution $\pi_\text{base}$. The RL objective is to maximize reward while minimizing the KL divergence between the current policy $\pi$ and $\pi_\text{base}$. Traditional RL (like SAC) uses a Gaussian prior, so it wanders freely. Using Diffusion as the prior, the KL constraint acts like an *invisible leash*, keeping exploration firmly anchored to the data manifold. (More on this later: someone recently formalized this into a theory of "entropy maximization on the manifold.")

### Around the Expert Data Manifold

The DPPO authors use a precise term: *on-manifold exploration* (or more accurately, *around the expert data manifold*). Exploration happens near the expert data manifold, rather than wandering the full action space.

Traditional RL adds noise to actions. The problem is that most noise pushes you off the manifold, and off-manifold actions are inherently unreasonable, making that exploration wasted. Diffusion is different: the denoising process naturally pulls samples toward high-probability regions, so exploration more reliably lands in reasonable territory. This is why DPPO can learn good policies with very few samples: not because it explores more, but because it explores *better*.

DPPO includes a particularly convincing experiment: in an environment called Avoid, the authors visualize the exploration coverage of different methods and find that the diffusion policy hugs the expert data manifold, while Gaussian policies scatter outward. This is more revealing than a benchmark score, because it uncovers something more fundamental: exploration *quality* matters more than exploration *quantity*.

I think this is one of the most underrated perspectives in the entire Diffusion + RL story. Everyone's discussing how to compute gradients, how to speed things up, but structured exploration, at the geometric level, might be the key to understanding *why* it works. For now, this is more experimental observation and geometric intuition than a proven singular mechanism, though I think it has strong explanatory power.

### What's Special About Diffusion, Exactly?

At this point, you might ask: BC warm-start is already known to help RL. How much of this success is really about Diffusion's geometric structure?

Fair question. I've thought about it for a while.

It's true that any good initialization helps RL. Pre-training an MLP policy with BC and then fine-tuning with PPO will outperform starting from scratch. So what makes Diffusion special?

My view: the difference lies in what "good" means. MLP BC pre-training gives you a point estimate: one "average-optimal" action. Diffusion gives you a *distribution*, specifically a manifold of reasonable actions.

When RL begins exploring, MLP exploration adds noise around that point estimate in arbitrary directions. Diffusion exploration moves *along the manifold* in structured directions.

This isn't saying MLP + BC + RL doesn't work. It does, just less efficiently. DPPO's comparison experiments show that under the same sample budget, Diffusion policy performs significantly better. I haven't carefully verified whether the BC-phase losses are truly comparable between the two, but intuitively, if it were purely an initialization gap, it's hard to explain the efficiency difference in the subsequent RL phase.

To strictly prove "geometric structure is the key factor" would require careful ablations, like training a Normalizing Flow on the same data and checking whether it produces similar effects. If yes, the key is "having learned the data manifold." If not, the iterative denoising process itself may also be important.

Current evidence is mostly indirect. But I lean toward the geometric structure explanation, because it unifies many observations: why exploration is more efficient, why training is more stable, why the approach is less sensitive to hyperparameters.

### But Maybe I'm Wrong?

Writing this, I should admit: I may be over-attributing. My thinking here is still taking shape.

"Structured exploration" is a compelling explanation, but it isn't the only one. Maybe Diffusion + RL works for entirely different reasons:

- **Maybe it's just better initialization.** Diffusion pre-training gives a stronger starting point, and the RL is just cashing in on that.
- **Maybe it's the more expressive policy class.** Diffusion can represent multimodal distributions, which is inherently stronger than a Gaussian policy, with nothing to do with "manifolds."
- **Maybe it's the smoothness from action chunking.** Predicting a full action sequence is naturally more stable than frame-by-frame prediction, a temporal modeling benefit, not specific to Diffusion.
- **Maybe it's the training stability from the denoising process.** Iterative denoising smooths gradients, an optimization benefit, unrelated to "exploration."

All of these are plausible, and they're not mutually exclusive. The real answer is probably a combination of factors, not one clean story called "structured exploration."

So why do I still lean toward the geometric explanation?

Because it has stronger predictive power. If the key is "having learned the data manifold," then we can predict that any method capable of learning a manifold (Normalizing Flow, VAE, Energy-Based Model) should show similar effects. If the key were just "better initialization," we couldn't explain why Diffusion outperforms an MLP with comparable BC loss.

This is just my read, not a conclusion. Cleanly decomposing these factors would require more careful ablations. But absent better evidence, I'll put my weight behind the explanation with the most explanatory reach.

Why say it's underrated? Because most papers, when describing their methods, focus on technical contributions: we proposed a new algorithm, we solved a computational problem, we improved benchmark scores. Those things matter, but they answer "how," not "why." Structured exploration gets closer to "why", but it rarely lands at the center of any paper.

That feels like a missed opportunity. A clearer understanding of "why it works" would help us better predict "when it works" and "when it doesn't." That's more valuable than just chasing another +2% on a benchmark.

## What This Insight Explains

With structured exploration in mind, a lot of things start making sense. Let's look at how this insight plays out in specific methods.

### DPPO: Treating the Denoising Chain as an MDP

DPPO's core idea is to treat the entire denoising chain as an MDP: each denoising step is an "action," and the full chain is an episode. This makes it possible to optimize with standard PPO.

It sounds like a hack, but it's actually quite natural. The denoising process is inherently sequential; each step can be evaluated and optimized independently. This isn't circumventing Diffusion's intractable likelihood; it's *leveraging* its structure.

Technically, DPPO uses a two-level MDP:

- **The Outer MDP** is the robot interacting with the environment. State is the observation, action is the full action sequence, reward is task success or failure.
- **The Inner MDP** is the Diffusion denoising process. State is the current noisy action, action is one denoising step, reward is... well, here's the problem: the denoising process has no intermediate rewards. Reward only arrives at the very end of the Outer MDP.

How do you handle that? **Index flattening.**

Flatten the two-level MDP into one long episode. If the outer level has $T$ steps and the inner level has $K$ denoising steps, the full episode has $T \times K$ steps. Then use standard GAE (Generalized Advantage Estimation) to estimate advantage at each step.

![DPPO two-level MDP flattening: T×K long chain, red arrows marking the difficulty of Advantage backpropagation](/figures/diffusion-policy-meets-rl/dppo-two-layer-mdp.png)

What's GAE? Briefly, it's a method for "credit assignment." You receive a reward at the end, but that reward results from many preceding actions. GAE estimates each step's contribution to the final reward using a decay factor: steps closer to the reward get more credit, steps farther away get less, but nothing is ignored entirely.

*(Strictly speaking, DPPO's implementation is more involved: it uses environment-step GAE with a denoising discount, rather than running standard GAE over every denoising step. But the core idea is the same: propagate the outer reward signal down into the inner denoising process.)*

The elegance of this design: the outer MDP reward can be propagated to every denoising step via GAE. Early denoising steps are far from the final reward, but GAE distributes credit using value estimates from subsequent steps.

One more key point: each denoising step outputs a Gaussian distribution (mean + variance), which means log probability can be computed directly, with no need to deal with the intractable marginal likelihood of the full Diffusion model. That's why PPO can be applied directly.

Why is the original Diffusion likelihood intractable? Because computing the likelihood of an action $a$ requires integrating over all possible denoising paths, and that integral has no closed-form solution. DPPO sidesteps this: it doesn't need the trajectory likelihood, only the per-step likelihoods. Each step is Gaussian; log probability is straightforward. The PPO importance sampling ratio becomes a product of per-step ratios, fully computable.

Sometimes the way around a hard problem isn't to solve it head-on, but to find a perspective where it simply doesn't arise. DPPO didn't solve Diffusion's intractable likelihood. It just found that if you treat denoising as an MDP, the problem doesn't need to be solved.

**The Engineering Reality Behind the Elegance**

Flattening the denoising chain into an MDP looks beautiful in theory. In engineering practice, it's a nightmare.

Suppose the outer robot interaction takes $T=100$ steps to receive a sparse reward (picking up the cup), and the inner Diffusion denoising needs $K=20$ steps. Flattened out, PPO is now looking at an episode of length 2,000.

RL's worst enemy is the credit assignment problem. The robot receives +1 at step 2,000. How does GAE attribute that reward to the 14th Gaussian denoising step during the 37th outer interaction? Such long episodes cause the variance of advantage estimates to explode.

DPPO makes this tractable by separating the discount factors for environment rewards and denoising steps. This isn't prominently featured in the paper, but from the method design, this separation is what makes credit assignment feasible.

This may also be part of why DPPO is fairly sensitive to hyperparameters (at least from the ablation results, the choice of discount factor meaningfully affects performance). If you plan to reproduce it, prepare for a tuning gauntlet.

From a structured exploration perspective, DPPO's contribution isn't a new algorithm; it's a change of perspective: reinterpreting Diffusion's generation process as an MDP that RL can optimize. This lets you preserve the manifold structure Diffusion learned while using PPO to fine-tune the policy.

### Offline RL: Diffusion as a Constraint

Another technical direction is Offline RL, with Diffusion-QL as the flagship work.

The core problem in Offline RL is distribution shift: Q-learning pushes policy toward high-Q actions, but if those actions weren't in the training data, Q value estimates are unreliable. Traditional approaches use various regularization methods to keep the policy from straying too far, with mixed results.

Diffusion-QL's key insight is that it doesn't add a Q-gradient as a post-hoc guidance signal during sampling; instead, it incorporates action-value maximization *directly into the Diffusion Policy training objective*.

The paper describes it as incorporating "maximizing action-values into the training loss of the conditional diffusion model." This way, the policy both preserves its fit to the behavior policy *and* biases toward higher-Q actions.

In other words, Diffusion-QL couples behavior cloning and policy improvement into one unified objective, rather than applying guidance separately at inference time.

This is structured exploration at work: Diffusion constrains the policy to the behavioral data manifold; RL pushes it in a better direction within that region. The constraint is "learned in," not "bolted on." The manifold constraint is encoded directly in the policy, rather than imposed at inference time.

After Diffusion-QL, EDP (Efficient Diffusion Policy) addressed a practical bottleneck: training speed. The numbers are striking: on gym locomotion, training time compresses from 5 days to roughly 5 hours (exact numbers depend on task and hardware). The key idea is to avoid running the full sampling chain, instead approximating action construction from corrupted actions during training. This shows the approach isn't just conceptually sound; it's rapidly becoming an engineering reality.

Worth noting: two earlier works laid the groundwork. Janner et al. (2022)'s Diffuser and Ajay et al. (2023)'s Decision Diffuser were pioneers of Diffusion for sequential decision-making, modeling entire trajectories rather than just actions. Diffusion-QL and EDP are direct descendants of that lineage.

### Inference-Time Guidance: The Frozen-Weights Approach

Everything discussed above combines Diffusion and RL at training time. But there's a completely different approach worth knowing: inference-time guidance.

The core idea: why use RL to update model weights at all? If Diffusion has already learned the structure of the data distribution (the score function), we can freeze the Diffusion weights entirely and just train a Q-function separately.

At generation time (during denoising), we add the Q-value gradient as an additional guiding force (like Classifier-Free Guidance in image generation), applied to each denoising step. Intuitively:

> Each step = walk along the manifold ($\nabla \log p(x)$) + move toward higher reward ($\alpha \nabla Q(x)$)

The big advantage: the original manifold is never touched. Guidance only navigates within it. Diffusion draws the track; Q-Gradient is the accelerator.

Of course, this has trade-offs: Q-function estimation needs to be accurate enough, and inference-time computation increases. But for cases where you're particularly worried about mode collapse, or don't want to retrain a large model, this is a compelling option. It relocates "improvement" from training time to inference time: accept slower inference, but don't risk damaging the manifold.

### Flow Matching: Faster Structured Generation

Physical Intelligence's $\pi_0$ series uses Flow Matching, not Diffusion. But the underlying idea is the same.

The difference between Flow Matching and Diffusion can be roughly understood as a difference in path shape: Diffusion corresponds to a stochastic denoising process; Flow Matching learns a velocity field that continuously pushes noise toward the data distribution.

An analogy: Diffusion is like navigating a maze via a random walk; each step is noisy, but the drift eventually leads to the exit. Flow Matching is like having a map that shows the most direct path from where you are to the exit. Both get there, but Flow Matching's path is more direct and efficient.

Mathematically, Flow Matching learns a velocity field $v(x, t)$ satisfying:

$$\frac{dx}{dt} = v(x, t)$$

Integrating from $t=0$ (noise) to $t=1$ (data) traces a continuous generation trajectory. The key distinction: Diffusion relies on stochastic differential equations (SDEs); Flow Matching uses ordinary differential equations (ODEs). Deterministic ODE paths mean fewer sampling steps for high-quality results.

![Diffusion vs. Flow Matching: stochastic path vs. deterministic path](/figures/diffusion-policy-meets-rl/diffusion-vs-flow.svg)

This speed advantage matters in robot control. Systems like $\pi_0$ use roughly 10 flow matching steps to predict an action chunk, theoretically enabling high-frequency control. That said, the model outputting an action chunk quickly is one thing; system-level real-time execution is another. Physical Intelligence's later RTC work specifically addresses this, which means $\pi_0$/$\pi_{0.5}$ were still executing chunks synchronously, and truly real-time policies required additional engineering.

But Flow Matching is not a free lunch. The "more direct deterministic path" framing is fine, as long as you don't read it as claiming a straight line from noise to data is proven optimal. More accurately: it chose a class of paths that are easier to train and easier to numerically integrate. For complex multimodal distributions (say, "grab with left hand" vs. "grab with right hand"), this more direct path may not always be ideal, potentially creating a tradeoff between expressivity and efficiency.

$\pi_{0.5}$ is better understood as an extension of this approach to open-world generalization, emphasizing heterogeneous co-training and hybrid multimodal examples rather than any single tokenization trick.

$\pi_{0.6}$'s RECAP method centers on advantage conditioning. The pipeline: pre-train a VLA with offline RL, collect autonomous rollouts in the real environment (with expert corrective interventions when needed), train a value function to estimate advantage, then update via advantage-conditioned policy extraction. Different technical details from DPPO, but solving the same problem: how to keep improving a policy while preserving the structure it already has.

RECAP's value is reframing "directly online-optimizing a large VLA" into a more controllable advantage-conditioned update loop. For real robots, this is important; it's easier to bring demonstrations, rollouts, and interventions into one training loop.

---

Step back and look at this landscape: DPPO, Diffusion-QL, EDP, inference-time guidance, Flow Matching, RECAP. The names differ, the math differs, the engineering differs. But through the lens of structured exploration, they're all wrestling with the same fundamental question:

**How do we make a policy better, without destroying the structural foundation it has already built?**

DPPO preserves the iterative structure of the denoising chain. Diffusion-QL encodes the manifold constraint into the training objective. Inference-time guidance freezes the model entirely and navigates only at inference time. Flow Matching uses a more direct generation path to accelerate. RECAP uses advantage conditioning to make large model fine-tuning more controllable. Different approaches, same logic: don't explore from scratch; improve from within existing structure.

## What This Perspective Can Do For You

We've spent a lot of time on "why it works." But understanding mechanisms isn't the goal; guiding practice is. If the structured exploration perspective is right, it should help us make better method choices, not just follow whoever currently tops the leaderboard.

### Choosing a Method

If you're starting a real-robot project today, which direction do you take?

I think DPPO is the most practical. Three reasons:

1. **The workflow is clear.** Collect demonstrations → train a Diffusion Policy → fine-tune with RL. Each step has a clear goal and verifiable results. You don't want a black box; you want a system you can debug incrementally.
2. **It's friendly to real robots.** You don't need to train Diffusion online (too slow); just fine-tune an existing policy. Manageable compute, high sample efficiency.
3. **The two-level MDP design is elegant.** It unifies Diffusion's generation process and RL's optimization process naturally, not forced.

That said, this is based on what I've read and how I understand real-robot contexts. If your setting is different (pure simulation, training time doesn't matter), the answer might be different.

Diffusion-QL is theoretically beautiful: Diffusion defines "what's reasonable," Q-learning finds the best within that, but I haven't seen many real-robot success cases. Could be Offline RL's Q-estimation problems, or Diffusion's sampling speed limiting real-time control.

Flow Matching surprised me with its speed. If your task needs high-frequency control (e.g., fine manipulation), this is worth serious consideration. There's a multimodal tradeoff we discussed earlier, but for robot control specifically, the speed benefit currently seems to outweigh it.

### The Reward Problem

There's another unavoidable issue: reward. Use RL and you have to tell the robot what "good" means. Easy in simulation; messy in the real world.

My current sense: if the Diffusion initialization is good enough, sparse rewards (success = +1, failure = 0) are sufficient. This comes mainly from DPPO's experiments: they used only sparse rewards across multiple tasks, and it worked well. The structure already narrows the exploration space; you don't need dense feedback signals.

There's an interesting tradeoff: sparser rewards demand a higher-quality initialization; denser rewards increase the reward engineering burden. Structured exploration's benefit is that it allows sparser rewards, since exploration is efficient enough without heavy guidance.

This touches on a more general question: how do we inject prior knowledge into an AI system? Traditional RL tries to encode all human knowledge in the reward function. But this is hard: reward needs to precisely reflect your intent, and human intent is often fuzzy and hard to quantify.

Diffusion + RL offers an alternative: encode prior knowledge through data. Human demonstrations implicitly carry a lot of priors: what counts as a reasonable action, what makes a natural trajectory, what constitutes safe behavior. Diffusion learns all of that; RL only needs to fine-tune on top. The reward burden shrinks; sparse rewards become enough.

## The Dark Side of the Manifold: When Structure Backfires

We've praised structured exploration at length. Time to pour some cold water.

Structure is a double-edged sword. It makes exploration more efficient, but it also draws an invisible cage around it.

### Data Bias Gets Baked Into the Manifold

If the training data itself is biased, the manifold Diffusion learns is biased. Exploring on that biased manifold means you'll never find good solutions outside it.

Example: if all demonstration data uses the right hand, Diffusion learns a "right-hand grasping" manifold. Even if left-hand grasping is better in some cases, RL will struggle to discover it; exploration is constrained to the right-hand territory.

This isn't unique to Diffusion + RL; all imitation-learning-based methods share it. But structured exploration makes it more insidious: **you think you're exploring, but you're actually just circling inside a limited space.**

### RL Will Destroy the Diversity Diffusion Built

There's an even subtler issue: RL may erase the multimodal structure Diffusion worked hard to learn.

Diffusion Policy's major selling point is multimodality. Faced with a cup, there might be 5 different grasps in the expert data; Diffusion faithfully preserves all 5 peaks. But RL is an extremely greedy optimizer. If it finds that "top grasp with right hand" gets reward 1.01 while the other 4 grasps get 1.00, RL's gradient updates will ruthlessly concentrate all probability mass on that 0.01 edge.

The result? After RL fine-tuning, the Diffusion model may degrade into a policy that only produces one action. Its reward in the current environment is higher, but it's lost robustness to physical disturbances. If the right hand gets blocked, it won't switch to the left, because its left-hand manifold got erased by RL.

This is called **mode collapse**. At its core, it and data bias are two sides of the same coin: data bias means the manifold was incomplete to begin with; mode collapse means RL whittled down a complete manifold. In both cases, the tragedy is the same: **the structure is shrinking.**

### What Can You Do About It?

Honestly, there aren't great answers yet.

For mode collapse, common approaches include:

- **KL divergence constraint** on the RL loss, preventing the fine-tuned policy from drifting too far from the base Diffusion model.
- **Entropy bonus** to encourage the policy to stay diverse.
- Barceló et al. (2024) proposed *Hierarchical Reward Fine-tuning*, using dynamic hierarchical training to avoid mode collapse.

These methods tend to cap the performance ceiling. There's a fundamental tension between maintaining diversity and maximizing reward, and no clean resolution exists yet.

For data bias, a few directions:

- **$\epsilon$-greedy off-manifold exploration:** most of the time explore on the manifold, but with small probability $\epsilon$ add a large random perturbation and jump off. Crude, but crude sometimes works.
- **Multi-manifold ensembles:** train multiple Diffusion models on different data subsets, each covering different modes. At inference time, use a meta-policy to select which model to use. You're ensembling geometric universes rather than predictions.
- **Active data collection:** if the current model only knows right-hand grasps, go deliberately collect left-hand demonstrations and retrain. Requires a human in the loop, but is probably the most reliable.

None of these are elegant. But we should at minimum be aware these problems exist, rather than pretending structured exploration solves everything.

### Structure vs. Randomness: A Deeper Distinction

Earlier I mentioned that structured exploration can be understood as KL-Regularized RL. This analogy actually goes further.

Think about what RL is really doing. It's adjusting the policy distribution, making high-reward actions more probable and low-reward actions less probable. Isn't that just reweighting the original distribution?

More concretely: under a KL constraint, the optimal policy update has a beautiful closed-form solution. The new distribution is the old distribution multiplied by an exponential weight exp(f(x)/η), where f is the reward function. This means each RL update is essentially reweighting the current distribution. Good trajectories get higher weight, bad trajectories get lower weight.

From this angle, reinforcement learning can be understood as multi-step reweighted behavior cloning. BC learns an initial distribution, RL repeatedly reweights that distribution, gradually shifting probability mass toward high-reward regions. PG, PPO, AWR, even CFG guidance can all be seen as different approximations of this framework.

What does this have to do with Diffusion + RL?

The key is: where does the reweighting happen?

Traditional RL models policies with Gaussians, so reweighting happens across the entire action space. But Gaussians are too "spread out." Most probability mass lies off the manifold, and reweighting those regions is wasted effort.

Diffusion is different. The distribution it learns is already concentrated on the data manifold. When RL reweights this distribution, the adjustments happen within the manifold, not scattered across the full space. This is where structured exploration's efficiency comes from: not fewer reweighting steps, but each step being more meaningful.

A recent paper, [De Santi et al. (2025)](https://arxiv.org/abs/2506.15385), made this intuition more formal: framing exploration as entropy maximization on the data manifold.

Their idea: a pre-trained Diffusion model implicitly defines an approximate data manifold; exploration can be written as entropy maximization on that constrained region. The paper's experiments span text-to-image and other domains, not specifically robot fine-tuning.

But I think its value is providing a formal language. It turns "structured exploration" from a geometric intuition into something rigorously definable: if a generative model has given you a "reasonable region," then exploration can be understood as spreading out as widely as possible within that region, rather than searching the full space.

Through this lens, mode collapse becomes perfectly quantifiable: **entropy is dropping, and the manifold is collapsing.** RL's greedy optimization squeezes a distribution spread across a manifold into a sharp spike.

There's another related theoretical perspective worth mentioning. Finzi et al. (2026) proposed a framework called Epiplexity, which tries to answer a fundamental question: for a computationally bounded observer, what kind of information is actually "useful"?

Their core distinction: not all "uncertainty" is created equal. One kind of uncertainty is "structural." You don't know the answer now, but given enough computation time, you could infer it from the data. Another kind is "random." No matter how long you compute, it's just unpredictable noise. They call the former epiplexity (extractable structural complexity) and the latter time-bounded entropy.

This distinction maps remarkably well onto the structured exploration intuition.

Think about what the manifold Diffusion learns actually is. It's the "patterned" part of the data: temporal dependencies between actions, correspondences between states and actions, physically plausible trajectories under constraints. These are all high-epiplexity information: complex, but structured, learnable.

What about regions off the manifold? For a computationally bounded agent, those regions are mostly noise. Not that there's "no information" there, but extracting it would require computation far beyond your budget. From a practical standpoint, it's random.

The efficiency advantage of structured exploration, in this language, becomes: concentrating samples in high-epiplexity regions (on the manifold), rather than wasting them in high-entropy but low-epiplexity random space. You're not "exploring less"—you're "exploring smarter," spending your limited computational budget where structure can actually be extracted.

![Epiplexity vs Entropy: Same data, same compute budget. Structured data yields extractable patterns; random data yields only noise.](/figures/diffusion-policy-meets-rl/epiplexity-vs-entropy.png)

## Structure Determines Boundaries

In the traditional machine learning paradigm, "exploration" and "exploitation" are two separate things that need to be balanced manually. Diffusion's structure hints at another possibility: **exploration itself can be structured, and structure is itself a kind of prior.**

This leads to a more general question: how do we inject prior knowledge into AI systems?

The traditional approach is to design reward, design loss, design architecture: all forms of "hard-coded" priors requiring human expert knowledge. Diffusion + RL shows another possibility: "soft-coding" priors through data. Human demonstrations implicitly encode a wealth of priors: what counts as a reasonable action, what makes a natural trajectory, what constitutes safe behavior. Diffusion captures all of that; RL only needs to fine-tune on top.

This paradigm (build structure first, then optimize within the structure) may not be limited to robot control. Any problem requiring search in a complex space could benefit: drug design, materials discovery, program synthesis.

But this paradigm has a ceiling. If structure determines exploration efficiency, what determines structure's boundary?

Data determines structure, but data is collected by humans. Human biases, human blind spots, the limits of human imagination: all of it gets carved into the structure. The manifold Diffusion learns is, fundamentally, the capability boundary of whoever demonstrated the task. RL can find better solutions within that boundary, but it can't cross it.

Maybe this is the real ceiling of the Diffusion + RL paradigm: not an algorithm problem, not a compute problem: a data problem. You can only search within what you've been shown.

**Structure in, structure out.** The structure you put in determines the boundary of what you can explore.

---

*Written March 12, 2026*

## How to Cite This Post

If you want to reference this essay, cite the stable page URL rather than a local Markdown file:

- Author: Junhua Yao
- Title: "Diffusion Policy + RL: An Underrated Insight"
- Published: March 12, 2026
- Canonical URL: <https://huashanjian.github.io/jottings/diffusion-policy-meets-rl/>

### Suggested reference

Yao, J. (2026, March 12). *Diffusion Policy + RL: An Underrated Insight*. Junhua Yao. <https://huashanjian.github.io/jottings/diffusion-policy-meets-rl/>

### BibTeX

```bibtex
@online{yao2026diffusionpolicyrl,
  author = {Junhua Yao},
  title = {Diffusion Policy + RL: An Underrated Insight},
  date = {2026-03-12},
  url = {https://huashanjian.github.io/jottings/diffusion-policy-meets-rl/},
  langid = {english},
  note = {Blog post}
}
```

## References

1. Chi, C., Xu, Z., Feng, S., Cousineau, E., Du, Y., Burchfiel, B., Tedrake, R., & Song, S. (2023). *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*. [arXiv:2303.04137](https://arxiv.org/abs/2303.04137)

2. Ren, A. Z., Lidard, J., Ankile, L. L., Simeonov, A., Agrawal, P., Majumdar, A., Burchfiel, B., Dai, H., & Simchowitz, M. (2024). *Diffusion Policy Policy Optimization*. [arXiv:2409.00588](https://arxiv.org/abs/2409.00588)

3. Wang, Z., Hunt, J. J., & Zhou, M. (2022). *Diffusion Policies as an Expressive Policy Class for Offline Reinforcement Learning*. [arXiv:2208.06193](https://arxiv.org/abs/2208.06193)

4. Kang, B., Ma, X., Du, C., Pang, T., & Yan, S. (2023). *Efficient Diffusion Policies for Offline Reinforcement Learning*. [arXiv:2305.20081](https://arxiv.org/abs/2305.20081)

5. Stanczuk, J., Batzolis, G., Deveney, T., & Schönlieb, C.-B. (2022). *Your diffusion model secretly knows the dimension of the data manifold*. [arXiv:2212.12611](https://arxiv.org/abs/2212.12611)

6. Physical Intelligence. (2025). *π0.6: a VLA That Learns From Experience*. [arXiv:2511.14759](https://arxiv.org/abs/2511.14759)

7. Lipman, Y., Chen, R. T. Q., Ben-Hamu, H., Nickel, M., & Le, M. (2022). *Flow Matching for Generative Modeling*. [arXiv:2210.02747](https://arxiv.org/abs/2210.02747)

8. De Santi, R., Vlastelica, M., Hsieh, Y.-P., Shen, Z., He, N., & Krause, A. (2025). *Provable Maximum Entropy Manifold Exploration via Diffusion Models*. [arXiv:2506.15385](https://arxiv.org/abs/2506.15385)

9. Barceló, R., Alcázar, C., & Tobar, F. (2024). *Avoiding mode collapse in diffusion models fine-tuned with reinforcement learning*. [arXiv:2410.08315](https://arxiv.org/abs/2410.08315)

10. Janner, M., Du, Y., Tenenbaum, J. B., & Levine, S. (2022). *Planning with Diffusion for Flexible Behavior Synthesis*. [arXiv:2205.09991](https://arxiv.org/abs/2205.09991)

11. Ajay, A., Du, Y., Gupta, A., Tenenbaum, J., Jaakkola, T., & Agrawal, P. (2023). *Is Conditional Generative Modeling all you need for Decision-Making?* [arXiv:2211.15657](https://arxiv.org/abs/2211.15657)

12. Finzi, M., Qiu, S., Jiang, Y., Izmailov, P., Kolter, J. Z., & Wilson, A. G. (2026). *From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence*. [arXiv:2601.03220](https://arxiv.org/abs/2601.03220)
