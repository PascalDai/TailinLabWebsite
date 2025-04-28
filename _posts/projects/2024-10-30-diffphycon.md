---
layout: project
categories: projects
title: "DiffPhyCon: A Generative Approach to Control Complex Physical Systems"
permalink: /:categories/diffphycon/
image: "/assets/img/projects/dagaccps/dagaccps.gif"
authors:
  [
    { name: "Long Wei", url: "https://longweizju.github.io/", hasAsterisk: true },
    { name: "Peiyan Hu", url: "https://peiyannn.github.io/", hasAsterisk: true },
    { name: "Ruiqi Feng", url: "https://weenming.github.io/", hasAsterisk: true },
    { name: "Haodong Feng", url: "https://scholar.google.com/citations?user=0GOKl_gAAAAJ&hl=en", hasAsterisk: false },
    { name: "Yixuan Du", url: "https://openreview.net/profile?id=~Yixuan_Du1", hasAsterisk: false },
    { name: "Tao Zhang", url: "https://zhangtao167.github.io/", hasAsterisk: false },
    { name: "Rui Wang", url: "", hasAsterisk: false },
    { name: "Yue Wang", url: "https://www.microsoft.com/en-us/research/people/yuwang5/", hasAsterisk: false },
    { name: "Zhi-Ming Ma", url: "http://homepage.amss.ac.cn/research/homePage/8eb59241e2e74d828fb84eec0efadba5/myHomePage.html", hasAsterisk: false },
    { name: "Tailin Wu", url: "https://tailin.org/", hasAsterisk: false }
  ]
links:
  [
    { name: arXiv, url: "https://arxiv.org/abs/2407.06494" },
    { name: paper, url: "https://neurips.cc/virtual/2024/poster/95505"},
    { name: code, url: "https://github.com/AI4Science-WestlakeU/diffphycon"},
    { name: "bibtex", url: "#bibtex" },
  ]
---

### Abstract

Controlling the evolution of complex physical systems is a fundamental task across science and engineering. Classical techniques suffer from limited applicability or huge computational costs. On the other hand, recent deep learning and reinforcement learning-based approaches often struggle to optimize long-term control sequences under the constraints of system dynamics. In this work, we introduce Diffusion Physical systems Control (DiffPhyCon), a new class of method to address the physical systems control problem. DiffPhyCon excels by simultaneously minimizing both the learned generative energy function and the predefined control objectives across the entire trajectory and control sequence. Thus, it can explore globally and plan near-optimal control sequences. Moreover, we enhance DiffPhyCon with prior reweighting, enabling the discovery of control sequences that significantly deviate from the training distribution. We test our method on three tasks: 1D Burgers' equation, 2D jellyfish movement control, and 2D high-dimensional smoke control, where our generated jellyfish dataset is released as a benchmark for complex physical system control research. Our method outperforms widely applied classical approaches and state-of-the-art deep learning and reinforcement learning methods. Notably, DiffPhyCon unveils an intriguing fast-close-slow-open pattern observed in the jellyfish, aligning with established findings in the field of fluid dynamics. The project website, jellyfish dataset, and code can be found at [https://github.com/AI4Science-WestlakeU/diffphycon](https://github.com/AI4Science-WestlakeU/diffphycon).

<br><br>

### Problem Setup: Complex physical system control task

Given a control objective, find the optimal control sequence under physical dynamics constraints.

<div class="row">
  <div class="col-8">
    Example: how to control the movement of the wings of a jellyfish, such that it could achieve the highest speed in fluid, under the constraints of its boundary shapes and fluid dynamics
  </div>
  <div class="col-4">
    <img src="/assets/img/projects/dagaccps/pic1.png" class="col-6">
  </div>
</div>

<br><br>

### Key Components

- Reformulates the physical dynamics from an energy-based model perspective across the entire trajectory and control sequence
- Uses diffusion models to learn the energy functions and inject the control objective as a condition or guidance of the sampling process 
- Enhanced by a prior reweighting technique, enabling the discovery of control sequences that are significantly better than training ones
<img src="/assets/img/projects/dagaccps/pic2.png" class="col-12">

<br><br>

### Results

- 1D Burgers’ Equation Control

Control objective: minimize the error between the final state and the target state

Visualization results under the FO-PC (full observation, partial control) setting. The curve for the system state of each time step under control and the target state are plotted for our method (DiffPhyCon) and baselines. The x-axis is the spatial coordinate, and the y-axis is the value of the system state. Our method achieves the lowest control objective.
<img src="/assets/img/projects/dagaccps/pic3.png" class="col-12">

- 2D Jellyfish Movement Control (Navier-Stokes Equation) 

Control objective: maximize the average moving speed of the jellyfish, under energy cost constraints  

Visualization results of the generated control curves (the opening angles between the two wings) of three test jellyfish by our method (DiffPhyCon and DiffPhyCon-lite) and baselines. The resulting control objective J for each curve is presented. Our method achieves the highest moving speed. Interestingly, our method presents a desired fast-close-slow-open pattern, aligning with established findings in the field of fluid dynamics.
<img src="/assets/img/projects/dagaccps/pic4.png" class="col-12">

- 2D Smoke Indirect Control (Navier-Stokes Equation) 
<img src="/assets/img/projects/dagaccps/pic5.png" class="col-12">

Control objective: minimize the smoke failing to pass through the target exit 
The following GIF shows the generated smoke density map (left) and control signals (middle and right).
<img src="/assets/img/projects/dagaccps/pic6.gif" class="col-12">

<br><br>

### Take-away Message

- Diffusion models under the guidance of the control objective demonstrate strong performance for complex physical system control. 
- Prior reweighting is an effective technique to generate control sequences that are significantly better than training ones.
- Our proposed framework is not limited to physical system control and it may bring promise for wider applications, such as robot control.

<br><br>

### Acknowledgement

We thank Yuchen Yang for insightful discussions on theoretical analysis. We thank anonymous reviewers for providing valuable feedback on our manuscript. We also gratefully acknowledge the support of Westlake University Research Center for Industries of the Future and Westlake University Center for High-performance Computing.

<br><br>

### Citation

<a data-scroll href="#bibtex" id=bibtex> </a>
{% highlight bibtex %}
@inproceedings{
 wei2024diffphycon,
 title={DiffPhyCon: A Generative Approach to Control Complex Physical Systems},
 author={Wei, Long and Hu, Peiyan and Feng, Ruiqi and Feng, Haodong and Du, Yixuan and Zhang, Tao and Wang, Rui and Wang, Yue and Ma, Zhi-Ming and Wu, Tailin},
 booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems},
 year={2024},
 url={https://openreview.net/forum?id=MbZuh8L0Xg}
}
{% endhighlight %}