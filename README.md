## LLM Cancer Target

基于大模型搭建文献信息提取器，从文献摘要中提出癌症潜在靶点。

癌症靶点的挖掘，特别是针对特定亚群病人的靶点（比如有着 TP53 突变的癌细胞的依赖性基因或通路是什么）的发现对癌症精准治疗有着关键的作用。基于 ChatGPT 或类似的大语言模型可以方便的从文献中提取这样的信息，通过整合这些靶点信息，有利于后续的实验验证以及进一步的数据挖掘。

该 Demo 通过对 ChatGPT 进行 `Few-shot promoting` （提供了两个正例，一个负例样本，具体见 `app.py` 中 `get_response` 函数），使其可以进行癌症依赖性信息提取。后续可以进一步让模型输出 JSON 格式，并对 PubMed 上的文献摘要进行爬取，生成大量的 “癌症--基因/通路” 依赖性关系。

 ![](https://picgo-wutao.oss-cn-shanghai.aliyuncs.com/undefinedimage-20230612122538457.png)

![](https://picgo-wutao.oss-cn-shanghai.aliyuncs.com/undefinedimage-20230612122610802.png)