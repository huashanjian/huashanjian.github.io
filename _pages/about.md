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
My interest in Embodied Intelligence is driven by the potential to create truly adaptive agents. I am keenly exploring advancements in:
*   **World Models:** Believing that the ability to predict 'what happens next' is fundamental, I'm studying how agents learn these internal models to anticipate consequences and plan effectively.
*   **Spatial Intelligence:** Fascinated by how humans and animals navigate and interact spatially, I'm learning about computational approaches for robots to build spatial understanding and perform tasks requiring geometric reasoning.
*   **Reinforcement Learning for Robotics:** Investigating how RL algorithms can leverage learned world models and spatial representations to acquire complex skills more efficiently and safely on physical systems.

Looking ahead, I am excited by the potential of combining learned **world models** and **spatial reasoning** to unlock higher-level cognitive abilities in robots, such as tool use, complex manipulation in cluttered scenes, and collaborative interaction in shared spaces.

My research interests primarily involve Embodied Intelligence and Generative AI. As I build my academic profile, you can follow my work on <a href='https://scholar.google.com/citations?user=UwMitgEAAAAJ'>Google Scholar</a> (citations: <span id='total_cit'>...</span> <a href='https://scholar.google.com/citations?user=UwMitgEAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).

# 📊 GitHub Statistics

<div class="github-stats-section">
  <div class="stats-grid">
    <div class="grid-item">
      <img height="200" src="https://github-readme-stats-plum-zeta.vercel.app/api?username=huashanjian&show_icons=true&theme=ambient_gradient&hide_border=true&include_all_commits=true&count_private=true" alt="GitHub Stats" />
    </div>
    <div class="grid-item">
      <img height="200" src="https://github-readme-stats-plum-zeta.vercel.app/api/top-langs/?username=huashanjian&layout=compact&theme=ambient_gradient&hide_border=true&langs_count=8" alt="Top Languages" />
    </div>
  </div>
  
  <div class="stats-center">
    <img src="https://github-readme-stats-plum-zeta.vercel.app/api/pin/?username=huashanjian&repo=AI-101&theme=ambient_gradient&hide_border=true" alt="Featured Repository" />
  </div>
  
  <div class="stats-center">
    <div class="custom-contribution-graph">
      <img src="https://github-readme-activity-graph.vercel.app/graph?username=huashanjian&theme=ambient_gradient&custom_title=Contribution%20Graph&hide_border=true" alt="GitHub Activity Graph" />
    </div>
  </div>
</div>

# 🔥 News
- *2025.03.15*:   Launched **AI101: Pioneering AI Education for Teens**, China's first open-access AI curriculum for secondary education. See the [Projects](https://github.com/huashanjian/AI-101) section for details.
- *2025.02.09*:   Successfully completed my first surfing experience and obtained the L2 certification!
- *2024.12.16*:   Attended the AI Computing Technical Committee Forum at HKUST(GZ).
- *2024.11.29*:   Attended the Third AI4S International Symposium at PKU Shenzhen.
- *2024.11.14*:   Attended the X-Lake Forum on Embodied Intelligence at Tsinghua SIGS.

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
