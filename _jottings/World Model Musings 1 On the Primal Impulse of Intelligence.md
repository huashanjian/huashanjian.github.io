---
title: "World Models Musing 1: On the Origins of Thought and the Three Great Schools"
date: 2025-09-13
---

# **World Models: On the Origins of Thought and the Three Great Schools**

### **The Primal Impulse of Intelligence**

When we speak of "intelligence," our minds often leap to images of Einstein scribbling on a blackboard or Mozart composing in a flurry of inspired notes. These are symbols of human brilliance—profound, untouchable. Yet in the world of AI engineers and scientists, intelligence is redefined in simpler, almost crude terms: something computable, executable, measurable. If we had to distill it into one essential capacity, then today’s AI intelligence is, at its core, the **ability to anticipate the future**.

“Anticipating the future”? That sounds like something from the Oracle of Delphi, or a sci-fi prophecy. But in practice, it’s more like a mathematical game—one powered by vast data and precise computation. AI can forecast the arc of a baseball, predict the next move on a Go board, or simulate your friend's likely reaction in a given scenario. Impressive, yes. But does it understand the _why_ behind the prediction? Can it claim the kind of insight we attribute to emotional intelligence, to empathy, to human understanding?

When an algorithm knows that “if A happens, B is likely to follow,” does it truly grasp the causal mechanisms beneath that sequence? Does it comprehend the physical, psychological, or social laws that link A to B? That remains unanswered. This form of predictive intelligence aligns more with what cognitive psychologist Daniel Kahneman calls **System 1**—fast, intuitive, heuristic—rather than **System 2**—slow, deliberate, causal reasoning. The AI skims the surface of the historical data ocean, fishing out correlations and assembling fragments into the future it deems “most likely,” but it does not deduce necessity from first principles like a scientist does.

All of this "prediction" unfolds in a peculiar, almost mystical realm: the AI’s **internal universe**. A space constructed from billions—sometimes trillions—of parameters and synthetic neurons. Like a child playing with a vast sandbox built from scraped-up internet sand, it rehearses, again and again, its vision of the future. This internal world is where the model sees, thinks, and acts. It never touches the wind, never feels gravity—but still claims to understand the rules of nature. Is this not a quiet form of arrogance unique to the digital age? Can a world made of 0s and 1s truly rival the world we touch, feel, and grow in? That’s the central philosophical tension at the heart of world model research.

---

### **The Intellectual Lineage of World Models**

“World models” are not an invention of AI. Their conceptual roots run deep through the soil of human thought. As early as 1943—before the first digital computer—Scottish psychologist Kenneth Craik proposed in _The Nature of Explanation_ that an organism carries a **“small-scale model”** of reality in its mind, allowing it to simulate actions and anticipate consequences without actually executing them. This was a profound insight: our brains do not passively record the world like a camera, but actively construct simulations to guide decision-making.

Eighty years later, armed with GPUs and billions of parameters, AI researchers believe they can build such internal models for machines. But the idea has undergone a **radical formalization**. No longer a philosophical musing, the world model is now defined as a **learned, predictive environment simulator**—or more vividly, a **game engine for reality**.

That phrase—“game engine”—reveals the ambition. AI doesn’t just want to replicate intelligence. It wants a playable, digital twin of Earth: a sandbox where it can learn, experiment, and fail safely. The core mechanism? Learning physical regularities of the “if… then…” kind. Formally, the goal is to learn the environment’s **transition function**, predicting the **next state (sₜ₊₁)** given the **current state (sₜ)** and **action (aₜ)**. This amounts to inferring a probabilistic transition model of a Markov Decision Process (MDP):  
 P(sₜ₊₁ | sₜ, aₜ)

It may not know Newton’s laws or the second law of thermodynamics, but from enough examples, it can learn that “if you push an object, it moves.” That’s statistical induction, not physical deduction. The AI’s “laws of motion” resemble a thick manual of case studies, not an elegant equation scrawled on a physicist’s chalkboard.

And why does this predictive regularity matter? Because it **decouples learning from acting**. AI, like a child imagining fire before touching it, can simulate risks in its mind’s eye before acting in reality. A self-driving AI can crash millions of times in simulation before ever touching asphalt. This boosts **sample efficiency** and **safety**. Yet, the gap between simulation and the messy, unforgiving real world—the infamous **Sim-to-Real Gap**—remains a daunting challenge. No matter how good the dream, reality has a way of pushing back.

---

### **The Philosophical Divide**

The field of reinforcement learning (RL) has long been shaped by a fundamental divide—a kind of dualist tension—between two learning paradigms. These two schools of thought represent competing visions for how intelligent behavior should be acquired.

The first is the **Model-Free school**, or what we might affectionately call the **“Muscle Memory Clan.”** Its ethos is simple: don’t overthink it. Just act, fail, and adapt. Like a child learning to ride a bike—not by studying physics but by falling and getting back up—model-free agents learn purely through trial and error. No internal map of the world. Just a reactive policy mapping states to actions. Q-learning, SARSA, Deep Q Networks (DQN), PPO—these are the bread and butter of this approach.

The appeal is obvious: simplicity and directness. No need to build a model of the world. Just optimize behavior directly. In simulated environments, it works astonishingly well.

But the shortcomings are glaring. **Data inefficiency** is chief among them. To build that “muscle memory,” model-free methods demand astronomical amounts of experience. AlphaGo trained on millions of self-play games. In real-world robotics, that level of trial-and-error would be catastrophically expensive. Worse still, **poor generalization** plagues these agents. Like a seasoned commuter thrown off by a roadblock, they struggle when the environment shifts even slightly.

Thus emerged the **Model-Based school**, or the **“Contemplative Thinkers.”** Their creed? First understand, then act. Don’t touch the fire until you’ve dreamed it a thousand times.

This approach builds a world model from limited real-world interaction, then uses it to simulate outcomes and plan actions. It enables **massive sample efficiency**—hours of real-world experience can be expanded into days of internal simulation. It also ensures **safety**—errors occur in silico, not in reality.

But here lies the rub: **Model Bias.** A flawed model produces flawed plans. In dynamic or uncertain environments, internal models may become inaccurate, causing accumulated errors to derail performance. The dreamer becomes a daydreamer. Building an accurate, generalizable model remains the holy grail of this school.

---

### **The Three Kingdoms of World Modeling**

By 2024–2025, the model-based path has gained dominance. But the question of how to build this “internal universe” has birthed three distinct factions—each with its own philosophy, its own engineering trade-offs. What we now witness is a full-blown **Three Kingdoms** era of world models.

**1. The Church of Pixels**  
 _Motto: “Seeing is believing. Pixels are king.”_

Led by titans like **Google’s Genie**, **NVIDIA’s Cosmos**, and **OpenAI’s Sora**, this faction believes: if a model can generate video indistinguishable from reality, it must have internalized the laws that govern that reality. Their approach is **ultra-behaviorist**—if the output looks right, the model must “understand.” These models simulate the world by modeling video, at scale. The goal? A fully interactive, generalizable **digital twin of Earth**, a metaverse sandbox for embodied AI.

**2. The Zen of Abstraction**  
 _Motto: “Perceive essence, not surface.”_

Led by **Yann LeCun** and **Meta AI**, this school criticizes the pixel-faithful approach as wasteful and doomed. Why render every leaf’s motion when the point is to learn structure, not surface? Their innovation, **JEPA (Joint Embedding Predictive Architecture)**, shifts focus from generation to prediction, from images to embeddings. Models like **V-JEPA** operate in abstract feature space, ignoring unpredictable details and focusing on what can be reliably inferred. It's minimalist, elegant, and remarkably data-efficient.

**3. The Pragmatic Alliance**  
 _Motto: “Stand on the shoulders of giants. Don’t reinvent wheels.”_

Straddling the extremes, this school finds a middle path. Instead of learning everything from scratch or modeling pixels directly, they **decouple perception from dynamics**. Pretrained visual encoders (like **DINOv2**) serve as frozen backbones, and the focus shifts to learning dynamics within these high-quality feature spaces. Projects like **DINO-world** and **DINO-WM** exemplify this route. It’s the engineer’s approach: buy the best engine, and focus on building the rest of the car.

---

Each of these schools offers a distinct lens on what it means to model the world—pixels, embeddings, or pragmatism. Their rivalries and alliances are shaping the new frontier of AI. In the chapters that follow, we’ll dive deeper into each lineage, exploring their techniques, assumptions, and trade-offs.

The war for the inner universe has only just begun.

