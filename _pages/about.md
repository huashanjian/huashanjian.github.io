---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>
# May my work open new perspectives for you.

I am Junhua Yao, a second-year undergraduate in Computer Science with a focus on embodied intelligence and world models. My interest lies in how agents perceive, abstract, and transfer knowledge across different bodies and environments.

I see science as a craft that values clarity over cleverness and patience over haste. A small honest experiment can speak more than a large system built for speed. I believe reproducibility is a form of honesty and that negative results deserve respect, for they reveal the edges of understanding. Abstraction only has meaning when its assumptions are visible, and writing should clarify thought rather than decorate it.

Science is not only for specialists. I regard communicating its ideas to the public as a natural duty. To make complex notions accessible is to protect curiosity itself, and to keep science connected with the world it serves.

I welcome exchanges with those who share the wish to ask sharp questions and to think with care.

# 💡 Research Interest: Embodied Intelligence

My interest in Embodied Intelligence is to build agents that understand and act in the physical world, not just predict it. I'm currently exploring:

*   **Causality & Intuitive Physics:** Learning the cause–effect structure and key physical properties that govern interaction, to improve robustness, explanation, and generalization.
*   **World Models:** Moving beyond next-step forecasting toward decision-grounded models that expose structure, support counterfactual reasoning, and remain reliable under distribution shift.
*   **Spatial Intelligence:** Computational approaches for geometric understanding and spatial reasoning that enable long-horizon manipulation and navigation.
*   **Reinforcement Learning for Robotics:** Data-efficient, safe policy learning on real systems, leveraging learned models and structure for faster skill acquisition and sim-to-real reliability.

Looking ahead, I'm excited about combining causal structure, world models, and spatial reasoning to unlock higher-level abilities in robots—such as tool use, dexterous manipulation in cluttered scenes, and collaborative behaviors in shared spaces—while maintaining reliability and transfer across tasks, embodiments, and environments.

My research interests primarily involve Embodied Intelligence and Generative AI. As I build my academic profile, you can follow my work on <a href='https://scholar.google.com/citations?user=UwMitgEAAAAJ'>Google Scholar</a> (citations: <span id='total_cit'>...</span> <a href='https://scholar.google.com/citations?user=UwMitgEAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2025.03.15*:   Launched **AI101: Pioneering AI Education for Teens**, China's first open-access AI curriculum for secondary education. See the [Projects](https://github.com/huashanjian/AI-101) section for details.
- *2025.02.09*:   Successfully completed my first surfing experience and obtained the L2 certification!
- *2024.12.16*:   Attended the AI Computing Technical Committee Forum at HKUST(GZ).
- *2024.11.29*:   Attended the Third AI4S International Symposium at PKU Shenzhen.
- *2024.11.14*:   Attended the X-Lake Forum on Embodied Intelligence at Tsinghua SIGS.

# 📚 Educational Resources & Materials

I warmly welcome you to explore my interests in Embodied Intelligence. My curiosity about world models is not only about their promise as an AI technique, but also about the deeper questions they pose on how intelligence perceives, imagines, and understands the world.

Here I share resources and reflections I have prepared for non-specialist readers. They are not complete or final, only a part of my own learning that I hope may open the field in an accessible way. Whether you are new to AI, working from another discipline, or simply curious about intelligence, I hope these materials offer you a fresh perspective and invite further conversation.

## 🌍 World Models 

### **World Models: When Machines Begin to Imagine**
*An accessible introduction to world models in AI, covering the philosophical foundations and practical implementations.*

- **📊 Slides**: [View Slides](https://drive.google.com/file/d/1yH8hOjfyds6W3SHeAAYI1DIiWDWfywqI/view?usp=sharing) *(Google Drive)*
- **🎯 Target Audience**: Undergraduate students, AI enthusiasts


<div style="text-align: center; margin: 20px 0;">
<iframe src="https://drive.google.com/file/d/1yH8hOjfyds6W3SHeAAYI1DIiWDWfywqI/preview" 
        width="320" 
        height="180" 
        allow="autoplay" 
        style="border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
</iframe>
<p style="margin-top: 10px; font-size: 0.9em; color: #666;">
<em>Preview of World Models Slides - Click <a href="https://drive.google.com/file/d/1yH8hOjfyds6W3SHeAAYI1DIiWDWfywqI/view?usp=sharing" target="_blank">here</a> for full-screen view</em>
</p>
</div>

# ✍️ Jottings
{% assign jottings_list = site.jottings | sort: 'date' | reverse %}
<div class="jottings-preview">
  {% for jotting in jottings_list limit:5 %}
    <div class="jotting-preview-item">
      <a href="{{ jotting.url | relative_url }}" class="jotting-preview-title">{{ jotting.title }}</a>
      <span class="jotting-preview-date">{{ jotting.date | date: "%Y-%m-%d" }}</span>
    </div>
  {% endfor %}
  {% if jottings_list.size > 5 %}
    <div class="jotting-preview-more">
      <a href="/all-jottings/">All Jottings &raquo;</a>
    </div>
  {% endif %}
</div>

# 📝 Publications 

As a freshman in Computer Science, I am currently focusing on building a solid foundation in my field. While I don't have any publications yet, I am passionate about conducting meaningful research that can make a real impact.

I believe in the importance of thorough understanding and careful exploration before rushing into publications. My goal is to eventually contribute solid work that advances our understanding of embodied intelligence and brings genuine value to the research community.

# 🎖 Honors and Awards
- Currently, I am dedicated to establishing a solid academic base and contributing to meaningful projects. This section will be updated accordingly as I achieve future accomplishments.


# Experience
<div class="experience-item" style="display: flex; align-items: flex-start; margin-bottom: 1.5rem;">
  <div class="experience-logo" style="flex: 0 0 120px; margin-right: 20px;">
    <img src="/images/tea.jpg" alt="TEA Lab logo" style="width: 100px; border-radius: 5px;">
  </div>
  <div class="experience-details" style="flex: 1;">
    <p style="margin: 0; font-size: 1.1em;"><strong><a href="http://hxu.rocks/" target="_blank">TEA Lab, Tsinghua University</a></strong></p>
    <p style="margin: 0.2em 0;">Jun. 2025 - Present, Intern Researcher, Beijing, China</p>
    <p style="margin: 0.2em 0;">Supervised by <a href="http://hxu.rocks/" target="_blank">Prof. Huazhe Xu (许华哲)</a></p>
  </div>
</div>
