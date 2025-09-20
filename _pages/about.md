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

Hi there! I'm Junhua Yao, a passionate and curious learner based in the dynamic city of Guangzhou. Currently a freshman pursuing my undergraduate degree, I'm thrilled to be exploring the fascinating world of Computer Science.

I have a budding interest in cutting-edge technologies like Generative AI and Embodied AI, and while I'm just starting my academic journey, I'm eager to dive into research and deepen my understanding of these exciting fields.

Right now, I'm sharpening my skills with tools and languages like PyTorch, C++, Python, LaTeX, and Git. It's been a rewarding challenge, and I'm enjoying every step of the process. I'm also familiar with tools like Zotero for managing research papers and references—small wins that make the learning journey smoother!

Outside of academics, I'm all about staying active and exploring the world. Whether it's playing badminton, swimming, or planning my next travel adventure, I love discovering new places and experiencing different cultures. Traveling is a particular passion of mine, as it allows me to broaden my horizons and embrace the beauty of diversity.

I'd love to connect! Feel free to reach out at junhuayao41@gmail.com if you'd like to chat about shared interests, potential collaborations, or just to say hi.

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

I warmly welcome you to explore my research interests and directions. As a learner venturing into the field of Embodied Intelligence, I'm deeply fascinated by the concept of world models—not only as a cutting-edge AI technology, but as a profound philosophical inquiry into the nature of intelligence itself.

I've prepared some thoughts and materials about world models specifically for non-specialists, hoping to share this fascinating field in an accessible way and offer you fresh perspectives. Whether you're an AI beginner, an interdisciplinary researcher, or simply someone curious about intelligence, I hope these resources will inspire your thinking and spark meaningful conversations.

## 🌍 World Models & AI

### **World Models: A Comprehensive Introduction**
*An accessible introduction to world models in AI, covering the philosophical foundations and practical implementations.*

- **📊 Slides**: [View Slides](https://drive.google.com/file/d/1yH8hOjfyds6W3SHeAAYI1DIiWDWfywqI/view?usp=sharing) *(Google Drive)*
- **📝 Related Writing**: [World Models Musing 1: On the Origins of Thought and the Three Great Schools](/jottings/World%20Model%20Musings%201%20On%20the%20Primal%20Impulse%20of%20Intelligence/)
- **🎯 Target Audience**: Undergraduate students, AI enthusiasts
- **⏱️ Duration**: ~45 minutes

<div style="text-align: center; margin: 20px 0;">
<iframe src="https://drive.google.com/file/d/1yH8hOjfyds6W3SHeAAYI1DIiWDWfywqI/preview" 
        width="640" 
        height="480" 
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
