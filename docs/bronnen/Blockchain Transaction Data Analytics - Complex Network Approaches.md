# Blockchain Transaction Data Analytics: Complex Network Approaches

Cover image

Big Data Management

Editor-in-Chief

Xiaofeng Meng

School of Information, Renmin University of China, Beijing, Beijing, China

Editorial Board

Daniel Dajun Zeng

University of Arizona, Tucson, AZ, USA

Hai Jin

School of Computer Science and Technology, Huazhong University of Science and Technology, Wuhan, Hubei, China

Haixun Wang

Facebook Research, USA

Huan Liu

Arizona State University, Tempe, AZ, USA

X. Sean Wang

Fudan University, Shanghai, Shanghai, China

Weiyi Meng

Binghamton University, Binghamton, NY, USA

Advisory Editors

Jiawei Han

Dept Comp Sci, University Illinois at Urbana-Champaign, Urbana, IL, USA

Masaru Kitsuregawa

National Institute of Informatics, University of Tokyo, Chiyoda, Tokyo, Japan

Philip S. Yu

University of Illinois at Chicago, Chicago, IL, USA

Tieniu Tan

Chiense Academy of Sciences, Bejing, Beijing, China

Wen Gao

Room 2615, Science Buildings, Peking University Room 2615, Science Buildings, Beijing, Beijing, China

The big data paradigm presents a number of challenges for university curricula on big data or data science related topics. On the one hand, new research, tools and technologies are currently being developed to harness the increasingly large quantities of data being generated within our society. On the other, big data curricula at universities are still based on the computer science knowledge systems established in the 1960s and 70s. The gap between the theories and applications is becoming larger, as a result of which current education programs cannot meet the industry’s demands for big data talents.

This series aims to refresh and complement the theory and knowledge framework for data management and analytics, reflect the latest research and applications in big data, and highlight key computational tools and techniques currently in development. Its goal is to publish a broad range of textbooks, research monographs, and edited volumes that will:

- Present a systematic and comprehensive knowledge structure for big data and data science research and education
- Supply lectures on big data and data science education with timely and practical reference materials to be used in courses
- Provide introductory and advanced instructional and reference material for students and professionals in computational science and big data
- Familiarize researchers with the latest discoveries and resources they need to advance the field
- Offer assistance to interdisciplinary researchers and practitioners seeking to learn more about big data

The scope of the series includes, but is not limited to, titles in the areas of database management, data mining, data analytics, search engines, data integration, NLP, knowledge graphs, information retrieval, social networks, etc. Other relevant topics will also be considered.

EditorsJiajing Wu, Dan Lin and Zibin Zheng

# Blockchain Transaction Data Analytics

## Complex Network Approaches

Editors

Jiajing Wu

School of Software Engineering, Sun Yat-sen University, Zhuhai, Guangdong, China

Dan Lin

School of Software Engineering, Sun Yat-sen University, Zhuhai, Guangdong, China

Zibin Zheng

School of Software Engineering, Sun Yat-sen University, Zhuhai, Guangdong, China

ISSN 2522-0179e-ISSN 2522-0187Big Data Management ISBN 978-981-97-4429-9e-ISBN 978-981-97-4430-5[https://doi.org/10.1007/978-981-97-4430-5](https://doi.org/10.1007/978-981-97-4430-5)© The Editor(s) (if applicable) and The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025This work is subject to copyright. All rights are solely and exclusively licensed by the Publisher, whether the whole or part of the material is concerned, specifically the rights of translation, reprinting, reuse of illustrations, recitation, broadcasting, reproduction on microfilms or in any other physical way, and transmission or information storage and retrieval, electronic adaptation, computer software, or by similar or dissimilar methodology now known or hereafter developed.The use of general descriptive names, registered names, trademarks, service marks, etc. in this publication does not imply, even in the absence of a specific statement, that such names are exempt from the relevant protective laws and regulations and therefore free for general use.The publisher, the authors and the editors are safe to assume that the advice and information in this book are believed to be true and accurate at the date of publication. Neither the publisher nor the authors or the editors give a warranty, expressed or implied, with respect to the material contained herein or for any errors or omissions that may have been made. The publisher remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

This Springer imprint is published by the registered company Springer Nature Singapore Pte Ltd.

The registered company address is: 152 Beach Road, #21-01/04 Gateway East, Singapore 189721, Singapore

**Preface**

Blockchain transaction data analytics has garnered extensive attention from governments, enterprises, and academia due to its potential to understand transaction behaviors in blockchain transaction networks, enhance system performance, and uncover potential issues. However, numerous challenges remain in blockchain transaction data analytics, primarily due to the high complexity of the data, the vast amount of data, and the immature analysis methods and tools. These challenges significantly hinder the full potential utilization of blockchain transaction data.

In recent years, significant progress has been made in the field of blockchain transaction data analytics. Various methods have been developed to analyze blockchain transaction data more efficiently. However, research in this field is still in its early stages of development.

This book aims to provide researchers, engineers, policymakers, and students with a comprehensive and state-of-the-art resource for understanding and addressing the various issues in blockchain transaction data analytics. This book takes a unique approach to blockchain data analysis research, focusing on data analytics based on network-based approaches. Leveraging network analysis methods, the book concentrates on three main aspects of blockchain transaction data analytics and mining: (1) transaction network modeling and pattern mining, including macro and micro-level account attributes, money laundering network patterns, and network evolution patterns; (2) account business classification, such as account label prediction based on graph neural networks; and (3) anomaly behavior identification, covering phishing detection, risk scoring, and transaction tracking.

With its comprehensive coverage of the issues and solutions related to blockchain transaction data analytics, this book serves as a valuable resource for anyone interested in understanding and solving these problems. We hope this book will contribute to the in-depth research and widespread application of blockchain technology by providing a holistic view of the challenges and opportunities in this field.

Jiajing WuDan LinZibin Zheng**Zhuhai, China**

**Acknowledgments**

We would like to express our sincere appreciation to all those who have contributed to the completion of this book on blockchain transaction data analytics.

First, we extend our gratitude to the contributors who have shared their valuable expertise and insights on this complex and rapidly evolving topic. Their contributions have been instrumental in creating a comprehensive and up-to-date resource on the subject.

We are also grateful to the editorial team at Springer for their guidance and support throughout the publishing process. Their professionalism, expertise, and commitment to excellence have been crucial in making this book a reality.

Finally, we express our appreciation to the readers of this book. We hope that the book will be a valuable resource for researchers, engineers, policymakers, and others working in the area of blockchain transaction data analytics. We also hope that the book will inspire further research and innovation in this exciting and important field.

We acknowledge that the subject of blockchain and its applications is complex and rapidly evolving, and that there are many potential conflicts of interest that may arise in the course of researching, writing, and publishing a book on this topic. We have made every effort to disclose any conflicts of interest that we are aware of, and we welcome feedback and input from readers and other stakeholders on any potential biases or conflicts that may be present in the work. This book is partially supported by the National Key R&D Program of China (No. 2023YFB2704703), the National Natural Science Foundation of China under project (62372485, 62032025, 623B2102), and the National Natural Science Foundation of Guangdong province (2023A1515011314).

**Contents**

**Part I Overview**

[**1 Blockchain Data Analytics from a Network Perspective**](#oebps-html-619883_1_en_1_chapter-xhtml)Jiajing Wu, Jieli Liu, Ming Fang, Yijing Zhao and Zibin Zheng

[**1.1 Introduction**](#oebps-html-619883_1_en_1_chapter-xhtml-sec1)

[**1.1.1 Blockchain Transaction Models**](#oebps-html-619883_1_en_1_chapter-xhtml-sec2)

[**1.1.2 Data Sources of Blockchain Transactions**](#oebps-html-619883_1_en_1_chapter-xhtml-sec3)

[**1.2 Research Status**](#oebps-html-619883_1_en_1_chapter-xhtml-sec4)

[**1.2.1 Transaction Network Modelling**](#oebps-html-619883_1_en_1_chapter-xhtml-sec5)

[**1.2.2 Transaction Network Analysis**](#oebps-html-619883_1_en_1_chapter-xhtml-sec6)

[**1.2.3 Recognition Techniques on Transaction Networks**](#oebps-html-619883_1_en_1_chapter-xhtml-sec7)

[**1.2.3.1 Entity Identification**](#oebps-html-619883_1_en_1_chapter-xhtml-sec8)

[**1.2.3.2 Trading Pattern Recognition**](#oebps-html-619883_1_en_1_chapter-xhtml-sec9)

[**1.2.3.3 Illicit Activity Detection**](#oebps-html-619883_1_en_1_chapter-xhtml-sec10)

[**1.3 Summary and Outlook**](#oebps-html-619883_1_en_1_chapter-xhtml-sec11)

[**References**](#oebps-html-619883_1_en_1_chapter-xhtml-bib1)

**Part II Blockchain Transaction Data Analysis**

[**2 Dynamic and Microscopic Traits of Typical Accounts**](#oebps-html-619883_1_en_2_chapter-xhtml)Jiajing Wu, Baoying Huang, Jieli Liu and Zibin Zheng

[**2.1 Introduction**](#oebps-html-619883_1_en_2_chapter-xhtml-sec1)

[**2.2 Data Preparation for Account Profiling**](#oebps-html-619883_1_en_2_chapter-xhtml-sec2)

[**2.2.1 Problem Description**](#oebps-html-619883_1_en_2_chapter-xhtml-sec3)

[**2.2.2 Data Collection**](#oebps-html-619883_1_en_2_chapter-xhtml-sec4)

[**2.2.3 Data Processing**](#oebps-html-619883_1_en_2_chapter-xhtml-sec5)

[**2.2.4 Network Construction**](#oebps-html-619883_1_en_2_chapter-xhtml-sec6)

[**2.3 Evolution of Transaction Features**](#oebps-html-619883_1_en_2_chapter-xhtml-sec7)

[**2.3.1 Life Cycles of Accounts**](#oebps-html-619883_1_en_2_chapter-xhtml-sec8)

[**2.3.2 Changes in the Number of Transactions**](#oebps-html-619883_1_en_2_chapter-xhtml-sec9)

[**2.3.3 Changes in the Amount of Transactions**](#oebps-html-619883_1_en_2_chapter-xhtml-sec10)

[**2.3.4 Changes in the Number of Neighbors**](#oebps-html-619883_1_en_2_chapter-xhtml-sec11)

[**2.3.5 Changes in the Number of Old and New Neighbors**](#oebps-html-619883_1_en_2_chapter-xhtml-sec12)

[**2.4 Properties of Transaction Ego Network**](#oebps-html-619883_1_en_2_chapter-xhtml-sec13)

[**2.4.1 Temporal Variation of Network Density**](#oebps-html-619883_1_en_2_chapter-xhtml-sec14)

[**2.4.2 Local Clustering Coefficient**](#oebps-html-619883_1_en_2_chapter-xhtml-sec15)

[**2.4.3 Pattern Statistics**](#oebps-html-619883_1_en_2_chapter-xhtml-sec16)

[**2.5 Experiments of Trading Ego Networks**](#oebps-html-619883_1_en_2_chapter-xhtml-sec17)

[**2.5.1 Features Extraction**](#oebps-html-619883_1_en_2_chapter-xhtml-sec18)

[**2.5.2 Experiment Settings**](#oebps-html-619883_1_en_2_chapter-xhtml-sec19)

[**2.5.3 Experiment Results**](#oebps-html-619883_1_en_2_chapter-xhtml-sec20)

[**2.6 Discussion**](#oebps-html-619883_1_en_2_chapter-xhtml-sec21)

[**2.7 Conclusion**](#oebps-html-619883_1_en_2_chapter-xhtml-sec22)

[**References**](#oebps-html-619883_1_en_2_chapter-xhtml-bib1)

[**3 Evolution of Global Driving Factors in Ethereum Transaction Networks**](#oebps-html-619883_1_en_3_chapter-xhtml)Dan Lin, Jingjing Yang, Jialan Chen, Jiajing Wu and Zibin Zheng

[**3.1 Introduction**](#oebps-html-619883_1_en_3_chapter-xhtml-sec1)

[**3.2 Link Prediction Framework**](#oebps-html-619883_1_en_3_chapter-xhtml-sec2)

[**3.2.1 Link Prediction Based Network Evolution**](#oebps-html-619883_1_en_3_chapter-xhtml-sec3)

[**3.2.2 Ethereum Transaction Evolution Analysis Framework**](#oebps-html-619883_1_en_3_chapter-xhtml-sec4)

[**3.3 Data Preparation for Evolution Analysis**](#oebps-html-619883_1_en_3_chapter-xhtml-sec5)

[**3.3.1 Transaction Data Collection**](#oebps-html-619883_1_en_3_chapter-xhtml-sec6)

[**3.3.2 Network Construction**](#oebps-html-619883_1_en_3_chapter-xhtml-sec7)

[**3.4 Analysis of Microscopic Structural Properties**](#oebps-html-619883_1_en_3_chapter-xhtml-sec8)

[**3.4.1 Characterizing Measures of Microscopic Patterns**](#oebps-html-619883_1_en_3_chapter-xhtml-sec9)

[**3.4.2 Experimental Results and Analysis**](#oebps-html-619883_1_en_3_chapter-xhtml-sec10)

[**3.5 Evolution Factors of Ethereum Transaction Networks**](#oebps-html-619883_1_en_3_chapter-xhtml-sec11)

[**3.5.1 Training/Test Set Split**](#oebps-html-619883_1_en_3_chapter-xhtml-sec12)

[**3.5.2 Feature Extraction**](#oebps-html-619883_1_en_3_chapter-xhtml-sec13)

[**3.5.3 Scoring Methods for Unconnected Node Pairs**](#oebps-html-619883_1_en_3_chapter-xhtml-sec14)

[**3.5.4 Evaluation Index of Link Prediction**](#oebps-html-619883_1_en_3_chapter-xhtml-sec15)

[**3.5.5 Prediction Results and Analysis**](#oebps-html-619883_1_en_3_chapter-xhtml-sec16)

[**3.6 Estimation of the Direction of New Transaction Relationships**](#oebps-html-619883_1_en_3_chapter-xhtml-sec17)

[**3.6.1 Direction Estimation of New Edges by Node Degree**](#oebps-html-619883_1_en_3_chapter-xhtml-sec18)

[**3.6.2 Direction Estimation of New Edge by the Historical Direction**](#oebps-html-619883_1_en_3_chapter-xhtml-sec19)

[**3.7 Conclusion**](#oebps-html-619883_1_en_3_chapter-xhtml-sec20)

[**References**](#oebps-html-619883_1_en_3_chapter-xhtml-bib1)

[**4 Evolution and Voting Behaviors in the EOSIO Networks**](#oebps-html-619883_1_en_4_chapter-xhtml)Jieli Liu, Zhe Chen, Weilin Zheng, Dingyuan Lu, Jiajing Wu and Zibin Zheng

[**4.1 Introduction**](#oebps-html-619883_1_en_4_chapter-xhtml-sec1)

[**4.2 Preliminaries**](#oebps-html-619883_1_en_4_chapter-xhtml-sec2)

[**4.2.1 Accounts and Transactions in EOSIO**](#oebps-html-619883_1_en_4_chapter-xhtml-sec3)

[**4.2.2 DPoS and DPoS in EOSIO**](#oebps-html-619883_1_en_4_chapter-xhtml-sec4)

[**4.3 Related Work**](#oebps-html-619883_1_en_4_chapter-xhtml-sec5)

[**4.3.1 Decentralization Analysis of DPoS-Based Blockchains**](#oebps-html-619883_1_en_4_chapter-xhtml-sec6)

[**4.3.2 EOSIO Analysis**](#oebps-html-619883_1_en_4_chapter-xhtml-sec7)

[**4.4 Data Preparation for EOSIO Blockchain Analysis**](#oebps-html-619883_1_en_4_chapter-xhtml-sec8)

[**4.5 Measuring Decentralization in EOSIO**](#oebps-html-619883_1_en_4_chapter-xhtml-sec9)

[**4.5.1 Block Producer Election in EOSIO**](#oebps-html-619883_1_en_4_chapter-xhtml-sec10)

[**4.5.1.1 Overview of Block Producer Election**](#oebps-html-619883_1_en_4_chapter-xhtml-sec11)

[**4.5.1.2 Distribution Statistics**](#oebps-html-619883_1_en_4_chapter-xhtml-sec12)

[**4.5.1.3 Statistics of Voting Proxies**](#oebps-html-619883_1_en_4_chapter-xhtml-sec13)

[**4.5.2 Block Production in EOSIO**](#oebps-html-619883_1_en_4_chapter-xhtml-sec14)

[**4.5.2.1 Overview of Block Production**](#oebps-html-619883_1_en_4_chapter-xhtml-sec15)

[**4.5.2.2 Quantitative Analysis with Information Entropy**](#oebps-html-619883_1_en_4_chapter-xhtml-sec16)

[**4.6 Exploring the Voting Gang Anomalies**](#oebps-html-619883_1_en_4_chapter-xhtml-sec17)

[**4.6.1 Voter Clustering Analysis**](#oebps-html-619883_1_en_4_chapter-xhtml-sec18)

[**4.6.1.1 Method Design**](#oebps-html-619883_1_en_4_chapter-xhtml-sec19)

[**4.6.1.2 Detecting in Large Stakeholders**](#oebps-html-619883_1_en_4_chapter-xhtml-sec20)

[**4.6.1.3 Detecting in Voting Proxies**](#oebps-html-619883_1_en_4_chapter-xhtml-sec21)

[**4.6.2 Mutual Voting Anomaly Detection**](#oebps-html-619883_1_en_4_chapter-xhtml-sec22)

[**4.6.2.1 Mutual Voting Pattern Analysis**](#oebps-html-619883_1_en_4_chapter-xhtml-sec23)

[**4.6.2.2 Mutual Voting Gang Detection**](#oebps-html-619883_1_en_4_chapter-xhtml-sec24)

[**4.7 Discussion**](#oebps-html-619883_1_en_4_chapter-xhtml-sec25)

[**4.8 Conclusion**](#oebps-html-619883_1_en_4_chapter-xhtml-sec26)

[**References**](#oebps-html-619883_1_en_4_chapter-xhtml-bib1)

**Part III Blockchain Transaction Network Mining**

[**5 Account Classification Based on the Homophily-Heterophily Graph Neural Networks**](#oebps-html-619883_1_en_5_chapter-xhtml)Han Yang, Junyuan Fang, Jiajing Wu and Zibin Zheng

[**5.1 Introduction**](#oebps-html-619883_1_en_5_chapter-xhtml-sec1)

[**5.2 Preliminaries**](#oebps-html-619883_1_en_5_chapter-xhtml-sec2)

[**5.2.1 Notations**](#oebps-html-619883_1_en_5_chapter-xhtml-sec3)

[**5.2.2 Graph Neural Networks**](#oebps-html-619883_1_en_5_chapter-xhtml-sec4)

[**5.2.3 Homophily and Heterophily of Networks**](#oebps-html-619883_1_en_5_chapter-xhtml-sec5)

[**5.3 Related Work**](#oebps-html-619883_1_en_5_chapter-xhtml-sec6)

[**5.3.1 Graph Representation Learning**](#oebps-html-619883_1_en_5_chapter-xhtml-sec7)

[**5.3.2 Graph Neural Networks Under Heterophily**](#oebps-html-619883_1_en_5_chapter-xhtml-sec8)

[**5.3.3 Account Classification on Ethereum**](#oebps-html-619883_1_en_5_chapter-xhtml-sec9)

[**5.4 Methodology of Account Classification**](#oebps-html-619883_1_en_5_chapter-xhtml-sec10)

[**5.4.1 Bi-path Neighbor Sampling**](#oebps-html-619883_1_en_5_chapter-xhtml-sec11)

[**5.4.2 Separated Neighborhood Aggregation**](#oebps-html-619883_1_en_5_chapter-xhtml-sec12)

[**5.4.3 Attention-Based Node Representation Learning**](#oebps-html-619883_1_en_5_chapter-xhtml-sec13)

[**5.5 Experiments of Account Classification**](#oebps-html-619883_1_en_5_chapter-xhtml-sec14)

[**5.5.1 Experimental Settings**](#oebps-html-619883_1_en_5_chapter-xhtml-sec15)

[**5.5.1.1 Ethereum Transaction Dataset**](#oebps-html-619883_1_en_5_chapter-xhtml-sec16)

[**5.5.1.2 Baselines for Comparison**](#oebps-html-619883_1_en_5_chapter-xhtml-sec17)

[**5.5.1.3 Implementation Details**](#oebps-html-619883_1_en_5_chapter-xhtml-sec18)

[**5.5.2 Account Classification Results**](#oebps-html-619883_1_en_5_chapter-xhtml-sec19)

[**5.5.3 Timing Performance Analysis**](#oebps-html-619883_1_en_5_chapter-xhtml-sec20)

[**5.5.4 Effect of Heterophilic Information**](#oebps-html-619883_1_en_5_chapter-xhtml-sec21)

[**5.5.5 Ablation Studies**](#oebps-html-619883_1_en_5_chapter-xhtml-sec22)

[**5.5.6 Parameter Sensitivity Analysis**](#oebps-html-619883_1_en_5_chapter-xhtml-sec23)

[**5.6 Conclusion**](#oebps-html-619883_1_en_5_chapter-xhtml-sec24)

[**References**](#oebps-html-619883_1_en_5_chapter-xhtml-bib1)

[**6 Phishing Fraud Detection Based on the Streaming Graph Algorithm**](#oebps-html-619883_1_en_6_chapter-xhtml)Wenjia Yu, Jingjing Yang, Jieli Liu, Yijun Xia, Baoying Huang, Jiajing Wu and Zibin Zheng

[**6.1 Introduction**](#oebps-html-619883_1_en_6_chapter-xhtml-sec1)

[**6.2 Related Work**](#oebps-html-619883_1_en_6_chapter-xhtml-sec2)

[**6.2.1 Ethereum Phishing Fraud Detection**](#oebps-html-619883_1_en_6_chapter-xhtml-sec3)

[**6.2.2 Dynamic Network Representation Learning**](#oebps-html-619883_1_en_6_chapter-xhtml-sec4)

[**6.3 Problem Definition**](#oebps-html-619883_1_en_6_chapter-xhtml-sec5)

[**6.4 Methodology of Phishing Fraud Detection**](#oebps-html-619883_1_en_6_chapter-xhtml-sec6)

[**6.4.1 Ethereum Transaction Dataset Construction**](#oebps-html-619883_1_en_6_chapter-xhtml-sec7)

[**6.4.1.1 Phishing Fraud Data Collection**](#oebps-html-619883_1_en_6_chapter-xhtml-sec8)

[**6.4.1.2 Phishing Fraud Data Processing**](#oebps-html-619883_1_en_6_chapter-xhtml-sec9)

[**6.4.2 Temporal Transaction Graph Generation**](#oebps-html-619883_1_en_6_chapter-xhtml-sec10)

[**6.4.3 Model Architecture**](#oebps-html-619883_1_en_6_chapter-xhtml-sec11)

[**6.4.3.1 First Dimension**](#oebps-html-619883_1_en_6_chapter-xhtml-sec12)

[**6.4.3.2 Second Dimension**](#oebps-html-619883_1_en_6_chapter-xhtml-sec13)

[**6.4.4 Phishing Account Detection**](#oebps-html-619883_1_en_6_chapter-xhtml-sec14)

[**6.5 Experiments of 2DynEthNet**](#oebps-html-619883_1_en_6_chapter-xhtml-sec15)

[**6.5.1 Dataset Description of ETGraph and ETGraph-Labeled**](#oebps-html-619883_1_en_6_chapter-xhtml-sec16)

[**6.5.2 Experimental Setup**](#oebps-html-619883_1_en_6_chapter-xhtml-sec17)

[**6.5.2.1 Comparison Methods**](#oebps-html-619883_1_en_6_chapter-xhtml-sec18)

[**6.5.2.2 Evaluation Metrics**](#oebps-html-619883_1_en_6_chapter-xhtml-sec19)

[**6.5.2.3 Implementation Details**](#oebps-html-619883_1_en_6_chapter-xhtml-sec20)

[**6.5.3 Effectiveness Results**](#oebps-html-619883_1_en_6_chapter-xhtml-sec21)

[**6.5.4 Ablation Study**](#oebps-html-619883_1_en_6_chapter-xhtml-sec22)

[**6.5.5 Sensitivity Analysis**](#oebps-html-619883_1_en_6_chapter-xhtml-sec23)

[**6.5.6 Efficiency Performance**](#oebps-html-619883_1_en_6_chapter-xhtml-sec24)

[**6.6 Conclusion**](#oebps-html-619883_1_en_6_chapter-xhtml-sec25)

[**References**](#oebps-html-619883_1_en_6_chapter-xhtml-bib1)

[**7 Account Risk Rating Based on Network Propagation Algorithm**](#oebps-html-619883_1_en_7_chapter-xhtml)Dan Lin, Jiajing Wu, Qishuang Fu, Zhe Chen and Zibin Zheng

[**7.1 Introduction**](#oebps-html-619883_1_en_7_chapter-xhtml-sec1)

[**7.2 Preliminary**](#oebps-html-619883_1_en_7_chapter-xhtml-sec2)

[**7.2.1 Ethereum Financial Background**](#oebps-html-619883_1_en_7_chapter-xhtml-sec3)

[**7.2.2 The Nature of Blockchain: Anonymity**](#oebps-html-619883_1_en_7_chapter-xhtml-sec4)

[**7.2.3 Transaction Network Construction**](#oebps-html-619883_1_en_7_chapter-xhtml-sec5)

[**7.3 Related Work**](#oebps-html-619883_1_en_7_chapter-xhtml-sec6)

[**7.4 Methodology of Account Risk Rating**](#oebps-html-619883_1_en_7_chapter-xhtml-sec7)

[**7.4.1 Problem Definition and Model Overview**](#oebps-html-619883_1_en_7_chapter-xhtml-sec8)

[**7.4.2 Network Propagation Mechanism**](#oebps-html-619883_1_en_7_chapter-xhtml-sec9)

[**7.5 Experiments of Account Risk Rating**](#oebps-html-619883_1_en_7_chapter-xhtml-sec10)

[**7.5.1 Account Risk Rating Data Collection**](#oebps-html-619883_1_en_7_chapter-xhtml-sec11)

[**7.5.2 Effectiveness of De-anonymous Score**](#oebps-html-619883_1_en_7_chapter-xhtml-sec12)

[**7.5.3 Analysis of Risk Rating Results**](#oebps-html-619883_1_en_7_chapter-xhtml-sec13)

[**7.5.3.1 Distribution of Risk Rating Results**](#oebps-html-619883_1_en_7_chapter-xhtml-sec14)

[**7.5.3.2 Case Studies of Transaction Pattern**](#oebps-html-619883_1_en_7_chapter-xhtml-sec15)

[**7.5.4 Comparative Evaluation Settings**](#oebps-html-619883_1_en_7_chapter-xhtml-sec16)

[**7.5.4.1 Compared Methods**](#oebps-html-619883_1_en_7_chapter-xhtml-sec17)

[**7.5.4.2 Evaluation Metrics**](#oebps-html-619883_1_en_7_chapter-xhtml-sec18)

[**7.5.4.3 Implementation Details**](#oebps-html-619883_1_en_7_chapter-xhtml-sec19)

[**7.5.5 Comparative Evaluation Results**](#oebps-html-619883_1_en_7_chapter-xhtml-sec20)

[**7.5.6 Ablation Study**](#oebps-html-619883_1_en_7_chapter-xhtml-sec21)

[**7.5.7 Risk Threshold Analysis**](#oebps-html-619883_1_en_7_chapter-xhtml-sec22)

[**7.5.8 Guarantees for Practical Use**](#oebps-html-619883_1_en_7_chapter-xhtml-sec23)

[**7.6 Conclusion**](#oebps-html-619883_1_en_7_chapter-xhtml-sec24)

[**Appendix**](#oebps-html-619883_1_en_7_chapter-xhtml-sec25)

[**References**](#oebps-html-619883_1_en_7_chapter-xhtml-bib1)

[**8 Transaction Tracking Based on Personalized PageRank Algorithm**](#oebps-html-619883_1_en_8_chapter-xhtml)Zhiying Wu, Jieli Liu, Jiajing Wu and Zibin Zheng

[**8.1 Introduction**](#oebps-html-619883_1_en_8_chapter-xhtml-sec1)

[**8.2 Preliminaries**](#oebps-html-619883_1_en_8_chapter-xhtml-sec2)

[**8.2.1 Problem Definition**](#oebps-html-619883_1_en_8_chapter-xhtml-sec3)

[**8.2.2 Discussion of Method Design**](#oebps-html-619883_1_en_8_chapter-xhtml-sec4)

[**8.3 Methodology of Transaction Tracing**](#oebps-html-619883_1_en_8_chapter-xhtml-sec5)

[**8.3.1 Architecture Overview**](#oebps-html-619883_1_en_8_chapter-xhtml-sec6)

[**8.3.2 Graph Construction**](#oebps-html-619883_1_en_8_chapter-xhtml-sec7)

[**8.3.3 Graph Expansion**](#oebps-html-619883_1_en_8_chapter-xhtml-sec8)

[**8.3.3.1** ***Push*** **and** ***Rank***](#oebps-html-619883_1_en_8_chapter-xhtml-sec9)

[**8.3.3.2** ***Pop*** **and** ***Expand***](#oebps-html-619883_1_en_8_chapter-xhtml-sec10)

[**8.3.4 Local Community Detection**](#oebps-html-619883_1_en_8_chapter-xhtml-sec11)

[**8.4 Experiments of Transaction Tracing**](#oebps-html-619883_1_en_8_chapter-xhtml-sec12)

[**8.4.1 Theoretical Analysis**](#oebps-html-619883_1_en_8_chapter-xhtml-sec13)

[**8.4.2 Experimental Setups**](#oebps-html-619883_1_en_8_chapter-xhtml-sec14)

[**8.4.2.1 Transaction Tracing Dataset**](#oebps-html-619883_1_en_8_chapter-xhtml-sec15)

[**8.4.2.2 Compared Methods**](#oebps-html-619883_1_en_8_chapter-xhtml-sec16)

[**8.4.2.3 Experimental Settings**](#oebps-html-619883_1_en_8_chapter-xhtml-sec17)

[**8.4.2.4 Metrics**](#oebps-html-619883_1_en_8_chapter-xhtml-sec18)

[**8.4.3 Experimental Results**](#oebps-html-619883_1_en_8_chapter-xhtml-sec19)

[**8.4.3.1 Scalability vs. Performance**](#oebps-html-619883_1_en_8_chapter-xhtml-sec20)

[**8.4.3.2 Comparative Experiments**](#oebps-html-619883_1_en_8_chapter-xhtml-sec21)

[**8.4.3.3 Ablation Experiments**](#oebps-html-619883_1_en_8_chapter-xhtml-sec22)

[**8.4.3.4 Top*****N*** **Recall**](#oebps-html-619883_1_en_8_chapter-xhtml-sec23)

[**8.4.3.5 Responsible Disclosure**](#oebps-html-619883_1_en_8_chapter-xhtml-sec24)

[**8.4.4 Case Studies**](#oebps-html-619883_1_en_8_chapter-xhtml-sec25)

[**8.4.4.1 Cryptopia**](#oebps-html-619883_1_en_8_chapter-xhtml-sec26)

[**8.4.4.2 Kucoin**](#oebps-html-619883_1_en_8_chapter-xhtml-sec27)

[**8.4.4.3 Axie Infinity**](#oebps-html-619883_1_en_8_chapter-xhtml-sec28)

[**8.5 Conclusion**](#oebps-html-619883_1_en_8_chapter-xhtml-sec29)

[**Appendix**](#oebps-html-619883_1_en_8_chapter-xhtml-sec30)

[**References**](#oebps-html-619883_1_en_8_chapter-xhtml-bib1)

# Part IOverview

<a id="oebps-html-619883_1_en_1_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_1](https://doi.org/10.1007/978-981-97-4430-5_1)

# 1. Blockchain Data Analytics from a Network Perspective

Jiajing Wu[1](#oebps-html-619883_1_en_1_chapter-xhtml-aff4) , Jieli Liu[1](#oebps-html-619883_1_en_1_chapter-xhtml-aff4) , Ming Fang[1](#oebps-html-619883_1_en_1_chapter-xhtml-aff4) , Yijing Zhao[1](#oebps-html-619883_1_en_1_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_1_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_1_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_1_chapter-xhtml-contactofauthor1"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_1_chapter-xhtml-contactofauthor2"></a>

**Jieli LiuEmail:** [liujli7@mail2.sysu.edu.cn](mailto:liujli7@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_1_chapter-xhtml-contactofauthor3"></a>

**Ming Fang (Corresponding author)Email:** [blossom030107@163.com](mailto:blossom030107@163.com)

<a id="oebps-html-619883_1_en_1_chapter-xhtml-contactofauthor5"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

Since the debut of Bitcoin, a blockchain platform, blockchain-based cryptocurrencies have received wide attention and accumulated a wealth of transaction data. These transaction records include rich information and complete traces of financial activities, and therefore provide us an unprecedented opportunity for knowledge discovery. Networks are a universal language for describing interacting real systems, and much work on cryptocurrency transactions is conducted from a network perspective. This survey summarizes the existing work on analyzing and understanding blockchain transactions, aiming to provide a systematic guideline in this area. We first introduce the background of blockchain transaction, and then review existing research in three different aspects, i.e., transaction network modeling, transaction network analysis, and network-based detection technology, the purpose being to provide a systematic guideline for researchers in this area.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec1"></a>

## 1.1 Introduction

There are various types of blockchain cryptocurrencies and the data structures of different cryptocurrencies are different from each other. Specifically, blockchain cryptocurrency transactions are mainly based on transaction-centric models and account-centric models. This section introduces these two common transaction models and describes how blockchain transaction data is collected, thus laying the foundation for the transaction network analysis in Sect. [1.2](#oebps-html-619883_1_en_1_chapter-xhtml-sec4).

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec2"></a>

### 1.1.1 Blockchain Transaction Models

Blockchain transactions can be considered as user actions on a cryptocurrency platform. When a new transaction is initiated by a user, it is broadcast to all nodes in the Peer-to-Peer (P2P) network and can be added to a new block in the blockchain after verification. Blockchain technology can be traced back to Satoshi Nakamoto’s Bitcoin white paper in 2008 \[[1](#oebps-html-619883_1_en_1_chapter-xhtml-cr1)], followed by the first blockchain in 2009 with the release of the Bitcoin system and mining operations. Since the birth of Bitcoin, blockchain technology has gained widespread attention and has been applied in a variety of fields such as smart finance, Internet of Things, and so on \[[2](#oebps-html-619883_1_en_1_chapter-xhtml-cr2)–[4](#oebps-html-619883_1_en_1_chapter-xhtml-cr4)]. At the same time, many alternative coins called altcoins appeared rapidly, such as Namecoin \[[5](#oebps-html-619883_1_en_1_chapter-xhtml-cr5)], the first decentralised domain name system; Litecoin \[[6](#oebps-html-619883_1_en_1_chapter-xhtml-cr6)], which was improved in transaction confirmation speed; proposed to adopt Proof of Stake (PoS) Peercoin \[[7](#oebps-html-619883_1_en_1_chapter-xhtml-cr7)] as an alternative to Proof of Work (PoW). According to CoinMarketCap.com, by the beginning of 2021, there are more than 8000 blockchain cryptocurrencies on the market, with a total market capitalisation of more than \$1 trillion at one point. Other notable cryptocurrencies include Monero \[[8](#oebps-html-619883_1_en_1_chapter-xhtml-cr8)], Zerocash \[[9](#oebps-html-619883_1_en_1_chapter-xhtml-cr9)], EOS \[[10](#oebps-html-619883_1_en_1_chapter-xhtml-cr10)], and Libra \[[11](#oebps-html-619883_1_en_1_chapter-xhtml-cr11)], among which Ether \[[12](#oebps-html-619883_1_en_1_chapter-xhtml-cr12)] is the largest blockchain system with Turing-complete smart contracts, and its primary currency is known as Ether (or ETH), the world’s second-largest cryptocurrency after Bitcoin. Among the many blockchain cryptocurrencies, their transaction models can be mainly classified into transaction-centred and account-centred models, of which Bitcoin and Ether are the typical representatives of these two types of transaction models respectively. In the Bitcoin system, as a kind of user identification, a Bitcoin address is obtained from a user’s public key through a series of one-way hashing algorithms, and a single user can have multiple transaction addresses. The transaction model used in the Bitcoin system is a transaction-centric model in which a single transaction can have multiple inputs and multiple outputs and can be associated with multiple addresses. The inputs to a transaction consist of a set of Unspent Transaction Outputs (UTXOs), which must total no less than the amount paid for the transaction. The user on the input side of the transaction can specify a new address to receive change, and the address used to receive change is also known as the change address. Additionally, there is no concept of account balance in Bitcoin; a user’s balance can be calculated by summing up the amount of UTXO in the user’s wallet.

The transaction model in Ethernet is an account-centric model, which contains two kinds of accounts, namely, Externally Owned Account (EOA) and Contract Account. The EOA is similar to a bank account in that it has the ability to make deposits, withdrawals, and record some dynamic state information (e.g., account balance). The Contracted Account is associated with an executable bytecode, whose transactions are controlled by user-written smart contract code, and which maintains status information such as bytecode hashes and the balance of the Contracted Account. Unlike Bitcoin, a transaction in Ether is a signed packet from one account to another, which contains only one input and one output. Additionally, Ether transactions can perform three main functions including transfers, contract creation, and contract invocation. Based on the transaction sender, Ether transactions can be categorised into external transactions initiated by EOA and internal transactions triggered by contract invocation. Figure [1.1](#oebps-html-619883_1_en_1_chapter-xhtml-fig1) gives a typical example of an Ethernet external and internal transaction, where Transaction 1 and Transaction 2 are both transactions initiated by the EOA, and thus they are external transactions, while Transaction 3, Transaction 4, and Transaction 5 are transactions triggered by a smart contract, and thus they are internal transactions. External transactions may lead to the creation of many internal transactions, e.g., in Transaction 2, an EOA calls a contract account, which in turn triggers three subsequent internal transactions. In this section, we introduce the background of cryptocurrency transaction network analysis. We begin with a brief view of cryptocurrencies, in which we emphatically introduce several mainstream cryptocurrencies. Then we present the transaction process of cryptocurrencies, which is the foundation for further analysis of the transaction data. At the end of this section, we summarize the data sources for both the transaction data and some related label data.<a id="oebps-html-619883_1_en_1_chapter-xhtml-fig1"></a>

***Fig. 1.1***

Examples of the external transactions and internal transactions in Ethereum

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec3"></a>

### 1.1.2 Data Sources of Blockchain Transactions

The data sources of blockchain cryptocurrency transaction network analysis mainly include blockchain transaction data and label data. The most primitive method of obtaining blockchain transaction data is to access the blockchain network through blockchain clients (such as BitcoinCore and Geth) and synchronize the block data, so as to obtain the original data of the blockchain. However, for many cryptocurrencies, their raw blockchain data is stored in binary format and needs to be parsed into a readable format for further analysis. Therefore, we can build parsers based on the blockchain data structure to extract transaction records from the raw data acquired. On the other hand, some blockchain clients (such as Ethereum) provide a JSON-RPC interface for users to retrieve transaction data, specifically, Ethereum blockchain browser Etherscan ([https://etherscan.io/](https://etherscan.io/)) provides an API for retrieving address transaction history. The format of the transaction record is as follows: The TxHash field is the unique identifier of the transaction, the Value field indicates the amount of the ether transfer, the Timestamp field provides the time stamp of the transfer, and the transaction record field indicates the amount of the ether transfer. The From and To fields represent the sender and receiver of the Ethereum transfer, respectively. One only 20 bytes address, such as “0 x00b2ed34791c97206943314ee9cbd9530762a320”, assigned to each etheric lane address, provided by the etheric fang API, we can extract to the transaction data format. However, for some smart contract enabled blockchain systems, their internal transaction records are not stored in the blockchain system. These internal transaction records can be retrieved through the block browser, or detailed information about internal transactions can be obtained by replaying all external transactions using a custom client. Some clients also provide interfaces for obtaining internal transaction information, such as the “trace” module of the OpenEthereum client, which provides detailed run-time data generated in the Ethereum virtual machine, and is a convenient tool for accessing internal transaction records. In some transaction network mining tasks, the use of tag information can further assist in the design and validation of methods. However, blockchain users do not need to reveal their real identities during transactions, making it difficult their corresponding tag information. With the increasing maturity of the blockchain ecosystem, we can find some of the manually labelled tag data from some blockchain forums and blockchain browsers. For example, Walletexplorer.com is a smart blockchain browser with automatic address clustering capability that provides rich address labels; Bitcoin Forum records some addresses related to bitcoin robberies, thefts, and scams; the tag word cloud module of the blockchain browser Etherscan provides ethereum account labels tagged by users tags; furthermore, CryptoScamDB.org provides an open-source dataset for tracking malicious URLs and related cryptocurrency addresses associated with blockchain systems. In addition, some researchers have released cleaned and organised blockchain datasets for research. For example, XBlock.pro is a dataset sharing platform designed to help the benign development of blockchain and data research, which collects data related to the current mainstream blockchain cryptocurrencies and cleanses and categorises the data, and it is one of the blockchain data platforms with the largest amount of data and the widest coverage in the academic world, which can support researchers to carry out blockchain on-chain data analysis, blockchain anti-fraud, smart contract analysis, blockchain performance analysis and other research.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec4"></a>

## 1.2 Research Status

Existing work on blockchain cryptocurrency transaction network analysis can be specifically summarised into three closely related and progressive parts: transaction network modelling, transaction network analysis and identification techniques on transaction networks. Among them, transaction network modelling mainly covers the methods and discussion of storing transaction data in the form of network; transaction network analysis discusses the unique attributes of the transaction network from the perspective of network science; and identification techniques on the transaction network mainly include the identification of the attribution behind the account address, the identification of the transaction pattern, and the identification of the illegal activities on the blockchain. This section will introduce and summarise the current state of research on each of these 3 parts.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec5"></a>

### 1.2.1 Transaction Network Modelling

The first step in the study of blockchain cryptocurrency transaction networks is to model blockchain transaction data as a network based on the transaction characteristics of blockchain. The transaction models of current blockchain systems can be broadly classified into two categories, namely transaction-centric models and account-centric models. Blockchain systems based on these two different transaction models also differ significantly in their network modelling of transaction data. Bitcoin is the most typical blockchain transaction system that adopts the transaction-centric model, and there are a series of work on network modelling of Bitcoin transaction data. Literature \[[13](#oebps-html-619883_1_en_1_chapter-xhtml-cr13)] first introduces the concept of network modelling for Bitcoin transactions and proposes to model the Bitcoin transaction process as a transaction network with transactions as nodes and a user network with users as nodes, which represent the flow of Bitcoin funds between transactions and between users, respectively. In the Bitcoin transaction process, since the inputs of transactions are UTXOs from previous transactions, the transaction network is constructed intuitively and simply by using nodes to represent transactions and directed edges containing amount and timestamp information to represent Bitcoin fund flows. Considering the possibility that users have multiple bitcoin addresses, literature \[[13](#oebps-html-619883_1_en_1_chapter-xhtml-cr13)] first aggregates the addresses belonging to the same user by clustering, and then constructs a user network with users as nodes and fund flow relationships between users as edges. These two Bitcoin transaction network modelling methods are widely used in subsequent research on blockchain transaction network analysis \[[14](#oebps-html-619883_1_en_1_chapter-xhtml-cr14)]. In addition, literature \[[15](#oebps-html-619883_1_en_1_chapter-xhtml-cr15)] modelled Bitcoin transaction data as a weighted directed hypergraph with transactions and addresses as nodes, which can represent the input and output relationships between addresses and transactions. Ether is a typical representative of blockchain systems based on account-centric transaction models. In the research related to Ethernet, literature \[[16](#oebps-html-619883_1_en_1_chapter-xhtml-cr16)] introduces three ways of modelling Ethernet transaction data networks, i.e., the money flow network, the smart contract creation network and the smart contract invocation network. In all three networks, EOA and contract accounts are abstracted as nodes of the network, but the semantics of edges in the three networks differ. In the money flow network, edges denote the flow of money, while in the smart contract creation network and smart contract invocation network, edges denote the creation and invocation of contracts, respectively. Meanwhile, only the contract account can be the end point of an edge in the smart contract creation network and smart contract invocation network. Considering that multiple transactions occur between two accounts, literature \[[17](#oebps-html-619883_1_en_1_chapter-xhtml-cr17)] proposes to model Ethernet transaction records as a temporal multiplicity network. In this context, accounts are represented as nodes, and each transaction is represented as a directed edge pointing from the transaction sender to the transaction receiver, and each edge contains time and amount information. As a basic step of network analysis, network modelling directly affects the design and effect of upper layer algorithms, so it is very critical. There are many ways to model the current transaction network, but when performing network construction, we will face the problem of a wide variety of blockchain transaction operations, multiple sources of heterogeneous information and different downstream tasks. Thus, how to find a common modelling approach and modelling standard applicable to various blockchain data and different blockchain tasks is an important research direction.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec6"></a>

### 1.2.2 Transaction Network Analysis

Complex network theory has been widely demonstrated to be an effective tool for modelling and describing various types of complex systems. In the last two decades, researchers related to complex networks have proposed a variety of research metrics to characterise and measure networks. This subsection will briefly introduce some important network metrics and the performance of blockchain on these metrics to help understand the unique properties of blockchain cryptocurrency trading networks.

**(a) Number of Nodes and Edges**

The number of points and edges in a network is a common metric for measuring the size and density of the network. In their analysis of blockchain cryptocurrency transaction networks, Maesa et al. \[[18](#oebps-html-619883_1_en_1_chapter-xhtml-cr18)] observed that the network size of the Bitcoin transaction network grows faster than linearly. Alqassem et al. \[[19](#oebps-html-619883_1_en_1_chapter-xhtml-cr19)] also noticed this phenomenon and found that the Bitcoin transaction network is becoming denser and its degree distribution follows a power law distribution. Chen et al. \[[16](#oebps-html-619883_1_en_1_chapter-xhtml-cr16)] counted the number of nodes and edges in the Ethernet number of nodes and edges in the money flow network, smart contract creation network, and smart contract invocation network, and found that users’ transfer behaviours are more frequent than the creation of smart contracts and invocation of smart contracts in Ether.

**(b) Degree Distribution**

In an undirected network, the degree of a node is the number of edges of the node. In a directed network, the degree of a node is divided into in-degree and out-degree, the number of edges that start at a node is called the out-degree of that node, and the number of edges that end at a node is called the in-degree of that node. The degree distribution can represent the probability distribution of the degree of a node in a network and is calculated as follows

\$$\\displaystyle \\begin{aligned} p(k) = \\frac{\\mbox{the number of nodes with degree}~k}{\\mbox{the number of all nodes}}. \\end{aligned} $$

(1.1)

One interesting feature in complex network science is that the degree distribution of many realistic systems follows a power-law distribution which can be written as:

\$$\\displaystyle \\begin{aligned} p(k) = Ck^{-\\alpha}, \\end{aligned} $$

(1.2)

where *C* and \$$\\alpha $$ are constants and *k* is the value of the degree. Kondor et al. \[[20](#oebps-html-619883_1_en_1_chapter-xhtml-cr20)] found that both the in-degree distribution and out-degree distribution of Bitcoin address networks are highly heterogeneous. It has been observed that the degree distribution of many cryptocurrency transaction networks follows a power law. For example, Motamed and Bahrak \[[21](#oebps-html-619883_1_en_1_chapter-xhtml-cr21)] fitted a power-law distribution on the transaction networks for five kinds of cryptocurrencies and found that the power-law parameter \$$\\alpha $$ converges to a steady-state after some fluctuations.

**(c) Path Length**

The path length between two nodes in a network is defined as the minimum number of edges that have to traverse when connecting these two nodes. It is often calculated by the breadth-first search algorithm which can find the shortest path from one node to the other. The diameter of a network is the greatest path length of all the shortest paths in the network. Lischke and Fabian \[[22](#oebps-html-619883_1_en_1_chapter-xhtml-cr22)] showed that the average shortest path of Bitcoin user networks of different countries is in the same range. According to the change of diameter over time, Gaihre et al. \[[23](#oebps-html-619883_1_en_1_chapter-xhtml-cr23)] deduced the anonymity concerns of users in Bitcoin. Alqassem et al. \[[19](#oebps-html-619883_1_en_1_chapter-xhtml-cr19)] analyzed the four possible reasons for the increase in the diameter of Bitcoin transaction networks, namely, anonymity, thieves, the change addresses, and Bitcoin mixing services. Besides, many studies assess the “small-world” phenomenon in Bitcoin and Ethereum by calculating the average shortest path \[[24](#oebps-html-619883_1_en_1_chapter-xhtml-cr24), [25](#oebps-html-619883_1_en_1_chapter-xhtml-cr25)].

**(d) Clustering Coefficient**

The clustering coefficient describes the tendency of nodes to gather together in a network. Two measures of the clustering coefficient include the average of the local clustering coefficients and the global clustering coefficient. The local clustering coefficient quantifies the mean probability that two nodes sharing a common neighbor are also themselves neighbors. The global clustering coefficient measures the fraction of paths of length two in the network that are closed \[[26](#oebps-html-619883_1_en_1_chapter-xhtml-cr26)] and can be calculated by:

\$$\\displaystyle \\begin{aligned} C_g = \\frac{1}{n}\\sum_{v}{\\frac{t_v}{k_v(k_v-1)/2}}, \\end{aligned} $$

(1.3)

where *n* is the number of nodes, \$\$k_v\$$ is the degree of node *v* in the undirected network, and \$\$t_v\$$ is the number of triangles containing node *v*. Baumann et al. \[[14](#oebps-html-619883_1_en_1_chapter-xhtml-cr14)] observed that Bitcoin user networks have a rather high average clustering coefficient and typical “small-world” property. Similar results have also been found in the MFG of Ethereum \[[16](#oebps-html-619883_1_en_1_chapter-xhtml-cr16)]. Yet recent studies revealed that the clustering coefficient of transaction networks of Ripple and Namecoin is relatively low \[[27](#oebps-html-619883_1_en_1_chapter-xhtml-cr27), [28](#oebps-html-619883_1_en_1_chapter-xhtml-cr28)].

**(e) Centrality**

There are many kinds of centrality measures for networks, which can quantify the importance of a node in a network. The simplest centrality measure is node degree, and other widely considered centrality measures include eigenvector centrality, Katz centrality, PageRank, betweenness centrality, and closeness centrality. Lischke and Fabian \[[22](#oebps-html-619883_1_en_1_chapter-xhtml-cr22)] applied the degree centrality to identify major hubs in Bitcoin from September 2012 to April 2013. They found that during this period, exchanges, gambling businesses, and web wallet services were the top major hubs in the Bitcoin ecosystem. Chen et al. \[[16](#oebps-html-619883_1_en_1_chapter-xhtml-cr16)] listed the top 10 most important nodes in MFG, CCG, and CIG by PageRank. They found that financial applications such as exchanges play an important role in money transfer, contract creation, and contract invocation. For the Ethereum ERC20 ecosystem, top traders selected by PageRank have transactions with each other with a high frequency \[[29](#oebps-html-619883_1_en_1_chapter-xhtml-cr29)].

**(f) Assortativity Coefficient**

The assortativity coefficient measures the tendency of nodes to connect with other nodes in some similar ways. For example, the degree assortativity coefficient implies whether nodes in a network prefer to interact with others having a similar degree. A positive value of the assortativity coefficient with a maximum of 1 implies that the connectivity within the network is assortative mixing, while a negative value with a minimum of \$\$-\$$1 implies disassortative mixing, and 0 implies uncorrelation. A series of studies suggested that many blockchain systems like Bitcoin, Ethereum, Litecoin, and Dash are reported to be disassortative in their cryptocurrency transaction network \[[16](#oebps-html-619883_1_en_1_chapter-xhtml-cr16), [20](#oebps-html-619883_1_en_1_chapter-xhtml-cr20), [21](#oebps-html-619883_1_en_1_chapter-xhtml-cr21)].

**(g) Connected Component**

In undirected networks, a connected component is defined as a subgraph where each node can be reached from any others. While in directed networks, the concept of connected component includes weakly connected component and strongly connected component. The definition of weakly connected components is similar to that of connected components in undirected networks. A strongly connected component is the maximal set of nodes where there exists at least one directed path between each pair of nodes. While for calculating the weakly connected components, the edge directions are ignored in the directed networks. Statistics and analyses of connected components can help us understand the network structure. Gaihre et al. \[[23](#oebps-html-619883_1_en_1_chapter-xhtml-cr23)] observed that the number of connected components in the Bitcoin transaction network soared before 2011 but shrank later since many exchanges sprang up around 2010 and 2011, which promoted the circulation of bitcoins. Similar to other networks, most of the Bitcoin addresses are included in the largest connected component (LCC) of the Bitcoin transaction network as reported in \[[19](#oebps-html-619883_1_en_1_chapter-xhtml-cr19)]. For Ethereum, Guo et al. \[[30](#oebps-html-619883_1_en_1_chapter-xhtml-cr30)] found that the distribution of the finite component size can be approximated by the power-law model where a heavy-tailed property exists.

**(h) Community**

Community is network modules with internally dense connections and externally sparse connections. A network can be partitioned into a given number of communities with community detection algorithms. The partition of different communities presumably reflects the partition of functionality within a network. Alqassem et al. \[[19](#oebps-html-619883_1_en_1_chapter-xhtml-cr19)] investigated the properties of time-evolving community structure in Bitcoin. Their study found that the distribution of community sizes can be fitted by the exponentially truncated power law, and the majority of Bitcoin communities have a tree-like structure. Moreno-Sanchez et al. \[[28](#oebps-html-619883_1_en_1_chapter-xhtml-cr28)] studied how communities are formed in Ripple, they observed that user communities are dynamic and are formed via connecting to gateways in the same geographical region.

**(i) Network Motif**

Network motifs in complex networks are defined as recurrent subgraph patterns whose occurring number is significantly higher than that in randomized networks. Motifs are an efficient tool to reveal higher-order organizations in networks, and they are well known as the simple building blocks in complex systems. Bai et al. \[[31](#oebps-html-619883_1_en_1_chapter-xhtml-cr31)] investigated thirteen kinds of 3-node motifs in MFG of Ethereum, and classified these motifs into closed and open triplets, finding that though the number of closed triplets has increased, its proportion shows a decreasing tendency. And the average time for an open triplet to be closed ranges from 37 to 64 days. Paranjape et al. \[[32](#oebps-html-619883_1_en_1_chapter-xhtml-cr32)] observed that the fraction of cyclic triangle motifs is much higher in Bitcoin compared to any other datasets like StackOverflow. Moreno-Sanchez et al. \[[28](#oebps-html-619883_1_en_1_chapter-xhtml-cr28)] classified wallets into gateways, market makers, and users, and concluded that gateways are the key roles in Ripple from the most frequent motif, which is consistent with the network properties of low clustering coefficient and disassortativity. In addition to the well-known network properties mentioned above, some researchers have studied blockchain transaction networks from several new perspectives. For example, unlike previous studies that focused only on global network properties, Ron et al. \[[33](#oebps-html-619883_1_en_1_chapter-xhtml-cr33)] focused on user behaviour on the Bitcoin transaction network, including how users use Bitcoin, how they transfer Bitcoin between different accounts, and analysed the largest transactions that occur in the Bitcoin system. They found that most bitcoins are dormant and that the network has many strange looking structures such as binary tree structures, long chains. Lischke et al. \[[22](#oebps-html-619883_1_en_1_chapter-xhtml-cr22)] analysed the user network and economics of the bitcoin system in conjunction with off-chain data including business labels, IP addresses and geographic locations. They provide insights into the distribution of businesses and transactions in different countries, as well as the network nature of the transaction sub-networks involved in different businesses and different countries, respectively. Building on previous studies \[[34](#oebps-html-619883_1_en_1_chapter-xhtml-cr34), [35](#oebps-html-619883_1_en_1_chapter-xhtml-cr35)], Maesa et al. \[[36](#oebps-html-619883_1_en_1_chapter-xhtml-cr36)] analysed the outliers of the degree distribution in the Bitcoin user network and found some unusual transaction patterns. Through network analysis, Gaihre \[[23](#oebps-html-619883_1_en_1_chapter-xhtml-cr23)] answered the question of whether Bitcoin users care about anonymity or not, and they found that most of the users are weakly concerned about anonymity, but an important influencing factor is the value of bitcoins owned by the users. Chen et al. \[[29](#oebps-html-619883_1_en_1_chapter-xhtml-cr29)] investigated the creators, holders, and token trading activities of Ether’s ERC20 tokens through transaction network analysis. Liang et al. \[[27](#oebps-html-619883_1_en_1_chapter-xhtml-cr27)] studied the transaction network properties of three blockchain cryptocurrencies and analysed the competitiveness of these three cryptocurrencies in terms of these properties. Although current research has adequately covered the analysis of network properties of mainstream blockchain cryptocurrency trading networks in different time periods, the existing research discussion is very preliminary in terms of the time-series analysis of network properties and the generation and evolution of trading networks. Meanwhile, few studies have revealed the similarities and differences between blockchain cryptocurrency transaction networks and traditional citation networks and social networks. In the future, a more in-depth discussion on the network nature of blockchain cryptocurrency transaction networks can be conducted, and the characteristics of transaction networks can be combined to assist downstream tasks.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec7"></a>

### 1.2.3 Recognition Techniques on Transaction Networks

Since blockchain transactions do not require real user identification information, many blockchain cryptocurrency platforms have become hotbeds for various cybercrimes and illegal financial activities. Detection and identification techniques based on the development of blockchain transaction networks can help us identify abnormal transaction behaviours on the blockchain. The next section will introduce entity recognition, transaction pattern recognition and illegal activity detection. Among them, entity recognition can help find account addresses belonging to the same user or organisation, which is usually the basis for subsequent analysis tasks, and transaction pattern recognition distinguishes and identifies the transaction behaviours of different types of users, which provides the basis for subsequent illegal activity detection.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec8"></a>

#### 1.2.3.1 Entity Identification

Most blockchain cryptocurrency platforms make it inexpensive to create a new account or address and do not require verification of a user’s real identity. As a result, users can easily use multiple account addresses to enhance the covertness of blockchain trading activities, an operation that is common in criminal cases involving blockchain transactions. Ron et al. first proposed the use of an “entity” to describe the owner of such multiple account addresses \[[33](#oebps-html-619883_1_en_1_chapter-xhtml-cr33)], where the entity can be a user or an organisation. an organisation. In order to uncover the real identity information behind the blockchain account addresses, it is first necessary to correlate multiple account addresses belonging to the same entity, which is also known as entity identification. Existing entity identification methods are broadly classified into three types: entity identification based on transaction attributes, entity identification based on behaviour, and entity identification based on off-chain information. Entity identification based on transaction attributes mainly uses attributes specific to blockchain transactions to determine whether account addresses belong to the same entity. In the Bitcoin system, transactions have multiple inputs and multiple outputs, and since spending a bitcoin of an address requires the provision of the private key of that address, users normally do not share the private keys of the bitcoin addresses they own. Therefore, Reid et al. \[[13](#oebps-html-619883_1_en_1_chapter-xhtml-cr13)] considered the multiple input addresses of a Bitcoin transaction to be under the control of the same entity and in this way performed entity identification of the addresses in the Bitcoin system in an approach known as the multiple-input heuristic. Harrigan et al. \[[34](#oebps-html-619883_1_en_1_chapter-xhtml-cr34)] further investigated the effectiveness of this heuristic and found that the multiple-input heuristic could lead to miss-detections and misclassification errors. And both errors may be due to various factors such as address reuse, super clustering and continuous growth of address clusters. Remy et al. \[[37](#oebps-html-619883_1_en_1_chapter-xhtml-cr37)] proposed a new entity recognition method by combining multi-input heuristics and community detection techniques which increases recall at the cost of precision and hence can be adapted on its own in practical applications. Another typical approach for entity recognition using transaction attributes in the Bitcoin system is the zero-finding address heuristic, which was proposed by Reid et al. \[[13](#oebps-html-619883_1_en_1_chapter-xhtml-cr13)]. In Bitcoin transactions, additional change addresses are used to receive change, so we can identify the change address of the output side of the transaction and associate it with the corresponding input address. Klusman et al. \[[38](#oebps-html-619883_1_en_1_chapter-xhtml-cr38)] point out that the multiple-input heuristic and the find-change-address heuristic methods do not apply to blockchain systems such as Ether, based on an account-centric transaction model. To address this issue, Victor \[[35](#oebps-html-619883_1_en_1_chapter-xhtml-cr35)] proposed three heuristic rules on Ether: deposit account reuse, airdrop multiple participation, and self-authorisation. The deposit account reuse rule is designed in the context of exchanges. Indeed, exchanges usually generate deposit accounts for their users, and once a user transfers funds to his/her deposit account, this money is later automatically transferred to a hot wallet belonging to the exchange. When deposit accounts are reused, it is possible to identify a series of other accounts using the same deposit account as the same entity. The Airdrop Multiple Participation Rule is designed for airdrop situations, where airdrops are a common marketing method for raising funds for ICOs by distributing tokens. Since some users will register multiple accounts to participate in an airdrop and aggregate tokens into a single account, these accounts can be recognised as the same entity. The self-authorisation rule is based on the assumption that token consumers and token owners can be identified as the same entity when calling the authorisation function. After experimental analysis and validation, Victor concluded that the deposit account rule is the most effective method in the experiment. Behaviour-based entity identification uses user-specific behavioural preferences during transactions to determine whether multiple account addresses belong to the same entity, and thus some researchers consider the entity identification problem as a classification or clustering problem based on transaction behavioural features. Androulaki et al. \[[39](#oebps-html-619883_1_en_1_chapter-xhtml-cr39)] considered a number of transaction behavioural features, including the transaction time, the index of the counterparty, and the amount of the transaction, etc., and through the feature-based feature-based clustering revealed nearly 40% of user identities. Jourdan et al. \[[40](#oebps-html-619883_1_en_1_chapter-xhtml-cr40)] explored five types of features including address features, entity features, time features, centrality features, and modal features and investigated the effectiveness of these features in the task of classifying bitcoin addresses. Harlev et al. \[[41](#oebps-html-619883_1_en_1_chapter-xhtml-cr41)] used transaction behavioural features as inputs to supervised learning for bitcoin address de anonymisation. In addition, Shao et al. \[[42](#oebps-html-619883_1_en_1_chapter-xhtml-cr42)] converted the interactions of bitcoin addresses in a transaction network into low-dimensional feature vectors by means of network embedding and combined them with deep learning methods for entity recognition.

Blockchain off-chain data refers to relevant data not stored in the blockchain, which can be used to assist in the de-anonymisation process. Typical off-chain data includes IP addresses of nodes, publicly available tags, etc. Some users will collate and post fraudulent transaction addresses, mixed-coin service addresses, etc. in forums, which creates an opportunity to harvest this information through crawlers. At the same time, if a user exposes his address information, other addresses owned by the user can be found by analysing his transaction behaviour. Reid et al. \[[13](#oebps-html-619883_1_en_1_chapter-xhtml-cr13)] first applied this approach in entity identification and used off-chain information to identify some entities involved in theft. Based on the off-chain information provided on a Bitcoin forum, Fleder et al. \[[43](#oebps-html-619883_1_en_1_chapter-xhtml-cr43)] linked Bitcoin addresses to their corresponding real identities and found that some forum users had been involved in darknet transactions and gambling activities. Møser et al. \[[44](#oebps-html-619883_1_en_1_chapter-xhtml-cr44)] obtained relevant address information by using a mixing service and constructed a model for identifying mixing services by analysing the transactions of these address information.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec9"></a>

#### 1.2.3.2 Trading Pattern Recognition

In the blockchain cryptocurrency ecosystem, the trading behaviours of different users vary greatly, e.g., the trading activities of exchanges are far more active than those of ordinary users. Trading pattern recognition aims to reveal the particular structure of the trading network and further analyse users’ trading behaviours, and the relevant methods can be summarised as: visualisation methods, trace analysis and modal body analysis. Network visualisation is a powerful analytical method to intuitively understand the trading network and the trading patterns within it. McGinn et al. \[[45](#oebps-html-619883_1_en_1_chapter-xhtml-cr45)] discovered anomalous trading patterns including money laundering and denial-of-service attacks by visualising the Bitcoin trading network in some specific blocks. Chen et al. \[[46](#oebps-html-619883_1_en_1_chapter-xhtml-cr46)] visualised a subgraph of the daily trading network of anomalous addresses, and discovered a number of anomalous trading patterns related to the Bitcoin Chen et al. visualised a subgraph of the daily trading network of anomalous addresses and found some unusual trading patterns related to Bitcoin market price manipulation, such as self-loops, bidirectionals, triangles, etc. Meiklejohn et al. \[[47](#oebps-html-619883_1_en_1_chapter-xhtml-cr47)] found a special trading pattern called “Peeling Chain” in Bitcoin criminal activities. This pattern starts with an address holding a large number of Bitcoins, sequentially initiates a series of small expenditure transactions, and uses a disposable address to receive change, gradually transferring and dispersing the funds. McGinn et al. \[[48](#oebps-html-619883_1_en_1_chapter-xhtml-cr48)] visualise the source and target blocks of Bitcoin transactions as a neighbourhood matrix, and find that this visualisation method can easily reveal repeated transactions, and facilitates correlating transactions with similar behaviors. In the case where the identity of a particular account address is known, tracking and analysing the transactions of the account address is beneficial in summarising the trading patterns of that type of account. Maesa et al. \[[36](#oebps-html-619883_1_en_1_chapter-xhtml-cr36)] analysed the outliers of the degree distribution of the Bitcoin trading network, and by analysing these outliers, they noticed a type of swiping behaviour of the transactions. After further analysis, they concluded that these anomalous swipe transactions could be pseudonym attacks, spam attacks, or advertisement behaviours on the blockchain. Ron et al. \[[33](#oebps-html-619883_1_en_1_chapter-xhtml-cr33)] tracked large transactions of more than 50,000 BTC in the Bitcoin system and analysed the hidden transactional intent behind these transactions in long-chain and fork merge mode. A series of studies analysing the trading patterns of cryptocurrencies have been carried out by analysing the trading network modalities. Ranshous et al. \[[49](#oebps-html-619883_1_en_1_chapter-xhtml-cr49)] used directed hypergraphs to model the Bitcoin trading network and introduced network modalities in directed hypergraphs to reveal the trading patterns of the exchanges. Wu et al. \[[50](#oebps-html-619883_1_en_1_chapter-xhtml-cr50)] introduced the notion of temporal heterogeneous modalities in a temporally-directed Bitcoin trading network, which was used to address detection for bitcoin mashup services. Zola et al. \[[51](#oebps-html-619883_1_en_1_chapter-xhtml-cr51)] designed an entity recognition method using network modal features. Also, they investigated the similarity of transaction patterns of different entities over time and explored the question of whether there are some transaction patterns that are repeated in different batches of bitcoin transactions. Jourdan et al. \[[40](#oebps-html-619883_1_en_1_chapter-xhtml-cr40)] used network models to reveal the entity’s transaction pattern information and illustrate that transaction patterns can be viewed as fingerprints of entities through an entity identification task.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec10"></a>

#### 1.2.3.3 Illicit Activity Detection

The decentralised nature of the blockchain system and the fact that no real identity is required for transactions have not only attracted a large number of speculators, but also attracted the attention of many criminals, thus making the blockchain a hotbed for fraud, black market trade, money laundering and other illegal and criminal activities. Unlike traditional financial scenarios, blockchain systems cannot verify the identity of users by performing a Know Your Customer (KYC) process before conducting transactions. However, the public and immutable transaction records in blockchain systems provide us with the opportunity to detect illegal activities. Next, we will focus on reviewing blockchain financial fraud and money laundering detection efforts based on identification techniques on the transaction network. Financial fraud on blockchain systems poses a significant threat to the health of the cryptocurrency ecosystem. In a study by Vasek et al. \[[52](#oebps-html-619883_1_en_1_chapter-xhtml-cr52)] and others, multiple Bitcoin frauds including Ponzi schemes, mining scams, fraudulent wallets, and fraudulent transactions were reported and it was found that 13,000 potential victims lost about \$11 million in 192 fraud cases related to Bitcoin transactions. In addition, a rich variety of fraud types have been identified in other blockchain systems, such as ICO scams \[[53](#oebps-html-619883_1_en_1_chapter-xhtml-cr53)] and honeypot phishing contract scams \[[54](#oebps-html-619883_1_en_1_chapter-xhtml-cr54)]. Since blockchain fraud not only harms the interests of traders and investors, but also affects the reliability of blockchain transactions and people’s information about blockchain, some researchers have launched studies on blockchain fraud detection. Current detection methods include not only some feature extraction-based methods \[[55](#oebps-html-619883_1_en_1_chapter-xhtml-cr55)], but also some intelligent feature extraction-based detection methods. Tam et al. \[[56](#oebps-html-619883_1_en_1_chapter-xhtml-cr56)] proposed a graph convolutional neural network-based EdgeProp method to learn the embedding of nodes and edges in large-scale transaction networks. Unlike traditional graph convolutional neural network-based methods, EdgeProp learns the edge information of multiple edges, and thus effectively identifies illegal accounts on Ether. Wu et al. \[[57](#oebps-html-619883_1_en_1_chapter-xhtml-cr57), [58](#oebps-html-619883_1_en_1_chapter-xhtml-cr58)] proposed two random-walk based embedding methods, which take into account the characteristics of transaction volumes, timestamps, and multiple edges of the trading network when learning node embeddings, and verified the methods in a downstream phishing detection task to be Effectiveness. Money laundering is also an issue that needs to be regulated and taken seriously in blockchain systems. Money laundering is usually divided into three steps \[[59](#oebps-html-619883_1_en_1_chapter-xhtml-cr59)]: first, black money is injected into the financial system. Second, the black money is mixed into legitimate currencies and decoupled from illegal sources. Finally, the black money is consolidated and recovered by criminals and left in a seemingly legitimate state. Cryptocurrencies have become one of the options for hiding the flow of illicit money during money laundering due to the decentralised, transaction-anonymous nature of blockchain and the existence of many available privacy-preserving technologies. Elliptic, a prominent cryptocurrency intelligence firm, in its money laundering report on Bitcoin, identified exchanges, cryptocurrency mixing services, and gambling sites as the main streams of money laundering in Bitcoin \[[60](#oebps-html-619883_1_en_1_chapter-xhtml-cr60)]. As a result, research on money laundering detection on cryptocurrency trading networks in recent years has focussed on suspicious transaction patterns in coin-mixing services and exchanges. Bitcoin coin-mixing services were initially designed to enhance the anonymity of transactions by obfuscating the relationship between the input and the receiver of a transaction, making the source of funds more untraceable, but it is also known as a major tool to assist in illegal money laundering. Prado-Romero et al. \[[61](#oebps-html-619883_1_en_1_chapter-xhtml-cr61)] first emphasised the importance of coin-mixing service detection, and addressed coin-mixing service detection as a community outlier detection problem. This is because once mixed-coin services are detected, we can further analyse whether the account addresses interacting with these services are involved in illegal activities. However, the solutions in this work lack the ability to be automatically applicable to different types of mixed services. Wu et al. \[[50](#oebps-html-619883_1_en_1_chapter-xhtml-cr50)] further proposed a network modality-based detection approach, which automatically portrays the transaction patterns of different mixed services. In addition to mixed-coin service identification, Hu et al. \[[62](#oebps-html-619883_1_en_1_chapter-xhtml-cr62)] featured Bitcoin money laundering transaction patterns through feature characterisation and constructed a classifier for identifying money laundering transactions by using network embedding methods such as deepwalk \[[63](#oebps-html-619883_1_en_1_chapter-xhtml-cr63)] and node2vec \[[64](#oebps-html-619883_1_en_1_chapter-xhtml-cr64)]. Battista et al. \[[65](#oebps-html-619883_1_en_1_chapter-xhtml-cr65)] proposed the notion of purity to understand when and how Bitcoin is mixed, and built a bitcoin money flow visualisation system called BitConeView. Ranshous et al. \[[49](#oebps-html-619883_1_en_1_chapter-xhtml-cr49)] stated that exchanges provide a link between anonymous and real identities, and therefore studying the trading patterns of exchanges is an important step in anti-money laundering. They inscribed the suspicious money laundering patterns involved in exchanges with network modalities and used the network modalities as identifying features of exchanges.

In addition to financial fraud and money laundering issues, researchers have proposed other methods for detecting illegal activities on the blockchain based on transaction network identification techniques. Weber et al. \[[60](#oebps-html-619883_1_en_1_chapter-xhtml-cr60)] provide an Elliptic dataset on the Bitcoin system, which contains more than 200,000 transactional nodes, 234,000 transaction messages, and 166 node features. Transactions in this dataset are labelled into legitimate categories (e.g., exchanges, wallet providers, miners, and legitimate services), illegitimate categories (e.g., scams, malware, terrorist organisations, and ransomware), and unlabelled categories based on real entity information. Based on this dataset, the researcher used the EvolveGCN \[[66](#oebps-html-619883_1_en_1_chapter-xhtml-cr66)] method to identify and classify transactions. Due to the widespread use of cryptocurrencies in ransomware payments, Akcora et al. \[[67](#oebps-html-619883_1_en_1_chapter-xhtml-cr67)] proposed a topological information-based ransomware detection framework for detecting the addresses of known ransomware and emerging ransomware. Conti et al. \[[68](#oebps-html-619883_1_en_1_chapter-xhtml-cr68)] investigated the recent ransomware and its economic impact from the perspective of bitcoin payments and combined the information of co-entering transactions and zero-finding addresses to propose two clustering heuristics to identify ransomware-related addresses. During their investigation of the black market, Foley et al. \[[69](#oebps-html-619883_1_en_1_chapter-xhtml-cr69)] quantified illegal trading activities in Bitcoin and proposed two identification methods based on community detection and classification models. In addition, the authors point out through the results of their analysis that about half of the Bitcoin transactions are related to illegal activities.

In conclusion, these existing transaction network identification techniques are inevitably interfered by privacy-preserving techniques on the blockchain, and these two types of techniques are like a battle and contest between Mao and Shield, mutually prompting their respective technological innovations and developments. At present, the tricky task of detecting illegal activities on blockchain is only an afterthought, and there are fewer solutions that can be practically applied to early warning of illegal activities and tracking and interception of illegal funds. Therefore, in terms of the future, the identification technology on the blockchain transaction network still has a very large development space and application potential.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-sec11"></a>

## 1.3 Summary and Outlook

Most of the transaction data of blockchain cryptocurrencies is publicly accessible due to the transparency and openness of the blockchain system. By abstracting different objects in a cryptocurrency system as nodes and the transactional relationships between objects as connecting edges, blockchain cryptocurrency transaction data can be sadly modelled as large-scale complex networks. Over the past decade, researchers have conducted a large number of studies on blockchain transaction analysis from a network perspective. In this section, we provide a comprehensive review of the work related to blockchain transaction network research and summarise the existing techniques and results into three closely related and progressive parts, namely, transaction network modelling of blockchain cryptocurrencies, transaction network analysis, and identification techniques on transaction networks. From an overall perspective, the current field of blockchain cryptocurrency analysis has produced initial findings and theoretical results, while also advancing the development of complex network theory and graph mining techniques. By summarising and reflecting on the existing work, we propose some future research directions in the field of blockchain cryptocurrency transaction network analysis: (1) Dynamic information modelling and processing. Existing work on blockchain transaction network analysis and mining usually ignores temporal information, however, the blockchain network is a growing network, and the occurrence of new transactions is accompanied by the emergence of new nodes or new connected edges. These new nodes and new connecting edges may change the nature of the original network, and at the same time make the effectiveness of data mining models designed based on the original transaction network suffer. Thus, future work can further explore how to model dynamic blockchain transaction data, analyse the dynamic characteristics and evolution laws of the network, and design identification techniques that can adapt to network changes. (2) Transaction network data expansion. Data expansion of blockchain cryptocurrency transaction networks will be a major research direction worth looking forward to in blockchain transaction data analysis. On the one hand, in recent years, many off-chain transaction schemes for enhancing the scalability of blockchain have been proposed and initially applied, such as lightning network, thunderbolt network, etc., which will prevent us from obtaining all the blockchain transaction data. On the other hand, the transaction data of blockchain cryptocurrencies suffers from the problems of small number of tags and uneven number of tags in each category. Through network data expansion, we can restore some of the missing network structure information, provide effective information complementation to the transaction network, and alleviate the problem of difficult label acquisition to a certain extent, thus assisting blockchain transaction data analysis. (3) Transaction auditing and tracking. In blockchain transactions, users do not need to use real identity information, and some services and tools can be used to enhance the anonymity of transactions. While this enables better privacy protection for users, it also attracts many criminals who use blockchain transactions to evade regulation. Existing transaction de-anonymisation and tracking technologies are very limited, therefore, how to use transaction network analysis to achieve auditable transactions, traceability and interception of illegal transactions on a strongly anonymous, decentralised blockchain is an important research direction, not only to enhance compliance of blockchain transactions, but also to reduce the financial risk of users and potential investors.

<a id="oebps-html-619883_1_en_1_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr1"></a>Nakamoto, S.: Bitcoin: a peer-to-peer electronic cash system. [https://bitcoin.org/bitcoin.pdf](https://bitcoin.org/bitcoin.pdf) (2008)
2. 2\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr2"></a>Panarello, A., Tapas, N., Merlino, G., Longo, F., Puliafito, A.: Blockchain and IoT integration: a systematic survey. Sensors **18**(8), 2575 (2018)[Crossref](https://doi.org/10.3390/s18082575)
3. 3.Lu, Y.: Blockchain: a survey on functions, applications and open issues. J. Ind. Integr. Manag. **3**(04), 1850015 (2018)[Crossref](https://doi.org/10.1142/S242486221850015X)
4. 4\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr4"></a>Abbas, Q.E., Sung-Bong, J.: A survey of blockchain and its applications. In: Proc. Int. Conf. Artif. Intell. Inf. Commun., pp. 1–3. IEEE, Okinawa (2019)
5. 5\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr5"></a>Vinced: Namecoin - A distributed naming system based on Bitcoin. [https://bitcointalk.org/index.php?topic=6017.0](https://bitcointalk.org/index.php?topic=6017.0) (2011)
6. 6\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr6"></a>Lee, C.: Litecoin-open source p2p digital currency. [https://litecoin.org](https://litecoin.org) (2011)
7. 7\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr7"></a>King, S., Nadal, S.: PPCoin: peer-to-peer crypto-currency with proof-of-stake. [https://www.peercoin.net/](https://www.peercoin.net/) (2012)
8. 8\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr8"></a>Monero: Monero - a secure, private, untraceable cryptocurrency, Bitcoin forum. [https://bitcointalk.org/index.php?topic=583449.0](https://bitcointalk.org/index.php?topic=583449.0) (2014)
9. 9\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr9"></a>Sasson, E.B., Chiesa, A., Garman, C., Green, M., Miers, I., Tromer, E., Virza, M.: Zerocash: decentralized anonymous payments from Bitcoin. In: Proc. IEEE Symp. Secur. Priv., pp. 459–474. IEEE, Berkeley (2014)
10. 10\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr10"></a>Xu, B., Luthra, D., Cole, Z., Blakely, N.: EOS: an architectural, performance, and economic analysis. [https://whiteblock.io/wp-content/uploads/2019/07/eos-test-report.pdf](https://whiteblock.io/wp-content/uploads/2019/07/eos-test-report.pdf) (2018)
11. 11\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr11"></a>Amsden, Z., Arora, R., Bano, S., Baudet, M., Blackshear, S., Bothra, A., Cabrera, G., Catalini, C., Chalkias, K., Cheng, E., et al.: The Libra blockchain. [https://developers.libra.org/docs/assets/papers/the-libra-blockchain/2020-04-09.pdf](https://developers.libra.org/docs/assets/papers/the-libra-blockchain/2020-04-09.pdf) (2019)
12. 12\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr12"></a>Wood, G., et al.: Ethereum: a secure decentralised generalised transaction ledger. [http://gavwood.com/Paper.pdf](http://gavwood.com/Paper.pdf) (2014)
13. 13\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr13"></a>Reid, F., Harrigan, M.: An Analysis of Anonymity in the Bitcoin System, pp. 197–223. Springer, Berlin (2013)
14. 14\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr14"></a>Baumann, A., Fabian, B., Lischke, M.: Exploring the Bitcoin network. In: Proc. Int. Conf. Web. Inform. Syst. Technol., pp. 369–374. SciTePress, Barcelona (2014)
15. 15\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr15"></a>Maesa, D.D.F., Marino, A., Ricci, L.: Uncovering the Bitcoin blockchain: an analysis of the full users graph. In: Proc. IEEE Int. Conf. Data Sci. Adv. Anal., pp. 537–546. IEEE, Montreal (2016)
16. 16\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr16"></a>Chen, T., Zhu, Y., Li, Z., Chen, J., Li, X., Luo, X., Lin, X., Zhange, X.: Understanding Ethereum via graph analysis. In: Proc. IEEE Conf. Comput. Commun., pp. 1484–1492. IEEE, Honolulu (2018)
17. 17\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr17"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding Ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. II Express Briefs **67**(11), 2737–2741 (2020)
18. 18\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr18"></a>Maesa, D.D.F., Marino, A., Ricci, L.: Data-driven analysis of Bitcoin properties: exploiting the users graph. Int. J. Data Sci. Anal. **6**(1), 63–80 (2018)[Crossref](https://doi.org/10.1007/s41060-017-0074-x)
19. 19\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr19"></a>Alqassem, I., Rahwan, I., Svetinovic, D.: The anti-social system properties: Bitcoin network data analysis. IEEE Trans. Syst. Man Cybern. Syst. **50**(1), 21–31 (2020)[Crossref](https://doi.org/10.1109/TSMC.2018.2883678)
20. 20\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr20"></a>Kondor, D., Pósfai, M., Csabai, I., Vattay, G.: Do the rich get richer? An empirical analysis of the Bitcoin transaction network. PLoS One **9**(2), e86197 (2014)
21. 21\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr21"></a>Motamed, A.P., Bahrak, B.: Quantitative analysis of cryptocurrencies transaction graph. Appl. Netw. Sci. **4**(1), 1–21 (2019)[Crossref](https://doi.org/10.1007/s41109-019-0249-6)
22. 22\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr22"></a>Lischke, M., Fabian, B.: Analyzing the Bitcoin network: the first four years. Futur. Internet **8**(1), 7 (2016)[Crossref](https://doi.org/10.3390/fi8010007)
23. 23\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr23"></a>Gaihre, A., Luo, Y., Liu, H.: Do Bitcoin users really care about anonymity? An analysis of the Bitcoin transaction graph. In: Proc. IEEE Int. Conf. Big Data, pp. 1198–1207. IEEE, Seattle (2018)
24. 24\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr24"></a>Javarone, M.A., Wright, C.S.: From Bitcoin to Bitcoin cash: a network analysis. In: Proc. Work. Cryptocurrencies Blockchains Distrib. Syst., pp. 77–81. ACM, New York (2018)
25. 25\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr25"></a>Ferretti, S., D’Angelo, G.: On the Ethereum blockchain structure: a complex networks theory perspective. Concurr. Comput. Pract. Exp. **32**(12), e5493 (2020)[Crossref](https://doi.org/10.1002/cpe.5493)
26. 26\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr26"></a>Newman, M.E.J.: Networks: An Introduction. Oxford University Press, Oxford (2010)[Crossref](https://doi.org/10.1093/acprof:oso/9780199206650.001.0001)
27. 27\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr27"></a>Liang, J., Li, L., Zeng, D.: Evolutionary dynamics of cryptocurrency transaction networks: an empirical study. PLoS One **13**(8), 1–18 (2018)[Crossref](https://doi.org/10.1371/journal.pone.0202202)
28. 28\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr28"></a>Moreno-Sanchez, P., Modi, N., Songhela, R., Kate, A., Fahmy, S.: Mind your credit: assessing the health of the Ripple credit network. In: Proc. World Wide Web Conf., pp. 329–338. ACM, Lyon (2018)
29. 29\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr29"></a>Chen, W., Zhang, T., Chen, Z., Zheng, Z., Lu, Y.: Traveling the token world: a graph analysis of Ethereum ERC20 token ecosystem. In: Proc. World Wide Web Conf., pp. 1411–1421. ACM, Taipei (2020)
30. 30\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr30"></a>Guo, D., Dong, J., Wang, K.: Graph structure and statistical properties of Ethereum transaction relationships. Inf. Sci. (NY) **492**, 58–71 (2019)
31. 31\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr31"></a>Bai, Q., Zhang, C., Xu, Y., Chen, X., Wang, X.: Evolution of Ethereum: a temporal graph perspective. arXiv preprint arXiv:2001.05251 (2020)
32. 32\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr32"></a>Paranjape, A., Benson, A.R., Leskovec, J.: Motifs in temporal networks. In: Proc. ACM Int. Conf. Web Search Data Min., pp. 601–610. ACM, Cambridge (2017)
33. 33\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr33"></a>Ron, D., Shamir, A.: Quantitative analysis of the full Bitcoin transaction graph. In: Proc. Int. Conf. Financial Cryptogr. Data Secur., pp. 6–24. Springer, Okinawa (2013)
34. 34\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr34"></a>Harrigan, M., Fretter, C.: The unreasonable effectiveness of address clustering. In: Proc. Int. IEEE Conf. Ubiquitous Intell. Comput. Adv. Trust. Comput. Scalable Comput. Commun. Cloud Big Data Comput. Internet People, Smart World Congr., pp. 368–373. IEEE Computer Society, Toulouse (2016)
35. 35\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr35"></a>Victor, F.: Address clustering heuristics for Ethereum. In: Proc. Int. Conf. Financial Cryptogr. Data Secur., pp. 617–633. Springer, Kota Kinabalu (2020)
36. 36\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr36"></a>Maesa, D.D.F., Marino, A., Ricci, L.: An analysis of the Bitcoin users graph: inferring unusual behaviours. In: Proc. Int. Work. Complex Networks their Appl., vol. 693, pp. 749–760. Springer, Milan (2016)
37. 37\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr37"></a>Remy, C., Rym, B., Matthieu, L.: Tracking Bitcoin users activity using community detection on a network of weak signals. In: Proc. Int. Conf. Complex Networks their Appl., pp. 166–177. Springer, Lyon (2017)
38. 38\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr38"></a>Klusman, R., Dijkhuizen, T.: Deanonymisation in Ethereum using existing methods for Bitcoin. [https://homepages.staff.os3.nl/~delaat/rp/2017-2018/p61/report.pdf](https://homepages.staff.os3.nl/~delaat/rp/2017-2018/p61/report.pdf) (2018)
39. 39\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr39"></a>Androulaki, E., Karame, G.O., Roeschlin, M., Scherer, T., Capkun, S.: Evaluating user privacy in Bitcoin. In: Proc. Int. Conf. Financial Cryptogr. Data Secur., pp. 34–51. Springer, Okinawa (2013)
40. 40\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr40"></a>Jourdan, M., Blandin, S., Wynter, L., Deshpande, P.: Characterizing entities in the Bitcoin blockchain. In: Proc. IEEE Int. Conf. Data Min. Work., pp. 55–62. IEEE, Singapore (2018)
41. 41\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr41"></a>Harlev, M.A., Sun Yin, H., Langenheldt, K.C., Mukkamala, R., Vatrapu, R.: Breaking bad: de-anonymising entity types on the Bitcoin blockchain using supervised machine learning. In: Proc. Hawaii Int. Conf. Syst. Sci., pp. 3497–3506. ScholarSpace/AIS Electronic Library (AISeL), Hilton Waikoloa Village (2018)
42. 42\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr42"></a>Shao, W., Li, H., Chen, M., Jia, C., Liu, C., Wang, Z.: Identifying Bitcoin users using deep neural network. In: Proc. Int. Conf. Algorithms Archit. Parallel Process., pp. 178–192. Springer, Guangzhou (2018)
43. 43\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr43"></a>Fleder, M., Kester, M.S., Pillai, S.: Bitcoin transaction graph analysis. arXiv preprint arXiv:1502.01657 (2015)
44. 44\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr44"></a>Möser, M., Böhme, R., Breuker, D.: An inquiry into money laundering tools in the Bitcoin ecosystem. In: Proc. eCrime Res. Summit, pp. 1–14. IEEE, San Francisco (2013)
45. 45\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr45"></a>McGinn, D., Birch, D., Akroyd, D., Molina-Solana, M., Guo, Y., Knottenbelt, W.J.: Visualizing dynamic Bitcoin transaction patterns. Big data **4**(2), 109–119 (2016)[Crossref](https://doi.org/10.1089/big.2015.0056)
46. 46\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr46"></a>Chen, W., Wu, J., Zheng, Z., Chen, C., Zhou, Y.: Market manipulation of Bitcoin: evidence from mining the Mt. Gox transaction network. In: Proc. IEEE Conf. Comput. Commun., pp. 964–972. IEEE, Paris (2019)
47. 47\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr47"></a>Meiklejohn, S., Pomarole, M., Jordan, G., Levchenko, K., McCoy, D., Voelker, G.M., Savage, S.: A fistful of Bitcoins: characterizing payments among men with no names. In: Proc. Conf. Internet Meas. Conf., pp. 127–140. ACM Press, Barcelona (2013)
48. 48\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr48"></a>McGinn, D., McIlwraith, D., Guo, Y.: Towards open data blockchain analytics: a Bitcoin perspective. R. Soc. Open Sci. **5**(8), 180298 (2018)[Crossref](https://doi.org/10.1098/rsos.180298)
49. 49\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr49"></a>Ranshous, S., Joslyn, C.A., Kreyling, S., Nowak, K., Samatova, N.F., West, C.L., Winters, S.: Exchange pattern mining in the Bitcoin transaction directed hypergraph. In: Proc. Int. Conf. Financial Cryptogr. Data Secur., pp. 248–263. Springer, Malta (2017)
50. 50\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr50"></a>Wu, J., Liu, J., Chen, W., Huang, H., Zheng, Z., Zhang, Y.: Detecting mixing services via mining Bitcoin transaction network with hybrid motifs. IEEE Trans. Syst. Man Cybern. Syst. (2021, to be published). [https://doi.org/10.1109/TSMC.2021.3049278](https://doi.org/10.1109/TSMC.2021.3049278)
51. 51\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr51"></a>Zola, F., Bruse, J.L., Eguimendia, M., Galar, M., Orduna Urrutia, R.: Bitcoin and cybersecurity: temporal dissection of blockchain data to unveil changes in entity behavioral patterns. Appl. Sci. **9**(23), 5003 (2019)[Crossref](https://doi.org/10.3390/app9235003)
52. 52\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr52"></a>Vasek, M., Moore, T.: There’s no free lunch, even using Bitcoin: tracking the popularity and profits of virtual currency scams. In: Proc. Int. Conf. Financial Cryptogr. Data Secur., pp. 44–61. Springer, Puerto Rico (2015)
53. 53\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr53"></a>Bian, S., Deng, Z., Li, F., Monroe, W., Shi, P., Sun, Z., Wu, W., Wang, S., Wang, W.Y., Yuan, A., Zhang, T., Li, J.: Icorating: a deep-learning system for scam ICO identification. arXiv preprint arXiv:1803.03670 (2018)
54. 54\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr54"></a>Torres, C.F., Steichen, M., State, R.: The art of the scam: demystifying honeypots in Ethereum smart contracts. In: Proc. USENIX Secur. Symp., pp. 1591–1607. USENIX Association, Santa Clara (2019)
55. 55\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr55"></a>Monamo, P., Marivate, V.N., Twala, B.: Unsupervised learning for robust Bitcoin fraud detection. In: Proc. Inf. Secur. South Africa, pp. 129–134. IEEE, Johannesburg (2016)
56. 56\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr56"></a>Handason Tam, D.S., Lau, W.C., Hu, B., Ying, Q., Chiu, D.M., Liu, H.: Identifying illicit accounts in large scale e-payment networks - a graph representation learning approach. arXiv preprint arXiv:1906.05546 (2019)
57. 57\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr57"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: T-EDGE: temporal weighted multidigraph embedding for Ethereum transaction network analysis. Front. Phys. **8**, 204 (2020)[Crossref](https://doi.org/10.3389/fphy.2020.00204)
58. 58\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr58"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. (2020, to be published). [https://doi.org/10.1109/TSMC.2020.3016821](https://doi.org/10.1109/TSMC.2020.3016821)
59. 59\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr59"></a>Bryans, D.: Bitcoin and money laundering: mining for an effective solution. Indiana Law J. **89**, 441–472 (2014)
60. 60\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr60"></a>Weber, M., Domeniconi, G., Chen, J., Weidele, D.K.I., Bellei, C., Robinson, T., Leiserson, C.E.: Anti-money laundering in Bitcoin: experimenting with graph convolutional networks for financial forensics. arXiv preprint arXiv:1908.02591 (2019)
61. 61\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr61"></a>Prado-Romero, M.A., Doerr, C., Gago-Alonso, A.: Discovering Bitcoin mixing using anomaly detection. In: Proc. Iberoam. Congr. Pattern Recognit., vol. 10657, pp. 534–541. Springer, Valparaíso (2017)
62. 62\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr62"></a>Hu, Y., Seneviratne, S., Thilakarathna, K., Fukuda, K., Seneviratne, A.: Characterizing and detecting money laundering activities on the Bitcoin network. arXiv preprint arXiv:1912.12060 (2019)
63. 63\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr63"></a>Perozzi, B., Al-Rfou, R., Skiena, S.: DeepWalk: online learning of social representations. In: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 701–710. Association for Computing Machinery, New York (2014)
64. 64\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr64"></a>Grover, A., Leskovec, J.: Node2vec: scalable feature learning for networks. In: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 855–864. Association for Computing Machinery, San Francisco (2016)
65. 65\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr65"></a>Di Battista, G., Di Donato, V., Patrignani, M., Pizzonia, M., Roselli, V., Tamassia, R.: Bitconeview: visualization of flows in the Bitcoin transaction graph. In: Proc. IEEE Symp. Vis. Cyber Secur., pp. 1–8. IEEE, Chicago (2015)
66. 66\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr66"></a>Pareja, A., Domeniconi, G., Chen, J., Ma, T., Suzumura, T., Kanezashi, H., Kaler, T., Leisersen, C.E.: EvolveGCN: evolving graph convolutional networks for dynamic graphs. arXiv preprint arXiv:1902.10191 (2019)
67. 67\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr67"></a>Akcora, C.G., Li, Y., Gel, Y.R., Kantarcioglu, M.: Bitcoinheist: topological data analysis for ransomware detection on the Bitcoin blockchain. arXiv preprint arXiv:1906.07852 (2019)
68. 68\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr68"></a>Conti, M., Gangwal, A., Ruj, S.: On the economic significance of ransomware campaigns: a Bitcoin transactions perspective. Comput. Secur. **79**, 162–189 (2018)[Crossref](https://doi.org/10.1016/j.cose.2018.08.008)
69. 69\.<a id="oebps-html-619883_1_en_1_chapter-xhtml-cr69"></a>Foley, S., Karlsen, J.R., Putniņš, T.J.: Sex, drugs, and Bitcoin: How much illegal activity is financed through cryptocurrencies? Rev. Financ. Stud. **32**(5), 1798–1853 (2019)[Crossref](https://doi.org/10.1093/rfs/hhz015)

# Part IIBlockchain Transaction Data Analysis

<a id="oebps-html-619883_1_en_2_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_2](https://doi.org/10.1007/978-981-97-4430-5_2)

# 2. Dynamic and Microscopic Traits of Typical Accounts

Jiajing Wu[1](#oebps-html-619883_1_en_2_chapter-xhtml-aff4) , Baoying Huang[1](#oebps-html-619883_1_en_2_chapter-xhtml-aff4) , Jieli Liu[1](#oebps-html-619883_1_en_2_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_2_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_2_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_2_chapter-xhtml-contactofauthor1"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_2_chapter-xhtml-contactofauthor2"></a>

**Baoying Huang (Corresponding author)Email:** [huangby27@mail2.sysu.edu.cn](mailto:huangby27@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_2_chapter-xhtml-contactofauthor3"></a>

**Jieli LiuEmail:** [liujli7@mail2.sysu.edu.cn](mailto:liujli7@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_2_chapter-xhtml-contactofauthor4"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

While most existing analytical models treat account interactions as a network and examine it from a static and global perspective, they neglect the exploration of dynamic and micro-level account characteristics. Therefore, we have conducted pioneering work in this chapter to delve into these aspects of various account types on Ethereum, such as exchanges and phishing entities. Our research involves describing and comparing the trading dynamics of these accounts. Subsequently, we create trading ego networks for each account and carefully examine their microscopic characteristics. The experimental results reveal the unique characteristics of different account types in terms of transaction characteristics and ego network properties, revealing their respective roles. It is worth noting that there are obvious differences between normal accounts and illegal accounts in terms of transaction neighbors and interaction patterns. Additionally, our observations indicate that criminal gangs may be involved in phishing schemes. Based on the conclusions of our account analysis, we designed a variety of account features for classification tasks. Experimental results confirm the utility of our proposed dynamic and micro-features in differentiating various account types. We believe our analysis will provide valuable insights into account classification efforts within Ethereum as well as other blockchain platforms.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec1"></a>

## 2.1 Introduction

Most analytical work on Ethereum has focused solely on static transaction properties \[[1](#oebps-html-619883_1_en_2_chapter-xhtml-cr1), [2](#oebps-html-619883_1_en_2_chapter-xhtml-cr2)]. After selecting all Ethereum transactions at a certain moment, they created a snapshot of the Ethereum system as the object of analysis. For example, in terms of transaction pattern analysis \[[3](#oebps-html-619883_1_en_2_chapter-xhtml-cr3), [4](#oebps-html-619883_1_en_2_chapter-xhtml-cr4)], Liu et al. \[[5](#oebps-html-619883_1_en_2_chapter-xhtml-cr5)] studied the trading volume, structural properties of transaction networks and other transaction patterns of various Ethereum accounts. Besides, most of prior data mining investigated the entire Ethereum network \[[6](#oebps-html-619883_1_en_2_chapter-xhtml-cr6), [7](#oebps-html-619883_1_en_2_chapter-xhtml-cr7)].

However, Ethereum generates over 90,000 transactions per day, indicating that it is a constantly updated system. If we only focus on Ethereum at a single moment, we will lose information about network trends. In addition, previous global network analysis did not differentiate between various account nodes. This leads us to ignore the behavior patterns of accounts that play important roles on Ethereum.

Different from past work, we focus on the dynamic and microscopic features of several typical Ethereum accounts. According to Etherscan’s label word cloud,<a id="oebps-html-619883_1_en_2_chapter-xhtml-fn1_source"></a>[1](#oebps-html-619883_1_en_2_chapter-xhtml-fn1) there are hundreds of types of accounts on Ethereum. First, we select several typical accounts on Etherscan’s label cloud for classification, including normal accounts and illegal accounts. Normal accounts are those that have no illegal activity, while illegal accounts are the opposite. Then we explore in depth the dynamic changes in account trading attributes, including factors such as trading volume. It not only provides insight into Ethereum’s development trajectory, but also reveals transaction patterns specific to each account category at different stages. Account trading rules include a set of preferences, including transaction types, amounts, and frequent interactions with counterparties. Furthermore, microscopic examination of these key accounts provides a more detailed picture of their trading behavior than a global analysis. Based on transaction ego networks, we calculate different properties such as network density and prevalence patterns.

In a word, our study identifies dynamic and microscopic characteristics of accounts, an aspect less explored in previous research. To further confirm the importance of these features in account classification, we adopt a series of machine learning algorithms as classifiers in our experiments.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec2"></a>

## 2.2 Data Preparation for Account Profiling

This section describes the comprehensive approach taken to collect the account profiling and classification dataset. Initially, we select six different tagged accounts from the Ethereum website that are critical to the operation of Ethereum. We then collect the necessary transaction records, extracting important details such as transaction amount and timestamp. Ultimately, these transaction records become the basis for building a transaction ego network for each account, contributing to the characterization of trading behavior.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec3"></a>

### 2.2.1 Problem Description

This chapter is dedicated to studying the transaction behavior and account neighborhoods of various account types in the Ethereum ecosystem, aiming to refine the dynamic and microscopic characteristics that are beneficial to account classification. Our analysis unfolds in three stages. First, we choose six common account types, including normal accounts and illegal accounts. Secondly, we quantify the changing transaction behavior of these accounts at different stages, describing and comparing changes in financial attributes such as trading volume and amount. Finally, we delve into subnetwork densities, clustering coefficients, and prevalent patterns based on each account’s trading ego network. Our goal is to uncover key insights about accounts, which will subsequently serve as account attributes for the final account classification task.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec4"></a>

### 2.2.2 Data Collection

Etherscan is a widely used blockchain research platform that takes a multi-faceted approach to labeling numerous Ethereum accounts. This process involves incorporating different sources of evidence, such as user feedback and real-world events. Notably, Etherscan’s labeled data has been one of the data sources for past Ethereum research \[[8](#oebps-html-619883_1_en_2_chapter-xhtml-cr8), [9](#oebps-html-619883_1_en_2_chapter-xhtml-cr9)]. According to Etherscan’s label word cloud and previous work \[[10](#oebps-html-619883_1_en_2_chapter-xhtml-cr10)], Exchange, Mining, ICO Wallet, Gambling, Phish and Ponzi accounts are the most common and significant Ethereum accounts. As of the time of writing this chapter, we collect all accounts on Etherscan across these categories, as shown in Table [2.1](#oebps-html-619883_1_en_2_chapter-xhtml-tab1). The roles they play in the world of Ethereum are as follows. <a id="oebps-html-619883_1_en_2_chapter-xhtml-tab1"></a>

***Table 2.1***

The number of each type of Ethereum account

| Exchange | Mining | ICO wallet | Gambling | Phish | Ponzi |
| --- | --- | --- | --- | --- | --- |
| 280 | 62 | 168 | 36 | 3908 | 48 |

1. 1\.

   \$\$\\mathbf {Exchange}\$$: Accounts of online platforms that offer users the service of buying and selling various cryptocurrencies.

2. 2\.

   \$\$\\mathbf {Mining}\$$: Accounts of miners that verify and package the blockchain transaction.

3. 3\.

   \$\$\\mathbf {ICO Wallet}\$$: Accounts of wallets that raise funds for new cryptocurrency offerings.

4. 4\.

   \$\$\\mathbf {Gambling}\$$: Accounts of online platforms offering gambling services.

5. 5\.

   \$\$\\mathbf {Phish}\$$: Accounts of phishing scam operators.

6. 6\.

   \$\$\\mathbf {Ponzi}\$$: Accounts of Ponzi scheme operators.

In order to build ego networks, we download all Ethereum transaction records from XBlock,<a id="oebps-html-619883_1_en_2_chapter-xhtml-fn2_source"></a>[2](#oebps-html-619883_1_en_2_chapter-xhtml-fn2) including external and internal transactions. XBlock is a platform that provides abundant and open-source blockchain datasets \[[11](#oebps-html-619883_1_en_2_chapter-xhtml-cr11), [12](#oebps-html-619883_1_en_2_chapter-xhtml-cr12)]. The data file contains a large number of transaction records, and their respective fields and meanings are shown in Table [2.2](#oebps-html-619883_1_en_2_chapter-xhtml-tab2). <a id="oebps-html-619883_1_en_2_chapter-xhtml-tab2"></a>

***Table 2.2***

Details of Ethereum transaction data

| Field | Description |
| --- | --- |
| Timestamp | The Unix timestamp when the transaction occurs |
| From | The transaction initiator address, 20-byte string |
| To | The transaction recipient address, 20-byte string |
| Value | The transaction amount(*wei*), \$\$1 ETH=10^{18} wei\$$ |
| isError | The transaction status, *None* means success status |

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec5"></a>

### 2.2.3 Data Processing

The ego network \[[13](#oebps-html-619883_1_en_2_chapter-xhtml-cr13), [14](#oebps-html-619883_1_en_2_chapter-xhtml-cr14)] is often used to study the relationship between a central object and its neighbors. In the ego network, the network nodes are composed of only one central node and the neighbors of this node. Its edges contain the interactions between the central node *EGO* and its first-order neighbors *ALTER*, as well as the interactions between *ALTER*s. In this chapter, we treat each labeled account as an *EGO*, and select all first-order transactions that each *EGO* participates in. In other words, if a transaction’s *from* or *to* address is a labeled account, it is a first-order transaction for this *EGO*. Obviously, the other account that interacts with this *EGO* is its first-order neighbor. For each *EGO*, we collect its all first-order transactions, as well as the transactions that occurred between its first-order neighbors.

However, the account profiling and classification dataset contains numerous records that are irrelevant for subsequent analysis. Hence, we eliminate all transactions with zero value and self-loop transactions. Failed transactions, where the *isError* field isn’t *None*, are also deleted. So far, we have obtained a 500 GB Ethereum transaction account profiling and classification dataset with nearly 700 million records.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec6"></a>

### 2.2.4 Network Construction

We construct a transaction ego network for each labeled account, denoted by \$\$G=(V, E)\$$. As shown in Fig. [2.1](#oebps-html-619883_1_en_2_chapter-xhtml-fig1), *V* includes the labeled account *EGO* and its first-order transaction neighbor *ALTER*s. The set of transaction records obtained before is represented by *E*. Each directed edge is expressed as \$\$e=(t,u,v,w)\$$, which means that at time *t*, the *from* account *u* transfers *Ether* of amount *w* (which has been converted from *wei* to *ETH*), to the *to* account *v*. It is obvious that each transaction ego network represents a multi-edge directed network. We categorize the ego networks of accounts into six groups based on the account’s label type. In the subsequent analysis, the aggregate characteristics of each type are depicted by the average feature value across all accounts within the group.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig1"></a>

***Fig. 2.1***

An example of an ego network

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec7"></a>

## 2.3 Evolution of Transaction Features

Transaction attributes offer a direct reflection of the behavioral characteristics of an Ethereum account. In this section, we commence by computing the lifespan of each account and segmenting it into corresponding time intervals. Subsequently, we delve into the temporal evolution of transaction characteristics, such as transaction amount and the number of neighbors.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec8"></a>

### 2.3.1 Life Cycles of Accounts

In the Ethereum system, thousands of new accounts are generated every day, exhibiting a wide range of transaction frequencies. Therefore, the lifetime of an account is often used as the first factor to analyze, as one of the indicators of the account’s activity level. As explained in the previous overview, each transaction is associated with a Unix timestamp *t*. We define the lifetime of an account as the duration between its last transaction and its first transaction (until the data is collected). Since the unit of Unix timestamp is seconds, we need to change the unit of the calculation result to days, which can be written as \$$Life\\,\\,Cycle = (t\_{last} - t_{first}) / 86{,}400 $$.

For each type of account, we calculate the mean, median, and standard deviation over their lifetime. According to statistics in Table [2.3](#oebps-html-619883_1_en_2_chapter-xhtml-tab3), the life cycle distribution of all normal accounts is significantly different from that of illegal accounts. Taking exchange accounts and phishing accounts as examples, we plot the distribution of their life cycles in Fig. [2.2](#oebps-html-619883_1_en_2_chapter-xhtml-fig2). It is evident that over 80% of Phish accounts exhibit a life cycle of fewer than 300 days, whereas the life cycle of Exchange accounts displays a uniform distribution. Exchange accounts, serving as intermediaries for Ethereum transactions, boast the longest lifespans, attributable to their pivotal role in buying and selling Ethereum. Additionally, approximately half of Phish and Ponzi accounts showcase a life cycle of around 20 days. This is because criminals withdraw funds immediately after committing fraudulent activity and then leave the account idle. Unlike traditional social platforms, Ethereum account registration does not require identity verification, allowing fraudsters to remain anonymous by creating new accounts for each scam. This approach poses a difficult challenge to arresting cryptocurrency fraudsters. In addition, the standard deviation of the lifetime of illegal accounts is smaller, which means that the length of their lifetimes is relatively consistent compared to normal accounts.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig2"></a>

***Fig. 2.2***

Comparison of the life cycle of Exchange account and Phish accounts

<a id="oebps-html-619883_1_en_2_chapter-xhtml-tab3"></a>

***Table 2.3***

Statistics for the life cycle of accounts (days)

|  | Normal |  |  |  | Illegal |  |
| --- | --- | --- | --- | --- | --- | --- |
| Label | Exchange | Mining | ICO wallet | Gambling | Phish | Ponzi |
| Mean | 932.32 | 813.95 | 747.92 | 490.42 | 114.76 | 123.06 |
| Median | 915.28 | 764.97 | 702.88 | 352.74 | 15.56 | 23.07 |
| Std. | 503.82 | 465.85 | 477.22 | 431.78 | 238.41 | 297.85 |

In order to effectively observe the transaction characteristics of Ethereum accounts at each stage of the life cycle, we must establish an appropriate time window length *T* for each period. However, given the huge differences in account lifespan, a fixed time window is not suitable. Referring to the previous work \[[15](#oebps-html-619883_1_en_2_chapter-xhtml-cr15)], we consider it appropriate for analysis when *T* is equal to one-fifth of the life size of the account. Henceforth, the active duration of each account is segmented into five periods for subsequent analysis, denoted as P1 through P5 respectively.

**Finding 1** The life cycle of illegal accounts is much shorter than that of normal accounts. And most illegal accounts have similar life.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec9"></a>

### 2.3.2 Changes in the Number of Transactions

We first focus on the number of transactions, which is one of the characteristics that can intuitively reflect Ethereum transaction activity. As shown in Fig. [2.3](#oebps-html-619883_1_en_2_chapter-xhtml-fig3), it can be seen that except ICO Wallet accounts, the number of transactions of normal accounts far exceeds that of illegal accounts. Exchange, Mining and Gambling accounts have more than 10,000 transactions at each period. This phenomenon also coincides with their status as important hub nodes on Ethereum. Generally speaking, users buy and sell Ethereum on the exchange platform. And miners package transactions to generate new blocks and cryptocurrency rewards. Moreover, Gambling accounts attract users to play games for earning cryptocurrency rewards. All of these accounts contribute greatly to the circulation of Ethereum, which is the key factor for Ethereum to remain prosperous. At the same time, we also find that the number of transactions of ICO Wallet, Gambling, Phish and Ponzi accounts has a downward trend. Particularly, Phish accounts have less than 25 transactions at each period and only several transactions at the end of their life. In contrast, the number of transactions on another illegal account, the Ponzi account, remained at around 100. This also shows that Ponzi schemes are more deceptive than phishing scams and will not be detected quickly. So they can have a longer life cycle and more transactions.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig3"></a>

***Fig. 2.3***

The number of transactions per period

Indeed, transactions between accounts within Ethereum are directional in nature. For any given Ethereum account, its transactions can be categorized as either transfer-in or transfer-out transactions. In transfer-in transactions, the account receives Ether, while in transfer-out transactions, the account sends Ether to other accounts. In order to analyze the changes in the proportion of two kinds of transactions in each period, we set an indicator called \$$\\beta $$, which equals the number of incoming transactions divided by the number of outgoing transactions. The up and down arrows are used in Table [2.4](#oebps-html-619883_1_en_2_chapter-xhtml-tab4) to indicate the change in the value of \$$\\beta $$ compared to the previous period. <a id="oebps-html-619883_1_en_2_chapter-xhtml-tab4"></a>

***Table 2.4***

Changes in metric \$$\\beta $$

When \$$\\beta $$ is greater than 1, it means that there are more transfer-in transactions. If \$$\\beta $$ is less than 1, it means that there are more transfer-out transactions. Accounts with more incoming transactions than outgoing transactions throughout their lifetime include ICO Wallets, Gambling and Phish accounts. In the early days, ICO Wallets mainly accepted investments and raised funds, resulting in an excessively large proportion of initial transfer transactions. As the project progresses and matures, the number of transfer-in and transfer-out transactions gradually becomes balanced. Conversely, Gambling accounts often have more participants than winners, resulting in higher transaction volumes involving receiving funds rather than paying out winnings. Additionally, the Phish account continues to receive Ethereum from its victims, and at the end of its lifetime, \$$\\beta $$ increases significantly. The transaction history of the Phish account shows that after the scammers have achieved satisfactory profits in the final period, they will stop the phishing activities and perform multiple transfer transactions to transfer the funds elsewhere.

In contrast, Ponzi accounts use the strategy of returning late-stage investor funds to early-stage investors as bonuses multiple times, disguised as legitimate projects. Despite its large number of external transactions, the amount transferred out of the Ponzi account is much less than the profit, which can be proved from the analysis of transaction amounts in the next section.

Taking the Ponzi address *0x67ad530ecdfd7ac8289362914e88d018e8b3f3f0* as an example, part of the code of its smart contract for dividend distribution is shown in Fig. [2.4](#oebps-html-619883_1_en_2_chapter-xhtml-fig4). This implies that when new investments are transferred in, the Ponzi contract initiates a function to distribute dividends to all existing investors, resulting in transfer-out transactions. Specifically, the term “deposits” in line 1 refers to the queue of old investors, while the code in lines 3–12 is utilized to distribute rewards to each old investor. Consequently, whenever a transfer-in transaction transpires in a Ponzi account, multiple transfer-out transactions are triggered. Consequently, the number of transfer-out transactions of the Ponzi account significantly exceeds the number of transfer-in transactions.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig4"></a>

***Fig. 2.4***

An example of part of a Ponzi contract code

When an Exchange account transfers Ether to other accounts, it means that a user is purchasing Ether on the exchange platform. From an investment standpoint, users typically opt to buy Ether at varying price levels and subsequently sell it at a higher price, maximizing their returns \[[16](#oebps-html-619883_1_en_2_chapter-xhtml-cr16)]. As a result, the proportion of transfer-out transactions of Exchange accounts is larger and rising.

Another label characterized by a substantial proportion of outgoing transactions is Mining. Upon receiving Ethereum rewards for processing transactions, mining pools distribute bonuses to investors based on the proportion of their original investments. Consequently, the prevalence of transfer-out transactions is notably high. As the \$$\\beta $$ value of Mining accounts continues to rise, it suggests that certain investors are augmenting their investments in mining pools, potentially expediting the formation of monopolistic mining pools.

**Finding 2** Exchange, Mining and Gambling accounts have the most transactions at different stages. Ponzi accounts maintain a stable number of transactions and disguise themselves better.

**Finding 3** Different from the Phish account, the Ponzi account has a larger proportion of outgoing transactions, which is in line with the disguised behavior of the Ponzi account to distribute dividends.

**Finding 4** The increasing proportion of incoming transactions from Mining accounts suggests that investors are increasing their investment in mining pools.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec10"></a>

### 2.3.3 Changes in the Amount of Transactions

Unlike social networks, the connections between nodes in the Ethereum transaction network convey amount information, offering deeper insights into the activities of accounts. In this section, Fig. [2.5](#oebps-html-619883_1_en_2_chapter-xhtml-fig5) shows the amount of the two kinds of transaction in different periods.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig5"></a>

***Fig. 2.5***

Changes of the transaction amount per period. (**a**) Exchange. (**b**) Mining. (**c**) ICO Wallet. (**d**) Gambling. (**e**) Phish. (**f**) Ponzi

Among normal accounts, Exchange accounts exhibit the highest trading volume, followed by Gambling, ICO Wallet, and Mining accounts. Notably, for Exchange accounts, starting from the second stage, the volume of outgoing transactions surpasses that of incoming transactions, consistent with the proportional change of their outgoing transactions. This trend aligns with the emergence of decentralized exchanges like Uniswap and PancakeSwap, where users increasingly opt for seamless trading experiences with faster speeds and lower fees. Consequently, the transaction volume of centralized exchanges experiences a gradual decline. Overall, the income and expenditure of Exchange accounts remain largely balanced, affirming their role as trading intermediaries.

Interestingly, the amount transferred out from Mining accounts is nearly ten times the amount transferred in, which might seem counterintuitive. However, this discrepancy arises because a significant portion of funds in Mining accounts stem from Ether rewards for transaction processing. These rewards are automatically allocated to the account by the system based on the consensus algorithm and do not constitute transaction behaviors. Upon examining the balances of all Mining accounts on Etherscan, we discover that 90% of Mining accounts possess balances of less than 100 ETH. This observation further corroborates that mining pools generally maintain a state of equilibrium after distributing mining rewards.

In the initial stage, the income amount of ICO Wallet accounts significantly exceeds the outgoing amount, likely due to fundraising activities. Subsequently, these funds are gradually transferred out to project-related accounts. While there are few transfer-out transactions in the later periods of ICO Wallets, the average amount of these transactions is substantial. Similarly, in the first half of the life cycle of Gambling accounts, the income exceeds the expenditure. However, the difference between income and expenditure for Gambling accounts is generally marginal in each period. Interestingly, aside from a few active gambling platforms and ICO wallets, most Gambling and ICO wallet accounts maintain balances close to zero.

Among illegal accounts, the transaction volume of Ponzi accounts significantly exceeds that of phishing accounts, highlighting the greater impact of Ponzi schemes on the Ethereum ecosystem. For Phish accounts, the vast majority of transfer amounts occur in the first period. In subsequent periods, especially the final phase, all ill-gotten gains are typically moved to exchanges for withdrawal or laundered through currency mixing services. In contrast, Ponzi accounts employ different money laundering strategies. They imitate normal DeFi projects and conduct regular transfer activities after receiving initial investment. A portion of the funds was returned to early investors, while the remainder was transferred to other accounts owned by the scammers. It’s worth noting that the amount of fraud associated with Ponzi schemes has gradually decreased over time. Additionally, the Ponzi scheme involves transferring ether in bulk through smart contract accounts with preset parameters. Therefore, the proportion of external transactions in Ponzi accounts remains large. On the other hand, Phish accounts lure victims to send funds to the phisher’s EOA (externally owned account) through phishing emails or links, allowing the phisher to freely transfer funds. It is worth noting that the transaction patterns and amounts of Ponzi accounts are very similar to ICO Wallets, which further complicates the task of distinguishing legitimate projects from Ponzi schemes for ordinary users.

**Finding 5** Due to the rise of decentralized exchanges, the transaction amount of the centralized exchanges are gradually declining. Most ICO Wallet and Gambling accounts have balances close to zero.

**Finding 6** Ponzi schemes are more profitable and more harmful than phishing scams. Their strategies for transferring funds also vary widely.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec11"></a>

### 2.3.4 Changes in the Number of Neighbors

Ethereum is a world of anonymity, and almost everyone does not know the real identity of each other. While we can still investigate the “social” nature of different Ethereum accounts by comparing the number of trading partners. The fluctuations in the number of transfer-in and transfer-out neighbors are illustrated in Fig. [2.6](#oebps-html-619883_1_en_2_chapter-xhtml-fig6).<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig6"></a>

***Fig. 2.6***

Changes of the transaction neighbors per period. (**a**) Exchange. (**b**) Mining. (**c**) ICO Wallet. (**d**) Gambling. (**e**) Phish. (**f**) Ponzi

Undoubtedly, Exchange accounts boast the highest number of trading neighbors. At each period, the number of transfer-out neighbors exceeds twice the number of transfer-in neighbors, aligning with the aforementioned observation that outgoing transactions from Exchange accounts constitute a significant proportion. Therefore, the substantial group of trading neighbors and outgoing transactions serve as crucial distinguishing characteristics of Exchange accounts from other accounts. Similarly, Mining accounts exhibit a disparity between the number of outgoing and incoming neighbors, with a significantly larger number of outgoing neighbors. Additionally, there is a noticeable increase in outgoing accounts associated with miners over time. It’s worth noting that the number of transfer-in neighbors of Mining accounts remains constrained within 50, largely due to the fact that block rewards are not categorized as transfer-in transactions. Furthermore, the change trends in the number of transaction neighbors for ICO Wallet accounts mirror those of the number of transactions. The number of transfer-in neighbors peaks in the initial period and steadily declines thereafter, while the number of transfer-out neighbors remains relatively constant.

Similarly, there is a tendency towards fewer trading neighbors for Gambling accounts. In most cases, the number of transfer-in neighbors (participants) far exceeds the number of transfer-out neighbors (winners) in gambling games. For illegal accounts, their transfer-in neighbors can be regarded as victims, while their transfer-out neighbors primarily comprise other accounts controlled by fraudsters. The curve in Fig. [2.6](#oebps-html-619883_1_en_2_chapter-xhtml-fig6)e indicates that Phish accounts have the fewest neighbors among all accounts. Furthermore, Phish accounts display a higher proportion of transfer-in neighbors, indicating that the number of victims of phishing scams exceeds the number of outgoing neighbors. Additionally, the number of victims of Ponzi schemes is nearly ten times that of phishing scams, underscoring the challenge users face in identifying Ponzi schemes promptly. Notably, Ponzi schemes feature more transfer-out neighbors than transfer-in neighbors from the second period onwards, in contrast to phishing scams. This phenomenon arises because Ponzi schemes return a portion of funds as dividends to previous trading neighbors, as corroborated by the analysis of old and new neighbors in the subsequent section.

**Finding 7** The large number of trading neighbors is one of the distinctive features of the exchange, which distinguishes it from other accounts. Phish accounts have the fewest trading neighbors.

**Finding 8** The number of transfer-in neighbors of the Mining account and the number of transfer-out neighbors of the ICO Wallet account remain almost constant.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec12"></a>

### 2.3.5 Changes in the Number of Old and New Neighbors

Apparently, the presence of fixed interaction partners is a distinctive feature of accounts. Consequently, in each life period of an Ethereum account, we classify neighbor accounts that appear for the first time as new neighbors, while accounts that have already appeared in previous periods are deemed old neighbors. For instance, all transaction neighbors in the first period are considered new neighbors. To delve deeper into the transaction propensity of accounts, we analyze the proportions of new and old neighbors among transaction partners, as depicted in Fig. [2.7](#oebps-html-619883_1_en_2_chapter-xhtml-fig7). Each bar in the figure is segmented into two non-overlapping parts. The height of the blue area represents the number of new neighbors, while the height of the red area represents the number of old neighbors.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig7"></a>

***Fig. 2.7***

Changes of the different neighbors per period. (**a**) Exchange. (**b**) Mining. (**c**) ICO Wallet. (**d**) Gambling. (**e**) Phish. (**f**) Ponzi

With the exception of Ponzi accounts, most accounts primarily interact with new neighbors, as observed in the case of Exchange accounts. Notably, Mining accounts exhibit a growing number of old neighbors over time. This trend can be interpreted as follows: the greater the number of new neighbors representing investors in the current phase, the higher the number of old neighbors who need to be rewarded in the subsequent phase. From the second period onward, ICO Wallet accounts consistently maintain 1–2 old neighbors, denoting stable trading partners. Comparing the neighbor features of ICO Wallet accounts in Figs. [2.6](#oebps-html-619883_1_en_2_chapter-xhtml-fig6) and [2.7](#oebps-html-619883_1_en_2_chapter-xhtml-fig7), it’s obvious that most new neighbors of ICO Wallets originate from outgoing transactions. Moreover, Gambling accounts and Phish accounts share a common trait: the majority of new neighbors stem from transfer-in transactions. In the case of Gambling accounts, this is because many transfer-in neighbors are new users attracted to gambling games. Conversely, victims of phishing scams are unlikely to be deceived a second time after transferring funds to Phish accounts once, resulting in mostly new neighbors with only one transfer experience. For normal accounts, the average number of transactions with old neighbors exceeds 20, indicating sustained long-term transactions with stable users. Conversely, the average number of transactions with old neighbors for illegal accounts is less than 10. Specifically, the average number of transactions per neighbor for Phish accounts is 1, suggesting that phishing scams are easily detected by users. The only labeled accounts exhibiting a larger proportion of old neighbors are Ponzi accounts, with this proportion exceeding 90% in the last period. This trend arises because Ponzi schemes typically return some cryptocurrencies to early victims, enticing them to continue transferring funds to the Ponzi contract. Furthermore, there are fewer and fewer new users joining the Ponzi “project”.

**Finding 9** Except for Ponzi accounts, other accounts mostly interact with new neighbors in various periods of life. And Ponzi accounts have, on average, more transactions with old neighbors than Phish accounts.

**Finding 10** The ICO Wallet account has 1–2 stable partners. Most new neighbors to Gambling and Phish accounts come from transfer-in transactions.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec13"></a>

## 2.4 Properties of Transaction Ego Network

In addition to transactional characteristics, the structural attributes of Ethereum accounts play a crucial role in observing transaction patterns. Exploring network properties such as network density and motifs enables us to gain a deeper understanding of the complexity of labeled account neighborhoods. Since multiple edges have minimal impact on inspecting network characteristics, we focus on analyzing the simple directed graph version of the ego network in this section.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec14"></a>

### 2.4.1 Temporal Variation of Network Density

The change in network density not only indicates the persistence trend of the network, but also implies the degree of connection of all nodes in the network. For an ego network \$\$G=(V, E)\$$, its density can be defined as

\$$\\displaystyle \\begin{aligned} {} density(G)= \\frac{|E|}{|V|*(|V| - 1)}, \\end{aligned} $$

(2.1)

where \$\$|\\cdot |\$$ stands for the operation to calculate the size of the set.

Therefore, we compute the average network density at different periods for each type of account. As depicted in Fig. [2.8](#oebps-html-619883_1_en_2_chapter-xhtml-fig8), the densities of ego networks for labeled accounts are all below 0.25, exhibiting a decreasing trend. Similarly, in the multi-edge directed graph version, the densities of networks are also on the decline. The results are consistent with the conclusions of work \[[6](#oebps-html-619883_1_en_2_chapter-xhtml-cr6)], which showed the densities of all four global Ethereum networks are decreasing. Consequently, we can deduce that as Ethereum evolves, an increasing number of nodes emerge in the transaction network of an account. However, the majority of node pairs have no transactions between them, resulting in a sparser network. Firstly, Phish accounts exhibit the highest network density among labeled accounts, significantly surpassing other types of accounts. This discrepancy can be attributed to the analysis of transaction neighbors above, wherein it is observed that Phish accounts have the smallest average number of subnet nodes. Thus, the number of nodes emerges as a key factor influencing network density. Secondly, we observe strikingly similar network densities between ICO Wallet and Ponzi accounts. The slightly higher density for ICO Wallet accounts can be attributed to their fewer neighbors compared to Ponzi accounts. Conversely, Gambling, Exchange, and Mining accounts possess numerous neighbors, leading to relatively sparse subnets. However, subnet size does not necessarily correlate with subnet density. For instance, although Exchange subnets boast the largest networks, with an average of more than 100,000 nodes per subnet, their subnet densities are not the lowest. Considering the local clustering coefficient analysis in the subsequent section, we will uncover another factor influencing network density. Mining account subnets emerge as the sparsest, as their neighbors rarely interact with each other. Additionally, the average clustering coefficient of Mining accounts is the smallest among all accounts.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig8"></a>

***Fig. 2.8***

The density of ego network per period

**Finding 11** The ego network for each account is getting sparser. We consider the number of nodes in the subnet to be a factor that affects the network density.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec15"></a>

### 2.4.2 Local Clustering Coefficient

When assessing the degree of association among the neighbors of *EGO*, the local clustering coefficient serves as a commonly utilized analytical tool. This metric provides valuable insights into the underlying reasons for the sparsity observed in Ethereum’s local structure.

In general, the local clustering coefficient of a node is obtained by dividing the number of connections between nodes in the neighborhood by the number of connections that may exist between them. Hence in the directed ego network \$\$G=(V,E)\$$ of \$\$EGO_i\$$, the local clustering coefficient is:

\$$\\displaystyle \\begin{aligned} {} C_i = \\frac{|\\{e\_{uv}:u, v\\in N_i,e_{uv} \\in E\\}|}{|N_i|*(|N_i| - 1)}, \\end{aligned} $$

(2.2)

where \$\$N_i\$$ represents the first-order neighbors of \$\$EGO_i\$$. The average local clustering coefficient \$\$C_{avg}\$$ of each type of account is equal to the average of the corresponding coefficients of all accounts of this type.

The results presented in Table [2.5](#oebps-html-619883_1_en_2_chapter-xhtml-tab5) indicate that the clustering coefficient of the ICO Wallet account is 0.031, surpassing all other accounts. This signifies that the likelihood of transactions occurring between the ICO Wallet’s neighbors is approximately 3.1%, suggesting a strong connection among the investors associated with the ICO Wallet compared to other account types. Utilizing the formula for network density calculation, it is evident that due to the relatively low number of neighbors of the ICO Wallet account, its network density tends to be higher. This observation is further supported by the curve depicted in Fig. [2.8](#oebps-html-619883_1_en_2_chapter-xhtml-fig8), illustrating that the network densities of ICO Wallet accounts outpace those of typical accounts. <a id="oebps-html-619883_1_en_2_chapter-xhtml-tab5"></a>

***Table 2.5***

The average clustering coefficient of Ethereum accounts

| Label | Exchange | Mining | ICO Wallet | Gambling | Phish | Ponzi |
| --- | --- | --- | --- | --- | --- | --- |
| \$\$C_{avg}\$$ | 0.022 | 0.008 | 0.031 | 0.015 | 0.018 | 0.015 |

Additionally, among normal accounts, the local clustering coefficients of Exchange and Gambling accounts rank second only to ICO Wallets. Surprisingly, despite Exchange accounts having numerous neighbors, the likelihood of transactions occurring between them isn’t insignificant. Consequently, their ego network densities surpass those of Mining accounts. Within illegal accounts, the Phish account has a larger clustering coefficient compared to the Ponzi account, indicating a higher likelihood of connectivity among the neighbors of the Phish account. This suggests the presence of an organized fraudulent group in phishing activities. Notably, the clustering coefficient of the Mining account is 0.008, the lowest among all labels. This data starkly demonstrates the lack of correlation among the outgoing neighbors of the mining pool. So far, we have concluded that the number of network nodes and the degree of clustering jointly determine the size of network density.

**Finding 12** The local clustering coefficient of Phish accounts is larger than that of Ponzi accounts, which can better prove that there may be phishing fraud gangs. And the clustering coefficient is another factor that determines the network density.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec16"></a>

### 2.4.3 Pattern Statistics

In complex networks, recurring local connection patterns often unveil underlying principles. In the Ethereum transaction ego network, we observe that besides the 2-node pattern, the 3-node pattern emerges as the most prevalent. The 2-node pattern signifies transactions between *EGO* and its neighbors, as discussed earlier. Thus, our attention in this section primarily centers on the 3-node pattern, comprising a subgraph involving three nodes and their interconnected edges.

As is shown in Fig. [2.9](#oebps-html-619883_1_en_2_chapter-xhtml-fig9), patterns from M1 to M13 illustrate thirteen distinct types of patterns. Among these, a bidirectional edge connecting two nodes signifies transactions occurring in both directions between them, implying that Ether has been sent between the two nodes reciprocally. For instance, the M1 pattern denotes a one-way loop involving three nodes with a path length of 3.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig9"></a>

***Fig. 2.9***

3-Node patterns

We identify the least-occurring pattern and the top three most-occurring patterns in each type of ego networks. Subsequently, we analyze the significance of these common patterns in conjunction with the various features discussed earlier. Among all accounts, the M4 pattern emerges as the least prevalent. This pattern, characterized by a two-way loop connecting three nodes, suggests a particularly close relationship among the nodes involved. However, such cases are exceptionally rare within the actual transaction network. On the contrary, the M8, M9, and M10 patterns dominate the subnets of Exchange and Mining accounts, constituting over 95% of occurrences. These patterns exhibit the simplest structure within the three-node pattern, featuring only two one-way edges. This indicates that Exchange and Mining accounts primarily engage in one-way transactions with the majority of their neighbors. In the M8 pattern, the *EGO* node serves as the central node, initiating transactions with the other two nodes. Given that Exchange and Mining accounts typically have a higher number of outgoing neighbors compared to incoming ones, M8 patterns frequently manifest in their transaction ego networks.

Additionally, ICO Wallet accounts predominantly exhibit the M10, M8, and M9 patterns. Unlike Exchange and Mining accounts, ICO Wallet accounts tend to have a higher proportion of transfer-in neighbors. Consequently, the M10 pattern, where the *EGO* node acts as the central point receiving Ether from the other two nodes, is the most prevalent. In the ego networks of Gambling accounts, the M9, M10, and M11 patterns are frequently observed. Considering the transaction neighbor characteristics of Gambling accounts, wherein the numbers of transfer-in and transfer-out neighbors are nearly equal, the M9 pattern emerges as the most common mode. Furthermore, the M11 pattern includes a bidirectional edge, constituting approximately 15% of all patterns in Gambling subnets. This finding suggests that at least 15% of users participating in gambling activities are successful in winning the game and receiving bonuses.

Finally, we conduct a comparative analysis of common network patterns among illegal accounts. The patterns with the highest frequency in Phish accounts are M10, M9, and M8, while those in Ponzi accounts are M9, M11, and M12. As mentioned earlier, Phish accounts tend to have a larger proportion of transfer-in neighbors, who are typically victims of phishing scams. Consequently, the Phish account often appears as the central node in the M10 pattern. In contrast, two out of the three common patterns in Ponzi schemes involve bidirectional edges. Considering the nature of Ponzi schemes, bidirectional edges are likely generated between Ponzi accounts and early investors, giving the appearance of a more credible project. Moreover, the prevalence of bidirectional edges suggests a higher level of connectivity between Ponzi accounts and their initial investors. Additionally, the proportion of M1-M7 patterns in the Phish account’s network is higher than that of the Ponzi account. These patterns signify a closely related structure among the three nodes, indicating a higher probability of fraud gangs within the ego network of Phish accounts.

**Finding 13** The three most frequent patterns can clearly explain the respective trading patterns of different accounts.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec17"></a>

## 2.5 Experiments of Trading Ego Networks

After the previous account analysis, we find that different Ethereum accounts have completely different dynamic transaction behavior and transaction neighborhood characteristics. Consequently, leveraging these findings, we design multiple account features and employ a range of classic machine learning models for account classification. Experimental results validate that the account features we have devised are instrumental in addressing the account classification problem effectively.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec18"></a>

### 2.5.1 Features Extraction

For each Ethereum account, we design two major categories of account features, namely, dynamic transaction features and microscopic subnet features.

Dynamic transaction features include *Original features*, *Difference features* and *Orientation features*. *Original features* refer to all transaction feature values for each period. For example, \$\$Origin\\\_amt\\_{P1}\$$ represents the sum of transaction amount of an account in the first period of its life. Difference features can better capture the dynamic changes of the original features. Specifically, for each transaction feature, we calculate the difference between each time slice and the feature in the previous time slice, and then use this result as the difference feature. For example, *Diff* \$\$\\_tx\\_P2\\_P1\$$ indicates the difference obtained by subtracting the total transaction quantity of P1 from the sum of transaction quantity of the account in P2. In order to make better use of the difference in the characteristics of transfer-in and transfer-out transactions, we design the direction feature. For each transaction feature, we calculate the ratio of transfer-in divided by transfer-out for each time slice. For example, \$\$Orient\\_nei\\_P1\$$ indicates the value of dividing the number of transfer-in neighbors of the account in P1 by the number of transfer-out neighbors. Microscopic subnet features include *Original features* and *Difference features*. For example, the original features include the subnet density of each time slice, the three most common pattern IDs, and so on. The calculation method of the difference characteristic is the same as that of the transaction difference characteristic.

So far, we have extracted 146 account features for each Ethereum account, which are used as the input of the subsequent machine learning models.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec19"></a>

### 2.5.2 Experiment Settings

We select four machine learning models most commonly used for blockchain account classification tasks \[[17](#oebps-html-619883_1_en_2_chapter-xhtml-cr17)]. They are Logistic Regression (LR), Random Forest (RF), Support Vector Machine (SVM) and Multilayer Perceptron (MLP). For each machine learning model, we use the default parameters of the *sklearn* library.

Due to the imbalance in the number of various accounts, we randomly select 50 accounts from Exchange, Mining, ICO Wallet, and Phish in each experiment, and added all Gambling and Ponzi accounts as samples. We divide these samples into training set and testing set according to the ratio of 8:2, and use 5-fold cross-validation on the training set. In the end, we conduct 10 repeated experiments, using *Accuracy*, *Precision*, *Recall*, and *F1-score* as classification performance indicators.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec20"></a>

### 2.5.3 Experiment Results

As depicted in Table [2.6](#oebps-html-619883_1_en_2_chapter-xhtml-tab6), the Random Forest model demonstrates the most effective classification performance, achieving a precision rate of 0.826 and a recall rate of 0.802. This superiority can be attributed to the Random Forest model’s utilization of multiple classification trees for discriminating and classifying data, rendering it more adept at handling multi-featured data and less prone to overfitting. Furthermore, we present the confusion matrix obtained using the Random Forest model in Fig. [2.10](#oebps-html-619883_1_en_2_chapter-xhtml-fig10). The matrix reveals that mining accounts and phishing accounts are readily distinguishable from other account types. However, Gambling accounts exhibit a 22% probability of being misclassified as Ponzi accounts. We speculate that this misclassification arises due to the high similarity in microscopic subnet characteristics between gambling and Ponzi accounts. Additionally, Gambling, Exchange, and Phish accounts share similarities in terms of the difference in the amount transferred in and transferred out, as well as the local clustering coefficient. Hence, in future iterations, our model will require additional features to effectively distinguish Gambling accounts from other account types.<a id="oebps-html-619883_1_en_2_chapter-xhtml-fig10"></a>

***Fig. 2.10***

The confusion matrix of the Random Forest model predictions

<a id="oebps-html-619883_1_en_2_chapter-xhtml-tab6"></a>

***Table 2.6***

Experiment results with different classification models

| Model | Accuracy | Precision | Recall | F1-score |
| --- | --- | --- | --- | --- |
| LR | 0.712 | 0.496 | 0.576 | 0.501 |
| **RF** | **0.821** | **0.826** | **0.802** | **0.797** |
| SVM | 0.737 | 0.471 | 0.583 | 0.518 |
| MLP | 0.782 | 0.662 | 0.733 | 0.692 |

Bold values indicate that the model’s classification performance is the best among the current experiments

To reveal the significance of individual features in multi-classifying accounts, we conduct experiments using dynamic transaction features, microscopic subnet features, and their combined features. Table [2.7](#oebps-html-619883_1_en_2_chapter-xhtml-tab7) presents the classification performance using the Random Forest model. Evidently, employing solely dynamic transaction features yields better classification results than using only microscopic subnet features. However, combining both features provides richer information for account classification, consequently yielding improved classification outcomes. This further shows that the account characteristics we designed can reveal the differences between different Ethereum accounts. <a id="oebps-html-619883_1_en_2_chapter-xhtml-tab7"></a>

***Table 2.7***

Experiment results with different features

| Features | Accuracy | Precision | Recall | F1-score |
| --- | --- | --- | --- | --- |
| Dynamic transaction features | 0.796 | 0.788 | 0.774 | 0.770 |
| Microscopic subnet features | 0.718 | 0.713 | 0.707 | 0.697 |
| **Combination features** | **0.821** | **0.826** | **0.802** | **0.797** |

Bold values indicate that the model’s classification performance is the best among the current experiments

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec21"></a>

## 2.6 Discussion

In the past, the Ethereum analysis work mainly focused on the global transaction network, including the large-scale nodes \[[18](#oebps-html-619883_1_en_2_chapter-xhtml-cr18)], rich-club phenomenon \[[7](#oebps-html-619883_1_en_2_chapter-xhtml-cr7)], and so on. These studies have significantly contributed to unveiling the developmental landscape of Ethereum. However, they primarily conducted characteristic statistics on all accounts uniformly, overlooking the nuanced differences among various account types to a certain extent. Furthermore, they seldom delved into the dynamic transaction behavior and micro-neighborhoods of the accounts. Therefore, our work represents the first comprehensive endeavor towards the dynamic and microscopic analysis of different types of accounts on Ethereum. Through the aforementioned sections, we have unearthed critical findings following multidimensional analysis. These insights are instrumental in distinguishing between various types of accounts, particularly aiding in the identification of illegal accounts.

**The Dynamic Traits**

Firstly, we observe that the lifespan of illegal accounts tends to be significantly shorter compared to normal accounts. For instance, approximately 80% of phishing accounts exhibit an active period of only about 30 days. Secondly, the number of transactions serves as a distinguishing characteristic among different account types. Exchange, Mining, and Gambling accounts tend to have the highest transaction volumes. Among illegal accounts, Ponzi accounts demonstrate a higher proportion of outgoing transactions, while Phish accounts exhibit the opposite trend. This indicates that Ponzi accounts often masquerade as distributing dividends, while phishing accounts tend to transfer the entire proceeds at once. Furthermore, Ponzi accounts and Phish accounts employ distinct strategies for transferring illicit amounts. Ponzi schemes typically distribute small portions of the illicit proceeds at each stage, whereas phishing scams usually transfer the entire amount at the final stage. We also analyze the important trait of an account that has received little attention, which is the account’s transaction neighborhood. Statistical findings suggest that Exchange accounts typically possess the highest number of trading neighbors, whereas Phish accounts tend to have the fewest trading neighbors. The number of transfer-in neighbors for Mining accounts and the number of transfer-out neighbors for ICO accounts remain relatively constant.

**The Microscopic Traits**

In our microscopic analysis, we introduce an innovative approach by constructing a transaction ego network for each account. This method enables us to better extract neighborhood characteristics of accounts compared to previous global network analyses. Through examining the changes in density within these ego networks, we observe a trend towards sparser networks across all accounts. This suggests that the Ethereum ecosystem is not densely interconnected. Furthermore, we find that the local clustering coefficient of Phish accounts surpasses that of Ponzi accounts. This observation raises the possibility of the existence of phishing fraud gangs on Ethereum, engaging in multiple interactions to launder illicit funds. Finally, we conduct a statistical analysis on the common interaction patterns within the ego networks of different account types. The results highlight distinct differences between normal accounts and illegal accounts in this regard. The results tell us that normal accounts and illegal accounts also have obvious differences in this feature.

**Applications**

In summary, our focus on dynamic and microscopic analysis of Ethereum accounts allows us to uncover a broader range of account characteristics compared to previous studies. Beyond merely explaining the diverse roles played by Ethereum accounts, our findings offer insights into the developmental trajectory of Ethereum. Moreover, we identify significant disparities between normal accounts and illegal accounts in key characteristics such as lifespan and transaction neighborhoods. Building upon these insights, we introduce two categories of account characteristics. Our experimental results demonstrate that combining dynamic transaction features with microscopic subnet features yields the best classification performance. We believe that our research holds substantial reference value for account classification and illegal account detection not only in Ethereum but also in other blockchain ecosystems.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-sec22"></a>

## 2.7 Conclusion

In recent years, the soil of Ethereum has also derived products such as NFT and Metaverse. With the rapid development, the Ethereum world has gradually matured. As a result, studying Ethereum blockchain data has also become a chance to investigate the rules of Ethereum.

For this purpose, we paid attention to several prominent accounts in the Ethereum ecosystem. They are either key hubs to promote the circulation of Ethereum, or projects and games that attract many participants. Especially, some of them are fraud accounts cheating huge amounts of money. Although there is a lot of research about Ethereum, most of them stay at the static and global level to analyze the final state of these accounts. Therefore, this chapter focused on the dynamic and microscopic features of target accounts. Exploring the changes of various transaction traits, such as transaction amount and neighbors, provided us with clearer and plentiful insights into the Ethereum world. Then, we compared several network attributes of various accounts from the perspective of transaction ego networks. In most aspects, significant differences existed between normal accounts and illegal accounts. We also found that the trading rules of Exchange and Mining accounts in normal accounts are the most stable and reliable. Besides, the structural relationship between accounts further explained the role identity of accounts. Besides, the statistics of common patterns revealed distinct neighborhood characteristics of different accounts. In a word, our analysis provided insights into Ethereum classic accounts from both dynamic and micro perspectives, drawing many novel conclusions about the dynamics features and local patterns. These findings filled in the dynamic and microscopic gaps of traditional analysis.

Finally, we designed several account characteristics based on the findings of the account analysis. By using multiple machine learning models, the experimental results proved that the account features we designed perform well in the multi-classification task of Ethereum accounts. In addition, we further found that dynamic transaction features have a greater effect on classification than microscopic subnet features through comparative experiments. This also showed that our account analysis and feature design method are of great benefit for blockchain account classification.

Furthermore, there are still some research problems that we can continue to explore. First of all, we only used the six most important account labels on Ethereum. More labeled accounts, such as airdrop hunters and honeypot smart contracts, also have quite distinctive personalities, which are worth in-depth analysis. In addition, this chapter obtained some useful transaction and subnet peculiarities about different accounts. For example, there are clear signs of criminal gangs in the subnetwork of Phish accounts, especially in terms of local clustering coefficients and motifs. But in this chapter, we only used several classic classifiers for experiments. In the future, we will also devote ourselves to expanding our research, using the findings of this chapter to design a better classification model combined with GNN, and further solve the problem of identifying anonymous accounts, especially abnormal accounts.

<a id="oebps-html-619883_1_en_2_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr1"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
2. 2\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr2"></a>Liu, X.F., Akcora, C.G., Zhang, Z.-Y., Liu, J.-G.: Cryptocurrency transaction analysis from a network perspective. Front. Phys., 215 (2022). [https://doi.org/10.3389/fphy.2022.876983](https://doi.org/10.3389/fphy.2022.876983)
3. 3\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr3"></a>Toyoda, K., Ohtsuki, T., Mathiopoulos, P.T.: Multi-class Bitcoin-enabled service identification based on transaction history summarization. In: Proceedings of the 2018 IEEE Conference on Internet of things, pp. 1153–1160. IEEE, Halifax (2018)
4. 4\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr4"></a>Tovanich, N., Cazabet, R.: Pattern analysis of money flows in the bitcoin blockchain. In: Proceedings of the 2022 International Conference on Complex Networks and Their Applications, pp. 443–455. Springer, Palermo (2023)
5. 5\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr5"></a>Liu, X.F., Ren, H.-H., Liu, S.-H., Jiang, X.-J.: Characterizing key agents in the cryptocurrency economy through blockchain transaction analysis. EPJ Data Sci. **10**(1), 21 (2021)[Crossref](https://doi.org/10.1140/epjds/s13688-021-00276-9)
6. 6\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr6"></a>Zhao, L., Sen Gupta, S., Khan, A., Luo, R.: Temporal analysis of the entire Ethereum blockchain network. In: Proceedings of the 2021 World Wide Web Conference, pp. 2258–2269. ACM, Ljubljana (2021)
7. 7\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr7"></a>Lee, X.T., Khan, A., Sen Gupta, S., Ong, Y.H., Liu, X.: Measurements, analyses, and insights on the entire Ethereum blockchain network. In: Proceedings of the 2020 World Wide Web Conference, pp. 155–166. ACM, Taipei (2020)
8. 8\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr8"></a>Yuan, Q., Huang, B., Zhang, J., Wu, J., Zhang, H., Zhang, X.: Detecting phishing scams on Ethereum based on transaction records. In: Proceedings of the 2020 IEEE International Symposium on Circuits and Systems (ISCAS), pp. 1–5. IEEE, Seville (2020)
9. 9\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr9"></a>Chen, W., Guo, X., Chen, Z., Zheng, Z., Lu, Y.: Phishing scam detection on Ethereum: towards financial security for Blockchain ecosystem. In: Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, pp. 4506–4512. IJCAI, Yokohama (2020)
10. 10\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr10"></a>Huang, T., Lin, D., Wu, J.: Ethereum account classification based on graph convolutional network. IEEE Trans. Circuits Syst. II: Express Briefs **69**(5), 2528–2532 (2022)
11. 11\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr11"></a>Zheng, P., Zheng, Z., Wu, J., Dai, H.-N.: XBlock-ETH: extracting and exploring blockchain data from Ethereum. IEEE Open J. Comput. Soc. **1**, 95–106 (2020)[Crossref](https://doi.org/10.1109/OJCS.2020.2990458)
12. 12\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr12"></a>Zheng, W., Zheng, Z., Dai, H.-N., Chen, X., Zheng, P.: Xblock-EOS: extracting and exploring blockchain data from EOSIO. Inf. Process. Manag. **58**(3), 102477 (2021)[Crossref](https://doi.org/10.1016/j.ipm.2020.102477)
13. 13\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr13"></a>Odella, F.: Using ego-network in surveys: methodological and empirical research issues. In: Proceedings of the International Conference on Network Science. Springer, Bloomington (2006)
14. 14\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr14"></a>Qian, G., Wang, S.: Generalized complex correntropy: application to adaptive filtering of complex data. IEEE Access **6**, 19113–19120 (2018)[Crossref](https://doi.org/10.1109/ACCESS.2018.2821141)
15. 15\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr15"></a>Huang, B., Liu, J., Wu, J., Li, Q., Lin, H.: Temporal analysis of transaction ego networks with different labels on Ethereum. arXiv preprint arXiv:2204.13253 (2022)
16. 16\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr16"></a>Shahriari, Z., Nazarimehr, F., Rajagopal, K., Jafari, S., Perc, M., Svetec, M.: Cryptocurrency price analysis with ordinal partition networks. Appl. Math. Comput. **430**, 127237 (2022)[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4425996)
17. 17\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr17"></a>Liu, X.F., Jiang, X.-J., Liu, S.-H., Tse, C.K.: Knowledge discovery in cryptocurrency transactions: a survey. IEEE Access **9**, 37229–37254 (2021)[Crossref](https://doi.org/10.1109/ACCESS.2021.3062652)
18. 18\.<a id="oebps-html-619883_1_en_2_chapter-xhtml-cr18"></a>Chen, T., Li, Z., Zhu, Y., Chen, J., Luo, X., Lui, J.C.-S., Lin, X., Zhang, X.: Understanding Ethereum via graph analysis. ACM Trans. Internet Technol. **20**(2), 1–32 (2020)[Crossref](https://doi.org/10.1145/3381036)

**Footnotes**

[1](#oebps-html-619883_1_en_2_chapter-xhtml-fn1_source)<a id="oebps-html-619883_1_en_2_chapter-xhtml-fn1"></a>

[https://cn.etherscan.com/labelcloud](https://cn.etherscan.com/labelcloud).

[2](#oebps-html-619883_1_en_2_chapter-xhtml-fn2_source)<a id="oebps-html-619883_1_en_2_chapter-xhtml-fn2"></a>

[https://xblock.pro/xblock-eth.html](https://xblock.pro/xblock-eth.html).

<a id="oebps-html-619883_1_en_3_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_3](https://doi.org/10.1007/978-981-97-4430-5_3)

# 3. Evolution of Global Driving Factors in Ethereum Transaction Networks

Dan Lin[1](#oebps-html-619883_1_en_3_chapter-xhtml-aff4) , Jingjing Yang[1](#oebps-html-619883_1_en_3_chapter-xhtml-aff4) , Jialan Chen[1](#oebps-html-619883_1_en_3_chapter-xhtml-aff4) , Jiajing Wu[1](#oebps-html-619883_1_en_3_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_3_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_3_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_3_chapter-xhtml-contactofauthor1"></a>

**Dan Lin (Corresponding author)Email:** [lind8@mail2.sysu.edu.cn](mailto:lind8@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_3_chapter-xhtml-contactofauthor2"></a>

**Jingjing Yang (Corresponding author)Email:** [yangjj93@mail2.sysu.edu.cn](mailto:yangjj93@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_3_chapter-xhtml-contactofauthor3"></a>

**Jialan ChenEmail:** [chenjlan6@mail2.sysu.edu.cn](mailto:chenjlan6@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_3_chapter-xhtml-contactofauthor4"></a>

**Jiajing WuEmail:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_3_chapter-xhtml-contactofauthor5"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

The evolution mechanism of Ethereum transactions is a significant but rarely mentioned topic, whereas the majority of current research in Ethereum transaction records concentrates on statistical analysis and measurements of the available data. In this chapter, we first collect Ethereum transaction data and create micro-level network models, after which we quantify the influence of network properties on Ethereum evolution using a link-prediction based approach. We then investigate the characteristics of the graph structure and the forces that give rise to newly formed transaction links. According to experimental findings, Ethereum networks have a star-shaped local and microscopic structure, and the growth of Ethereum transaction relationships is significantly influenced by the frequency of address transactions. The first-layer nodes of micro-structures control the network’s evolution. In addition, the degree of addresses provides a useful foundation for forecasting the path of incoming transactions. There is a discussion of possible future research on Ethereum transaction link prediction, such as the label effect of center addresses.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec1"></a>

## 3.1 Introduction

Owing to the rising prominence and quick rise in market capitalization \[[1](#oebps-html-619883_1_en_3_chapter-xhtml-cr1)–[5](#oebps-html-619883_1_en_3_chapter-xhtml-cr5)], a lot of research has been done on Ethereum \[[6](#oebps-html-619883_1_en_3_chapter-xhtml-cr6)]: (1) The security and Ethereum blockchain system. For a more robust and secure Ethereum blockchain platform, system enhancement and security concerns have received a lot of attention, as seen in the works of \[[7](#oebps-html-619883_1_en_3_chapter-xhtml-cr7)–[11](#oebps-html-619883_1_en_3_chapter-xhtml-cr11)]. (2) Applications and smart contracts. Because Ethereum smart contracts are so powerful, a lot of research has been done on Ethereum-based applications (e.g. \[[12](#oebps-html-619883_1_en_3_chapter-xhtml-cr12), [13](#oebps-html-619883_1_en_3_chapter-xhtml-cr13)]). (3) A market study on *Ether* cryptocurrency. Han et al. \[[14](#oebps-html-619883_1_en_3_chapter-xhtml-cr14)], for instance, first examined the volume-return causality, multi-fractality, and long-range dependence of the *Ether* market and offered insightful information on *Ether* investment. (4) Mining and analyzing Ethereum data. Blockchain systems keep their rich information-rich transaction records openly available to the public. As seen in Fig. [3.1](#oebps-html-619883_1_en_3_chapter-xhtml-fig1), Ethereum has amassed a sizable amount of user transaction records every day since its launch.<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig1"></a>

***Fig. 3.1***

Ethereum daily transactions chart

There is a good deal of research on data mining and analysis of Ethereum transaction records due to the high value of large-scale financial interactions. A temporally weighted multidigraph was proposed by Lin et al. \[[15](#oebps-html-619883_1_en_3_chapter-xhtml-cr15)] to simulate Ethereum transaction records. The study concluded that edges’ multiplicity characteristic and temporal information are crucial for time-sensitive transaction networks. A thorough identification model was proposed by Wu et al. \[[16](#oebps-html-619883_1_en_3_chapter-xhtml-cr16)] to identify phishing scams on Ethereum. To extract the features of addresses, *trans2vec*, a network embedding approach, is proposed. Security flaws were found in the source code of Ponzi schemes gathered from the Ethereum blockchain by Bartoletti et al. \[[17](#oebps-html-619883_1_en_3_chapter-xhtml-cr17)]. Huang et al. \[[18](#oebps-html-619883_1_en_3_chapter-xhtml-cr18)] described the transactions, account creation, and contract invocation as the first steps toward revealing new insights into the EOSIO blockchain. The Ethereum on-chain data was gathered and processed by Zheng et al. \[[19](#oebps-html-619883_1_en_3_chapter-xhtml-cr19)], who also provided some basic statistics and exploration. Wu et al. \[[20](#oebps-html-619883_1_en_3_chapter-xhtml-cr20)] presented a method for mixing detection in anti-money laundering. Using sample blockchain systems like Bitcoin and Ethereum, data extraction, exploration, and analytics were covered in the book *Blockchain Intelligence* \[[21](#oebps-html-619883_1_en_3_chapter-xhtml-cr21)].

The aforementioned study mostly covered the mining and static analysis of transaction records and the associated transaction networks at a specific point in time. Though it is still in its early stages of development, the Ethereum market is evolving quickly and is not as stable as the established market. We may therefore gain a better understanding of the development trend of the cryptocurrency market by examining the generating rules of transactions between Ethereum addresses and the evolution mechanisms of the complete transaction relationship. Furthermore, the development of innovative financial technologies (*Fintech*) \[[22](#oebps-html-619883_1_en_3_chapter-xhtml-cr22)] and regulatory technologies (*RegTech*) \[[23](#oebps-html-619883_1_en_3_chapter-xhtml-cr23)] benefits from a thorough analysis of the evolution of the Ethereum transaction relationship.

The dynamics and growth of Ethereum transaction connections have drawn more and more attention from researchers in the past few years. Chen et al. \[[24](#oebps-html-619883_1_en_3_chapter-xhtml-cr24)] presents a small-scale analysis of the evolution of Ethereum transactions by examining how network metrics change over time, such as the number of nodes, edges, clustering coefficient, Pearson coefficient, etc. Bai et al. \[[25](#oebps-html-619883_1_en_3_chapter-xhtml-cr25)] examined the Ethereum transactions from a temporal graph view within a suitable time window to comprehend the evolutionary behaviors. They also examined the evolution of the graph metrics over time. Important insights for the study of the blockchain transaction relationship based on complex networks can be gained from the work discussed above. These investigations typically abstract the transaction relationship into a network made up of nodes (node \$$\\equiv $$ vertex) and edges (edge \$$\\equiv $$ link), after which the network topology is statistically examined in a largely macroscopic way. On the other hand, transaction specifics and local patterns of transaction relationships have received minimal attention in this way.

In contrast to abstract networks, transaction networks have nodes and edges that store rich address and transaction data, respectively. Thus, the goal of this chapter is to determine how the evolution of the entire transaction network is related to the features and patterns of local and micro transactions. Transaction features for Ethereum transaction networks include number of transactions, amount of transactions, frequency of transactions, etc. We model network evolution as a link prediction issue and investigate how the transaction features affect the link prediction performance \[[26](#oebps-html-619883_1_en_3_chapter-xhtml-cr26)] to uncover the mechanism and driving forces of Ethereum transaction networks.

The main contributions of this chapter are listed as follows:

- We provide a newly defined hierarchical graph model, dubbed *haloed K-order subgraph*, where nodes represent Ethereum addresses and edges represent Ethereum transactions, to more accurately describe the local structure of transaction networks. We can assess the local topological structure of Ethereum transaction interactions thanks to this new subgraph.
- This is the *first* study to examine the development of the local and microscopic Ethereum transaction relationship. We discover that the growth of transactions concentrates on a particular level of subgraphs, and that the microscopic structure of Ethereum transaction links is star-shaped.
- We design scoring methods of link prediction problem to measure the influence of various network properties on the development of Ethereum transaction networks, with the goal of identifying the crucial elements that propel new transactions. The findings indicate that the evolution of Ethereum transaction networks is significantly influenced by the transaction frequency of addresses.

The remainder of this chapter is organized as follows. An introduction to link-prediction based network evolution and a summary of the suggested framework are provided in Sect. [3.2](#oebps-html-619883_1_en_3_chapter-xhtml-sec2). We discuss our methodology for gathering and modeling Ethereum transaction records in Sect. [3.3](#oebps-html-619883_1_en_3_chapter-xhtml-sec5). We conduct a micro-level analysis of the Ethereum transaction network in Sect. [3.4](#oebps-html-619883_1_en_3_chapter-xhtml-sec8), and we explain how to use the link prediction evaluation method in Sect. [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-sec11) to study the evolution process. We use the historical records in Sect. [3.6.1](#oebps-html-619883_1_en_3_chapter-xhtml-sec18) to predict the direction of the new transactions. In Sect. [3.7](#oebps-html-619883_1_en_3_chapter-xhtml-sec20), we conclude the chapter and looking to the future.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec2"></a>

## 3.2 Link Prediction Framework

In this section, we explain the concept of using a link prediction framework to investigate the Ethereum transaction relationship, and then outline the key components of the suggested framework.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec3"></a>

### 3.2.1 Link Prediction Based Network Evolution

The goal of link prediction is to estimate the likelihood that disconnected nodes in the network will form edges \[[27](#oebps-html-619883_1_en_3_chapter-xhtml-cr27), [28](#oebps-html-619883_1_en_3_chapter-xhtml-cr28)]. Suppose we have an undirected network \$\$G(V, E)\$$, with the node set *V* and the edge set *E*. After a link prediction method is used, the connection probability between nodes *x* and *y* is valued for each pair of unconnected nodes, and the score value is used to sort all unconnected pairs of nodes. The connections with higher scores are assumed to have a higher probability of new edge occurrence in the future.

We split the collection of observed edges into two halves at random to assess the accuracy of a link prediction system. The first is the training set \$\$E_T\$$, which is used as the known data to determine the score. The other one is the test set \$\$E_P\$$, which is used as the future links to verify whether the links from the test set have a higher score.

We leverage the precision of link prediction to deduce the main drivers of the network evolution by allocating pair scores of link prediction models based on various features of the network evolution. As an illustration, one commonly accepted measure of the structural similarity between two nodes is the number of common neighbors. The Common Neighbor (CN) index concept allows the score of a node pair comprising nodes *x* and *y* to be expressed as

\$$\\displaystyle \\begin{aligned} score^{CN}_{xy}=|Neighbor(x) \\cap Neighbor(y)|. \\end{aligned} $$

(3.1)

Several scoring methods, including the previously described common neighbor method, were used in \[[26](#oebps-html-619883_1_en_3_chapter-xhtml-cr26)] to forecast new-edge appearance in an aviation network. When compared to alternative scoring methods, the common neighbor score-based approach yields the best link prediction accuracy, suggesting that structural elements like the number of common neighbors have a significant impact on how these networks evolve.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec4"></a>

### 3.2.2 Ethereum Transaction Evolution Analysis Framework

In this chapter, we propose a link-prediction based framework to comprehend the evolution of Ethereum transaction relationships. As illustrated in Fig. [3.2](#oebps-html-619883_1_en_3_chapter-xhtml-fig2), we outline the following as the main steps of the proposed framework:<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig2"></a>

***Fig. 3.2***

A link-prediction based framework for analyzing Ethereum transaction relationships

1. 1\.

   **Transaction data acquisition.** We select multiple related transaction subgraphs for additional analysis to examine Ethereum transaction relationships in greater detail and locally. In this instance, we specifically utilize the *K*-order subgraph sampling method that we previously presented \[[5](#oebps-html-619883_1_en_3_chapter-xhtml-cr5)] to acquire several Ethereum transaction micro-structures, or subgraphs, that are centered on multiple chosen addresses.

2. 2\.

   **Network construction and analysis.** We propose to employ *haloed 2-order subgraphs* to extract more complete features for the analysis of the Ethereum transaction relationship. An Ethereum address is represented by each node in the network, and a transaction between addresses is represented by each edge. We examine the structural features of the created haloed subgraph using multiple sophisticated network metrics, which sets the stage for analyzing the network evolution of Ethereum transaction interactions.

3. 3\.

   **Evolution analysis via link prediction.** We extract a set of transaction attributes based on the structural properties of subgraphs and provide related scoring schemes for link prediction studies. Links will be divided into training and test sets for link prediction experiments. Every link in the Ethereum transaction network has a unique timestamp, making it a temporal network. In a network like this, it makes sense to forecast the occurrence of links in the future by utilizing the links that have been in the past. Therefore, in our experiments, the remaining 20% of the prior edges serve as the test samples to assess the algorithm’s efficacy, while the remaining 80% of the edges serve as the training samples to construct a prediction algorithm. The larger the importance of a given aspect in the evolution of Ethereum transaction networks, the higher the accuracy of link prediction when considering that feature.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec5"></a>

## 3.3 Data Preparation for Evolution Analysis

In this section, we explain how we collect the Ethereum transaction records by recursive sampling and how we organize them into structured datasets.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec6"></a>

### 3.3.1 Transaction Data Collection

Blockchain transaction records, or *time-intensive* transaction data, are typically obtained by executing an Ethereum client and synchronizing every block that is connected chronologically. Nevertheless, the local topological structure of transaction data is our focus in this chapter, and block-based data collection is inappropriate in this context. As a result, we recursively gather transaction records layer by layer using multiple addresses as the center addresses, resulting in a hierarchical collection with *K* levels. Such sampled records with connected addresses and local transaction relationships set aside for future research are referred to as *space-intensive* transaction data.

The recursive collection process is as follows:

1. 1\.

   **Initialization step:** Select a center address denoted as \$\$\\mathtt {Addr}^0\$$. Query the transaction records of \$\$\\mathtt {Addr}^0\$$ to obtain trading partners of \$\$\\mathtt {Addr}^0\$$, and name the set of all these partners as \$\$\\mathtt {Addr}^1\$$ which are also regarded as the first layer addresses. The transaction set between the center address \$\$\\mathtt {Addr}^0\$$ and the first layer addresses \$\$\\mathtt {Addr}^1\$$ is denoted as \$\$\\mathtt {Tx}^{0,1}\$$, as shown in Fig. [3.3](#oebps-html-619883_1_en_3_chapter-xhtml-fig3).<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig3"></a>

   ***Fig. 3.3***

   Recursively collected transaction records from Layer 1 to 2

2. 2\.

   **Recursive step:** Query the transaction records of the *n*-th layer addresses in \$\$\\mathtt {Addr}^n\$$ and obtain trading partners as \$\$\\mathtt {Addr}^{n+1}\$$. The set of transaction records between \$\$\\mathtt {Addr}^n\$$ and \$\$\\mathtt {Addr}^{n+1}\$$ is named as \$\$\\mathtt {Tx}^{n,(n+1)}\$$.

3. 3\.

   **Termination:** Stop query until *n* reaches the number of layers *K*, which is a pre-defined parameter.

In this work, we set \$\$K=3\$$. Centered on each randomly selected center address, we collect Ethereum transaction records and involved addresses with three layers. We have hierarchical address sets \$\$\\mathtt {Addr}^0\$$, \$\$\\mathtt {Addr}^1\$$, \$\$\\mathtt {Addr}^2\$$ and \$\$\\mathtt {Addr}^3\$$, and transaction sets \$\$\\mathtt {Tx}^{0,1}\$$, \$\$\\mathtt {Tx}^{1,1}\$$, \$\$\\mathtt {Tx}^{1,2}\$$, \$\$\\mathtt {Tx}^{2,2}\$$, \$\$\\mathtt {Tx}^{2,3}\$$.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec7"></a>

### 3.3.2 Network Construction

As previously discussed, hierarchical transaction records with three layers and a center address are obtained starting from a center address. In this section, we use a three-layer model to represent the gathered local transactions as a *haloed 2-order subgraph* from a network standpoint. Figure [3.4](#oebps-html-619883_1_en_3_chapter-xhtml-fig4) illustrates a 2-order subgraph that is haloed. To build a haloed 2-order subgraph *G*, we first model the address set \$\$\\mathtt {Addr}^{\\mathtt {k}} (k=0,1,2)\$$. Then, we model \$\$\\mathtt {Addr}^3\$$ as \$\$N^{halo}\$$, which is a supplement to the 2-order subgraph, and let \$\$N=\\bigcup _{k=0}^{2} N^k\$$ represent the set of objective nodes. Similarly, we model transaction sets \$\$\\mathtt {Tx}^{a,b}\$$ as edge sets \$\$E^{a,b}\$$, and define edges between *N* as the objective edges *E* (i.e. \$\$E = {E^{0,1}, E^{1,1}, E^{1,2}, E^{2,2}}\$$). In addition, we model \$\$\\mathtt {Tx}^{2,3}\$$ as \$\$E^{halo}\$$, which serves as a supplement to the subgraph.<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig4"></a>

***Fig. 3.4***

*Haloed* 2*-order subgraph*. Nodes in the white background are our research objects, while nodes in the gray circle are to supplement the transaction information of the margin nodes \$\$N^2\$$

To illustrate the need for “halo”, we use the node \$$\\alpha $$ in Fig. [3.4](#oebps-html-619883_1_en_3_chapter-xhtml-fig4) as an example. Located on the edge of the 2-order subgraph centered on \$\$N^0\$$, node \$$\\alpha $$ belongs to \$\$N^2\$$. The degree of \$$\\alpha $$ will be estimated as 2, but is actually 5, if we model the recursively gathered transaction records from Etherscan without \$\$N^{halo}\$$ and \$\$E^{halo}\$$ (i.e., the “halo” of the subgraph). Consequently, the halo layer knowledge helps more fully describe the microscopic structure of node \$$\\alpha $$.

We can extract more detailed properties of collected addresses, like transaction numbers, total transaction value, frequency of transactions, etc., with the addition of \$\$N^{halo}\$$ and \$\$E^{halo}\$$. By simulating a “halo”, one can guarantee the accuracy of margin address data and lessen the bias that comes from random sampling. We first randomly select six center addresses, as indicated in Table [3.1](#oebps-html-619883_1_en_3_chapter-xhtml-tab1). We next model the collected transaction records as *haloed* 2*-order subgraphs G*1–*G*6, with varying sizes. All of the transaction data that was collected will be made available for further research after the chapter is published. <a id="oebps-html-619883_1_en_3_chapter-xhtml-tab1"></a>

***Table 3.1***

Statistics of the constructed *haloed* 2*-order subgraphs*

| Graphs | Addresses of the center node | \$\$\|N\|\$$ | \$\$\|E\|\$$ | \$\$\|N^{halo}\|\$$ | \$\$\|E^{halo}\|\$$ |
| --- | --- | --- | --- | --- | --- |
| *G*1 | 0x4ef42927687b96cffadc1fd1037898a8c3d5d418 | 138 | 260 | 114,475 | 295,358 |
| *G*2 | 0x420415645d9062eb6b9168f03bee92f1b3cf296c | 145 | 384 | 142,722 | 405,144 |
| *G*3 | 0x3ffc9c4df6b29a0c3bf5a3056d37b68288c79a29 | 228 | 615 | 265,791 | 729,533 |
| *G*4 | 0x4a0d27a1044dd871a93275de5109e5f5efc4d46e | 302 | 599 | 207,081 | 673,899 |
| *G*5 | 0x4bb1c210e3921e0f051ed00e898b9605c902114e | 370 | 774 | 319,413 | 797,330 |
| *G*6 | 0x54de06d1a4d9b2bb63d5836ec3159393f860b121 | 2124 | 3377 | 248,243 | 722,556 |

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec8"></a>

## 3.4 Analysis of Microscopic Structural Properties

Based on the aforementioned haloed 2-order subgraphs, we investigate the local structural characteristics of Ethereum transaction relationships in this section. Such a study provides opportunities for network evolution analysis of Ethereum transaction relationships and helps us understand how transactions are distributed and progressively added in Ethereum.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec9"></a>

### 3.4.1 Characterizing Measures of Microscopic Patterns

We take into consideration the following metrics to examine the addition rules and edge distributions in the haloed 2-order subgraphs in order to characterize transaction patterns.

1. 1\.

   The ratio of edge types (\$$\\eta $$): The ratio of each edge type \$\$E^{a,b}\$$ in the edge set *E* is defined as

   \$$\\displaystyle \\begin{aligned} \\eta_{E^{a,b}} = \\frac{|E^{a,b}|}{|E|}, \\end{aligned} $$

   (3.2)

   which can measure the distribution of various types of edges.

2. 2\.

   *Clustering Coefficient* (CC): In the complex network theory, the clustering coefficient is used to characterize the clustering level between nodes in a network, which is defined as

   \$$\\displaystyle \\begin{aligned} \\mathrm{CC}=\\frac{3 \\times T\_{n}}{T_{p}}, \\end{aligned} $$

   (3.3)

   where \$\$T_{n}\$$ denotes the number of closed triangles in the network, and \$\$T_{p}\$$ is the number of connected three-point groups in the network.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec10"></a>

### 3.4.2 Experimental Results and Analysis

We can determine the distribution of various edge types in the Ethereum transaction network and, from there, deduce the shape and organization of Ethereum micro-structures by computing the three indicators mentioned above. The results are given in Tables [3.2](#oebps-html-619883_1_en_3_chapter-xhtml-tab2) and [3.3](#oebps-html-619883_1_en_3_chapter-xhtml-tab3), and the main results are described as follows:

1. 1\.

   It can be seen from Table [3.2](#oebps-html-619883_1_en_3_chapter-xhtml-tab2) that among the collected haloed 2-order subgraphs, \$\$\\eta _{E^{1,2}}\$$ is the highest, whereas \$\$\\eta _{E^{1,1}}\$$ and \$\$\\eta _{E^{2,2}}\$$ are incredibly low. According to this conclusion, few transactions occur between addresses in the same layer, and the majority of transactions are associated with \$\$\\mathtt {Tx}^{1,2}\$$ (transactions between the first and second layers). <a id="oebps-html-619883_1_en_3_chapter-xhtml-tab2"></a>

   ***Table 3.2***

   Proportion of different types of edges in the edge set *E*

   | Graphs | \$\$\\eta _{E^{0,1}}\$$ | \$\$\\eta _{E^{1,2}}\$$ | \$\$\\eta _{E^{1,1}}\$$ | \$\$\\eta _{E^{2,2}}\$$ |
   | --- | --- | --- | --- | --- |
   | *G*1 | 58/260 | **200/260** | 2/260 | 0/260 |
   | *G*2 | 64/384 | **318/384** | 2/384 | 0/384 |
   | *G*3 | 20/615 | **589/615** | 6/615 | 0/615 |
   | *G*4 | 142/599 | **456/599** | 1/599 | 0/599 |
   | *G*5 | 38/774 | **736/774** | 0/774 | 0/774 |
   | *G*6 | 80/3377 | **3296/3377** | 1/3377 | 10/3377 |

   The best results are marked in bold

   <a id="oebps-html-619883_1_en_3_chapter-xhtml-tab3"></a>

   ***Table 3.3***

   Clustering coefficient of different undirected Ethereum transaction subgraphs

   | Graphs | *G*1 | *G*2 | *G*3 | *G*4 | *G*5 | *G*6 |
   | --- | --- | --- | --- | --- | --- | --- |
   | *CC* | 0.01 | 0.012 | 0.064 | 0 | 0 | 0 |

2. 2\.

   There are not many closed triangles in the Ethereum transaction relationships, as evidenced by the low clustering coefficients displayed in Table [3.3](#oebps-html-619883_1_en_3_chapter-xhtml-tab3). It is unlikely that addresses with similar trading partners will transact in the future. The microstructure of Ethereum transaction networks is star-like, as this research indirectly demonstrates.

We can deduce from the results of these trials that transactions between addresses in the same layer are rare. Additionally, the Ethereum transaction network has a low clustering coefficient, which means that the local structure is star-shaped because an address’s partners do not transact with one another on Ethereum. However, it is implied that Ethereum transaction networks are not small-world networks by the low clustering coefficient.

Since transaction events are more frequent between first- and second-layer addresses, in our next study on network evolution, we concentrate on the newly formed edges between \$\$N^1\$$ and \$\$N^2\$$.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec11"></a>

## 3.5 Evolution Factors of Ethereum Transaction Networks

To design the scoring system based on these attributes, we first extract topological features from the transaction networks in this section. Next, we use a link prediction model linked to several scoring methods to measure the impact of various evolution parameters. The progress of the Ethereum transaction network’s fitness is reflected in the performance of link prediction models.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec12"></a>

### 3.5.1 Training/Test Set Split

To assess the performance of various models, networks are split into training and test sets for the link prediction problem. Edges in the Ethereum transaction network scenario are connected by timestamps. Since it is impossible to predict links based on unseen transactions, it is crucial that we segregate edges with earlier timestamps into the training set and leave the others with later timestamps in the test set. Therefore, we first sort all of the edges in the generated haloed 2-order subgraphs in ascending order of time, dividing the last 20% of the edges with a larger timestamp into the test set \$\$E_P\$$ and the preceding 80% of the edges with a smaller timestamp into the training set \$\$E_T\$$.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec13"></a>

### 3.5.2 Feature Extraction

To explore which factors affect the evolution of Ethereum transaction networks, we extracted two various types of network features, which are node features (*NF*) and edge features (*EF*).

The node feature value of node *i* is represented by \$\$NF(i)\$$ in a given haloed 2-order subgraph *G*.

We extract the node features (*NF*) for addresses as follows:

1. 1\.

   **Transaction frequency** (*TxFreq*): The number of transactions of nodes occurred per unit time;

2. 2\.

   **Total transaction amount** (*TxSum*): The sum of the *Ether* amount of the address’s income and expenditure.

Additionally, we denote \$\$EF(i,j)\$$ to represent the edge feature (*EF*) value of the edge connecting node *i* and *j*. We extract the edge feature (*EF*) for linked address pairs described below:

**Number of Transactions (*****TxNum*****)**

The number of transactions between node *i* and *j*.

Notably, with the supplement information of “halo”, \$\$N^{halo}\$$ and \$\$E^{halo}\$$, the node features and edge features of nodes in \$\$N^2\$$ can be calculated accurately.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec14"></a>

### 3.5.3 Scoring Methods for Unconnected Node Pairs

According to the experimental results in Sect. [3.4.2](#oebps-html-619883_1_en_3_chapter-xhtml-sec10), the newly added edges of a haloed 2-order subgraph typically occur between the first-order neighbor \$\$N^1\$$ and the second-order neighbor \$\$N^2\$$. Therefore, we primarily concentrate on the edges that join \$\$N^1\$$ and \$\$N^2\$$ in this section.

For each unknown relationship between \$\$N^1\$$ and \$\$N^2\$$, we assign distinct scores to indicate the likelihood of the real connection. A link prediction model, which is a numerical assessment of the corresponding network evolution model, correlates with each scoring method. We believe that node pairs with higher scores *S* will eventually have more links.

1. 1\.

   A scoring method depending on the endpoint on either the first or second layer:

   Consider an edge \$\$e_{ij}\$$ connecting nodes *i* and *j*, which belong to the first and second layers, respectively, i.e. \$\$i\\in N^1, j\\in N^2\$$. We first design a scoring criterion of \$\$e_{ij}\$$, denoted as \$\$S^{N^1}_{ij}\$$, based on node features of its endpoint on the first layers: <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ4"></a>

   \$$\\displaystyle \\begin{aligned} \\begin{aligned} S^{N^1}_{ij}=&amp;amp;\\lambda \\frac{\~NF(i)\~}{\~\\max \\{NF(p), p\\in N^1\\}\~}+\\\\ &amp;amp;(1-\\lambda)\\left(1-\\frac{\~NF(i)\~}{\~\\max \\{NF(p), p\\in N^1\\}~}\\right), \\end{aligned} {} \\end{aligned} $$

   (3.4)

   where \$\$\\lambda = 0\$$ or 1, *NF* can be *TxFreq* and *TxSum*, and *i* is the node feature. The method of new relationships introduced to the Ethereum transaction network is indicated by the scoring criterion. When \$\$\\lambda =1\$$, links with higher *NF* values at their endpoints receive better scores. Conversely, when \$\$\\lambda =0\$$, links with lower *NF* values at their endpoints receive higher scores. As an illustration, if the link prediction model with \$\$S^{N^1}_{ij}\$$, where \$\$NF=TxFreq\$$ and \$\$\\lambda =1\$$, performs better than models with alternative parameters, we can draw the conclusion that first-layer nodes that have historically seen higher transaction frequencies would likely have more transactions in the future.

   Similarly, we design a scoring criterion based on node features of its endpoint on the second layers, i.e. <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ5"></a>

   \$$\\displaystyle \\begin{aligned} \\begin{aligned} S^{N^2}_{ij}=&amp;amp;\\lambda \\frac{\~NF(j)\~}{\~\\max \\{NF(p), p\\in N^2\\}\~}+\\\\ &amp;amp;(1-\\lambda)\\left(1-\\frac{\~NF(j)\~}{\~\\max \\{NF(p), p\\in N^2\\}~}\\right). \\end{aligned} {} \\end{aligned} $$

   (3.5)

   We can determine which layer of nodes plays a critical role in the network evolution by comparing the link prediction model based on scoring methods \$\$S^{N^1}_{ij}\$$ and \$\$S^{N^2}_{ij}\$$, using the same \$$\\lambda $$ and *NF*.

2. 2\.

   A scoring method depending on both endpoints:

   Here, we examine a score method of an edge \$\$e_{ij}\$$ based on the previously described approach, taking into account simultaneously the node features of both endpoints from the first and second layers. According to the scoring methods \$\$S^{N^1}_{ij}\$$ using ([3.4](#oebps-html-619883_1_en_3_chapter-xhtml-equ4)) and \$\$S^{N^2}_{ij}\$$ using ([3.5](#oebps-html-619883_1_en_3_chapter-xhtml-equ5)), we design the scoring methods as <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ6"></a>

   \$$\\displaystyle \\begin{aligned} S^{N^1N^2}\_{ij}=S^{N^1}\_{ij}+S^{N^2}_{ij}, {} \\end{aligned} $$

   (3.6)

   where the setting of \$$\\lambda $$ can be different in \$\$S^{N^1}_{ij}\$$ and \$\$S^{N^2}_{ij}\$$, i.e. let \$\$\\lambda =\\lambda _1\$$ in \$\$S^{N^1}_{ij}\$$ and \$\$\\lambda =\\lambda _2\$$ in \$\$S^{N^2}_{ij}\$$. For instance, if we take into account the evolution mechanism that first-layer nodes with higher transaction frequency (*TxFreq*) and second-layer nodes with lower transaction frequency are more likely to have new transactions, parameters in score index \$\$S^{N^1N^2}\$$ ([3.6](#oebps-html-619883_1_en_3_chapter-xhtml-equ6)) can be set as \$\$NF=TxFreq\$$; \$\$\\lambda _1=1\$$ in \$\$S^{N^1}_{ij}\$$ and \$\$\\lambda _2=0\$$ in \$\$S^{N^2}_{ij}\$$.

3. 3\.

   A scoring method depending on the edge itself:

   Different from the scoring method \$\$S^{N^1N^2}_{ij}\$$ which depends on node features of endpoints, here the edge feature *EF* is used as the scoring criterion to calculate the score of links. We design the edge-feature based scoring method as <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ7"></a>

   \$$\\displaystyle \\begin{aligned} \\begin{aligned} S^E_{ij} = &amp;amp;\\lambda \\frac{\~EF(i,j)\~}{\~\\max \\{EF(e), e\\in E^{1,2}\\}\~}+\\\\ &amp;amp;(1-\\lambda) \\left( 1-\\frac{\~EF(i,j)\~}{\~\\max \\{EF(e), e\\in E^{1,2}\\}~}\\right), \\end{aligned} {} \\end{aligned} $$

   (3.7)

   where \$\$EF(i,j)\$$ represents the edge feature value of edge connecting node *i* and *j*, and we assign the edge feature *EF* as *TxNum*, i.e. the transaction number of edge between node *i* and *j*. With \$\$\\lambda =1\$$, edges with higher *EF* value receive higher scores, whereas with \$\$\\lambda =0\$$, edges with lower *EF* value receive higher scores. If there are no transactions between node *i* and *j* in the past, we have \$\$S^E_{ij}=0\$$.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec15"></a>

### 3.5.4 Evaluation Index of Link Prediction

In a given haloed 2-order subgraph, we first compute the score \$\$S_{ij}\$$ for each node pair \$\$(i,j)\$$ where \$\$i\\in N^1, j\\in N^2\$$, i.e. there are \$\$|N^1||N^2|\$$ links assigned scores based on a particular criterion. Next, we choose the top-*L* connections to be predicted links by sorting the links in descending order according to the assigned scores. Using the link prediction model task, we assess the network evolution mechanism’s performance using \$\$Precision@L\$$, or the percentage of accurate unknown edges among the edges whose scores are in the top *L*. If there are *m* edges which are in the test set \$\$E^P\$$ among the top *L* edges, \$\$Precision@L\$$ is defined as

\$$\\displaystyle \\begin{aligned} {} Precision@L = \\frac{m}{L}, \\end{aligned} $$

(3.8)

where *m* represents the number of edges that are predicted accurately. A larger *Precision* indicates a more accurate prediction model, because it prefers to assign higher scores to those missing links in the test set.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec16"></a>

### 3.5.5 Prediction Results and Analysis

Firstly, we investigate the effect of a single node feature on newly linked edges from two aspects, based on the scoring method with ([3.4](#oebps-html-619883_1_en_3_chapter-xhtml-equ4)) and ([3.5](#oebps-html-619883_1_en_3_chapter-xhtml-equ5)) depending on the endpoint on either the first or second layer. The six haloed 2-order subgraphs’ experimental outcomes are displayed in Fig. [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-fig5).

1. 1\.

   Compare the effects of various node attributes horizontally with varying \$$\\lambda $$. In detail, \$\$\\lambda =1\$$ typically performs better than \$\$\\lambda =0\$$ in most cases. The experimental result in Fig. [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-fig5) demonstrates that scoring methods with *TxFreq* outperform those with *TxSum* in graphs *G*1–*G*6, except *G*3 when \$\$L=20\$$. These show that the transaction frequency (*TxFreq*) has a greater influence than transaction amount (*TxSum*) on a new edge occurring in Ethereum transaction networks, and in most cases, a higher transaction frequency corresponds to a higher probability of generating new transaction relationships.<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig5"></a>

   ***Fig. 3.5***

   \$\$Precision@L\$$ of haloed 2-order subgraphs \$\$G1\\text{--}G6\$$ using a single node feature with ([3.4](#oebps-html-619883_1_en_3_chapter-xhtml-equ4)) and ([3.5](#oebps-html-619883_1_en_3_chapter-xhtml-equ5)) as the scoring criterion to calculate the unknown links. \$\$L=20, 50, 100, 150, 200, 250, 300\$$, \$\$\\lambda =0,1\$$

2. 2\.

   In haloed 2-order subgraphs, compare vertically the value of the same node feature with several layer nodes \$\$N^i\$$. Except for *G*2, the experimental result in Fig. [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-fig5) demonstrates that, when \$\$\\lambda =1\$$, the scoring method based on first-layer nodes outperforms that based on second-layer nodes. The outcome shows that the network evolution mechanism of Ethereum transaction relationships is dominated by endpoints on \$\$N^1\$$. In addition, there is a greater chance that the nodes of \$\$N^1\$$ with higher transaction frequencies will conduct new transactions in the future.

Secondly, we utilize the scoring method \$\$S^{N^1N^2}\$$ ([3.6](#oebps-html-619883_1_en_3_chapter-xhtml-equ6)) to compute the unknown edges’ score based on the node features of both \$\$N^1\$$. It can be seen from Fig. [3.6](#oebps-html-619883_1_en_3_chapter-xhtml-fig6) that:

1. 1\.

   Taking into account the influence of various node features *NF*, we discover that the transaction frequency scoring method (\$\$NF=TxFreq\$$) typically performs better than the transaction amount scoring method (\$\$NF=TxSum\$$). These findings are in line with prior scoring method outcomes that vary based on the endpoint on either the first or second layer ([3.4](#oebps-html-619883_1_en_3_chapter-xhtml-equ4) and ([3.5](#oebps-html-619883_1_en_3_chapter-xhtml-equ5)).<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig6"></a>

   ***Fig. 3.6***

   \$\$Precision@L\$$ of *G*1–*G*6 using a pair of node feature with ([3.6](#oebps-html-619883_1_en_3_chapter-xhtml-equ6)) as the scoring criterion to calculate the unknown links. \$\$L=20, 50, 100, 150, 200, 250, 300\$$, \$\$\\lambda _1=0,1\$$, \$\$\\lambda _2=0,1\$$

2. 2\.

   It demonstrates competitive performance in *G*1, *G*3, *G*5, and *G*6 when the transaction frequency (*TxFreq*) is chosen as the scoring criterion and \$\$\\lambda _1=1\$$ in \$\$S^{N^1}\$$ and \$\$\\lambda _2=0\$$ in \$\$S^{N^2}\$$ are specified. This suggests that there is a greater likelihood of links in the local structures between the first-order neighbor \$\$N^1\$$, which has a higher transaction frequency, and the second-order neighbor \$\$N^2\$$, which has a lower transaction frequency.

Thirdly, we investigate whether the number of past transactions will impact the development of the Ethereum transaction network using the scoring method \$\$S^E\$$ ([3.7](#oebps-html-619883_1_en_3_chapter-xhtml-equ7)), \$\$EF=TxNum\$$. As can be shown in Fig. [3.7](#oebps-html-619883_1_en_3_chapter-xhtml-fig7), scoring with \$\$\\lambda =1\$$ performs significantly better competitively than scoring with \$\$\\lambda =0\$$. With \$\$\\lambda =1\$$ and \$\$L=50\$$, the precision of link prediction is greater than 0.1, except for *G*4. We infer that there is a greater chance of a reconnect between node pairs with a higher number of transactions (*TxNum*). Stated differently, addresses with a high volume of transactions have a high probability of experiencing fresh transactions in the future.<a id="oebps-html-619883_1_en_3_chapter-xhtml-fig7"></a>

***Fig. 3.7***

\$\$Precision@L\$$ of *G*1–*G*6 using the edge feature of *TxNum* with ([3.7](#oebps-html-619883_1_en_3_chapter-xhtml-equ7)) as the scoring criterion to calculate the unknown links. \$\$L=20, 50, 100, 150, 200,\$$ \$\$250, 300\$$

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec17"></a>

## 3.6 Estimation of the Direction of New Transaction Relationships

Although there are directions to the transaction interactions in reality, we have examined the evolution of Ethereum transactions thus far from the perspective of an undirected network. To be more precise, with Ethereum, sending *Ether* to another address indicates withdrawal activity, whereas receiving *Ether* at an ordinary address indicates coin deposit behavior. Therefore, estimating the directions of new transactions is crucial.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec18"></a>

### 3.6.1 Direction Estimation of New Edges by Node Degree

First, we postulate that the preference of past transactions determines the future direction of links. Drawing on the past transaction records, we estimate whether the address is more likely to transmit or receive *Ether*. Here, we continue to concentrate on the direction estimate of edges between the first and second layer nodes, or \$\$E^{1,2}\$$, since the new connections of a haloed 2-order subgraph *G* typically occur between \$\$N^1\$$ and \$\$N^2\$$.

Given a haloed 2-order graph, considering node pair \$\$(i,j)\$$ between node *i* and *j* which are from the first and second layers, i.e. \$\$i \\in N^1\$$, \$\$j\\in N^2\$$, we estimate the direction of node pair \$\$(i,j)\$$ using the following methods.

1. 1\.

   An estimating method based on the degree of first layer nodes:

   First, we compute the value of an indicator \$\$D_{ij}^{N^1}\$$ of a node pair \$\$(i,j)\$$, which is defined as

   \$$\\displaystyle \\begin{aligned} {} D_{ij}^{N^1} = sgn(outdegree(i) - indegree(i)), \\end{aligned} $$

   (3.9)

   where \$\$outdegree(i)\$$ and \$\$indegree(i)\$$ represent the out-degree and in-degree of node *i*, respectively, and \$\$sgn(\\cdot )\$$ is the sign function that indicates the positivity of a variable. Then, we predict the direction of node pair \$\$(i,j)\$$ using the following rules: <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ10"></a>

   \$$\\displaystyle \\begin{aligned} {} \\left\\{ \\begin{array}{lcl} D\_{ij}^{N^1}=1 &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j}\\\\ D\_{ij}^{N^1}=-1 &amp;amp; \\Rightarrow &amp;amp; {i \\leftarrow j}\\\\ D_{ij}^{N^1}=0 &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j \~\\mathrm{or}~ i \\leftarrow j} \\end{array} \\right . \\end{aligned} $$

   (3.10)

   For instance, if \$\$D_{ij}^{N^1}=1\$$, the out-degree value of node *i* is greater than the in-degree value, indicating that there are more sending behaviors than receiving behaviors of node *i*. Therefore, it is comprehensive to predict node *i* to be a sender (i.e. \$\$i \\rightarrow j\$$) in the future if \$\$D_{ij}^{N^1}=1\$$, and predict *i* to be a receiver if \$\$D_{ij}^{N^1}=-1\$$. Otherwise, there is a fifty-fifty chance of predicting *i* to be the sender or receiver if \$\$D_{ij}^{N^1}=0\$$.

   After that, we compute the precision of the edge direction estimation by

   \$$\\displaystyle \\begin{aligned} Precision\_{D^{N^1}}=\\frac{|E_{D^{N^1}}|}{|E_P|}, \\end{aligned} $$

   (3.11)

   where \$\$E_{D^{N^1}}\$$ denotes the edges whose direction is predicted accurately based on the indicator \$\$D^{N^1}\$$, and \$\$|E_P|\$$ is the number of edges in the test set \$\$E_P\$$.

2. 2\.

   An estimating method based on the degree of second layer nodes:

   Similar to the previous method, we can estimate the direction of a node pair \$\$(i,j)\$$ by an indicator \$\$D_{ij}^{N^2}\$$, which is defined as

   \$$\\displaystyle \\begin{aligned} {} D_{ij}^{N^2} = sgn(outdegree(j) - indegree(j)), \\end{aligned} $$

   (3.12)

   where \$\$i \\in N^1\$$, \$\$j\\in N^2\$$. After computing \$\$D_{ij}^{N^2}\$$, we utilize the following rules to predict the direction of a node pair \$\$(i,j)\$$: <a id="oebps-html-619883_1_en_3_chapter-xhtml-equ13"></a>

   \$$\\displaystyle \\begin{aligned} {} \\left\\{ \\begin{array}{lcl} D\_{ij}^{N^2}=1 &amp;amp; \\Rightarrow &amp;amp; {i \\leftarrow j}\\\\ D\_{ij}^{N^2}=-1 &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j}\\\\ D_{ij}^{N^2}=0 &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j \~\\mathrm{or}~ i \\leftarrow j} \\end{array} \\right . \\end{aligned} $$

   (3.13)

   Similarly, we evaluate the performance of the edge direction estimation by

   \$$\\displaystyle \\begin{aligned} Precision\_{D^{N^2}}=\\frac{|E_{D^{N^2}}|}{|E_P|}, \\end{aligned} $$

   (3.14)

   where \$\$E_{D^{N^2}}\$$ represents the edges whose direction prediction is true based on the indicator \$\$D^{N^2}\$$.

3. 3\.

   An estimating method based on the degree of first and second layer nodes:

   Using the past transaction records of the nodes in the first or second layer, respectively, we have estimated the direction of future transactions. As in Sect. [3.5.3](#oebps-html-619883_1_en_3_chapter-xhtml-sec14)b, there exists a scenario in which both of them are taken into consideration simultaneously After computing \$\$D^{N^1}\$$ and \$\$D^{N^2}\$$ with ([3.10](#oebps-html-619883_1_en_3_chapter-xhtml-equ10)) and ([3.13](#oebps-html-619883_1_en_3_chapter-xhtml-equ13)), we predict the direction of a node pair \$\$(i,j)\$$ according to the rules:

   \$$\\displaystyle \\begin{aligned} {} (D\_{ij}^{N^1},D_{ij}^{N^2})= \\left\\{ \\begin{array}{lcl} (1,-1) &amp;amp; \\Rightarrow &amp;amp; {i \\leftarrow j}\\\\ (-1,1) &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j}\\\\ (1,1) &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j \~\\mathrm{and}~ i \\leftarrow j} \\\\ (-1,-1) &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j \~\\mathrm{and}~ i \\leftarrow j} \\\\ otherwise &amp;amp; \\Rightarrow &amp;amp; {i \\rightarrow j \~\\mathrm{or}~ i \\leftarrow j} \\end{array} \\right . \\end{aligned} $$

   (3.15)

   Similarly, we evaluate the performance of the edge direction estimation by

   \$$\\displaystyle \\begin{aligned} Precision\_{(D^{N^1},D^{N^2})}=\\frac{|E_{(D^{N^1},D^{N^2})}|}{|E_P|}, \\end{aligned} $$

   (3.16)

   where \$\$E_{(D^{N^1},D^{N^2})}\$$ denotes the edges whose direction prediction is true based on the indicator \$\$(D^{N^1},D^{N^2})\$$, and \$\$|E_P|\$$ is the number of edges in test set \$\$E_P\$$.

Comparing the results of \$\$Precision_{D^{N^1}}\$$ and \$\$Precision_{D^{N^2}}\$$, we discover that in most cases, estimating methods with \$\$D^{N^2}\$$ get higher precision than the methods with \$\$D^{N^1}\$$ except for *G*4. Additionally, the value of \$\$Precision_{D^{N^2}}\$$ of other subgraphs is greater than 50% except for *G*4. Considering the situation of both layers, we discover that \$\$Precision_{(D^{N^1},D^{N^2})}\$$ achieves the best result among the six subgraphs. The findings show a relationship between the degree feature of the addresses and the direction of the new transaction. In the microscopic structures, it has a closer relationship with both the first-order \$\$N^1\$$ and second-order neighbor \$\$N^2\$$. More than 70% of directed edges in the test set may be predicted with accuracy. This suggests that the node degree feature is a useful tool for determining transaction direction. Moreover, it suggests that certain node pairs in the recently added linking edges have two-way edges, meaning that certain Ethereum accounts can be both sender and recipient of ether.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec19"></a>

### 3.6.2 Direction Estimation of New Edge by the Historical Direction

In this part, we examine whether a subsequent trade between those node pairs that completed transactions in \$\$E_T\$$ will result in a change in their direction. We determine the ratio of new transactions that follow the definition of the historical direction of all new transactions,

\$$\\displaystyle \\begin{aligned} Ratio\_{sameDir}=\\frac{|E\_{P,D(E_T)}|}{|E_{P,T}|}, \\end{aligned} $$

(3.17)

where \$\$E_{P,D(E_T)}\$$ denotes the edges in \$\$E_P\$$ whose direction is the same as it in \$\$E_T\$$, and \$\$E_{P,T}\$$ denotes the edges in \$\$E_P\$$ that also exist in \$\$E_T\$$. Notably, the direction of a node pair in \$\$E_T\$$ or \$\$E_P\$$ is the major direction among the corresponding edge set. For instance, a node pair \$\$(u, v)\$$’s direction of \$\$E_T\$$ is set to \$\$u\\rightarrow v\$$ if there are more transactions transformed *Ether* from *u* to *v* in \$\$E_T\$$, otherwise the direction is set to \$\$u \\leftarrow v\$$. Table [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-tab5) displays the \$\$Ratio_{sameDir}\$$ values of the six subgraphs in the Ethereum transaction network. We discover that the \$\$Ratio_{sameDir}\$$ values of \$\$G1, G2, G3, G5, G6\$$, with the exception of *G*4, are greater than 70%. These results show that the transaction direction of addresses that have historically traded tends to match that of those transactions when they trade again.

From the results of estimating the direction of new transaction relationships, we find that *G*4 shows a different result from \$\$G1, G2, G3, G5, G6\$$. From Table [3.4](#oebps-html-619883_1_en_3_chapter-xhtml-tab4), we discover that the edge direction estimation in *G*4 has a stronger relationship with the first-order neighbor \$\$N^1\$$ in the microscopic structure. Table [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-tab5) shows that *G*4 has \$\$|E_{P,D(E_P)}|\$$ substantially less than other subgraphs. Therefore, we compute the repetition ratio as

\$$\\displaystyle \\begin{aligned} Ratio\_{samePair}=\\frac{|E_{P,T}|}{|E_P|}, \\end{aligned} $$

(3.18)

where \$\$E_{P,T}\$$ represents the edges in \$\$E_P\$$ that also exist in \$\$E_T\$$. Table [3.6](#oebps-html-619883_1_en_3_chapter-xhtml-tab6) shows that *G*4 has a repetition ratio of only 0.03, which is significantly less than that of other subgraphs. <a id="oebps-html-619883_1_en_3_chapter-xhtml-tab4"></a>

***Table 3.4***

The precision of direction estimation of new connections between based on estimating methods with \$\$D^{N^1}\$$, \$\$D^{N^2}\$$ and \$\$(D^{N^1},D^{N^2})\$$

| Graphs | \$\$Precision_{D^{N^1}}\$$ | \$\$Precision_{D^{N^2}}\$$ | \$\$Precision_{(D^{N^1},D^{N^2})}\$$ |
| --- | --- | --- | --- |
| *G*1 | 0.40 (21/52) | 0.62 (32/52) | **0.79 (41/52)** |
| *G*2 | 0.54 (42/77) | 0.90 (69/77) | **0.94 (73/77)** |
| *G*3 | 0.53 (66/123) | 0.67 (83/123) | **0.87 (107/123)** |
| *G*4 | 0.64 (76/119) | 0.33 (39/119) | **0.81 (96/119)** |
| *G*5 | 0.57 (88/155) | 0.65 (100/155) | **0.75 (117/155)** |
| *G*6 | 0.50 (344/676) | 0.59 (396/676) | **0.73 (496/676)** |

The best results are marked in bold

<a id="oebps-html-619883_1_en_3_chapter-xhtml-tab5"></a>

***Table 3.5***

The ratio of new transactions with the same direction as the historical transaction direction of six subgraphs in Ethereum transaction network

| Graphs | \$\$Ratio_{sameDir}\$$ |
| --- | --- |
| *G*1 | **0.94 (15/16)** |
| *G*2 | **1.00 (54/54)** |
| *G*3 | **0.80 (40/50)** |
| *G*4 | 0.25 (1/4) |
| *G*5 | **0.73 (36/49)** |
| *G*6 | **0.95 (148/156)** |

All results, except for the one with the lowest repetition ratio, are in bold

<a id="oebps-html-619883_1_en_3_chapter-xhtml-tab6"></a>

***Table 3.6***

The repetition ratio of new transactions with the same address pairs of six subgraphs in Ethereum transaction network

| Graphs | \$\$Ratio_{samePair}\$$ |
| --- | --- |
| *G*1 | **0.31 (16/52)** |
| *G*2 | **0.70 (54/77)** |
| *G*3 | **0.41 (50/123)** |
| *G*4 | 0.03 (4/119) |
| *G*5 | **0.12 (49/155)** |
| *G*6 | **0.23 (156/676)** |

All results, except for the one with the lowest repetition ratio, are in bold

<a id="oebps-html-619883_1_en_3_chapter-xhtml-sec20"></a>

## 3.7 Conclusion

In this chapter, we construct and analyze the haloed 2-order subgraphs, explore the trading relationships of Ethereum, and the evaluation metrics of link prediction, and quantify the impact of different network features on the evolution mechanism of Ethereum trading network. The experimental results show that the Ethereum transaction network exhibits a star-like local topology. Transaction frequency has a greater impact on the network evolution, and Ethereum addresses that have had multiple transactions in the past are likely to be transacted again in the future.

In the realm of cryptocurrencies, the trust level or evaluations that users provide to one another following a transaction are represented by the link between addresses. Therefore, similar to the earlier study \[[29](#oebps-html-619883_1_en_3_chapter-xhtml-cr29)], a potential usage of link prediction can be utilized to anticipate whether a bitcoin transaction relationship will arise between the users.

The current work still has several limitations. Future works:

1. 1\.

   Potential application:

   In this chapter, link prediction aids in the understanding of the Ethereum transaction network’s evolution. Additional insightful research has been done on the use of link prediction in transaction networks. Ethereum has seen many illicit activities and frauds, including money laundering, Ponzi schemes, and phishing. Link prediction has the potential to improve Ethereum transaction tracking and enable real-time tracking of *Ether* flow. Furthermore, the link prediction in Lightning Network has a few possible uses. Both parties must reserve high-security deposits in the payment channel for big Lightning Network transactions, and additional route nodes might need to be set up for route payments.

2. 2\.

   Internal transaction and token transfer:

   An essential component of the Ethereum ecosystem is the smart contract. On Ethereum, smart contracts are used by more than 100,000 different cryptocurrency types \[[30](#oebps-html-619883_1_en_3_chapter-xhtml-cr30)]. In the Ethereum evolution processes, it is worthwhile to take a closer look at the internal transactions sent by smart contract accounts. Tokens on Ethereum, for instance, exhibit inconsistent behaviors that are automatically detected by studies such as TokenScope \[[31](#oebps-html-619883_1_en_3_chapter-xhtml-cr31)] and the evolution of the token transfer network.

3. 3\.

   Label effect of center addresses:

   It is worth exploring the microstructure centered on the different addresses. Based on the labels provided by Etherscan, we find that the address centered at *G*4 is unlabeled, while the addresses centered at \$\$G1, G2, G3, G5, G6\$$ are labeled as “Phish/Hack”. Further data collection and experiments are needed to reveal whether the local structure of “Phish/Hack” addresses will exhibit different network characteristics from other unlabeled addresses. For example, from Table [3.5](#oebps-html-619883_1_en_3_chapter-xhtml-tab5), we can infer that “Phish/Hack” addresses may tend to trade with addresses that have already been traded and the direction stays the same, while unlabeled addresses may tend to trade more with new addresses.

We expect that further work in the future will be inspired by our work on Ethereum transaction evolution mechanisms.

<a id="oebps-html-619883_1_en_3_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr1"></a>Chen, T., Zhu, Y., Li, Z., Chen, J., Li, X., Luo, X., Lin, X., Zhange, X.: Understanding ethereum via graph analysis. In: Proc. IEEE INFOCOM, pp. 1484–1492 (2018)
2. 2.Liang, J., Li, L., Zeng, D.: Evolutionary dynamics of cryptocurrency transaction networks: an empirical study. PLoS One **13**(8), 1–18 (2018)[Crossref](https://doi.org/10.1371/journal.pone.0202202)
3. 3.Ferretti, S., D’Angelo, G.: On the ethereum blockchain structure: a complex networks theory perspective. Concurr. Comput. **32**(12), e5493 (2019)[Crossref](https://doi.org/10.1002/cpe.5493)
4. 4.Guo, D., Dong, J., Wang, K.: Graph structure and statistical properties of ethereum transaction relationships. Inf. Sci. **492**, 58–71 (2019)[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3938856)[Crossref](https://doi.org/10.1016/j.ins.2019.04.013)
5. 5\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr5"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. II Express Briefs **67**(11), 2737–2741 (2020)
6. 6\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr6"></a>Wood, G.: Ethereum: a secure decentralised generalised transaction ledger. Ethereum Project Yellow Pap. **151**, 1–32 (2014)
7. 7\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr7"></a>Liu, X., Muhammad, K., Lloret, J., Chen, Y.-W., Yuan, S.-M.: Elastic and cost-effective data carrier architecture for smart contract in blockchain. Future Gener. Comput. Syst. **100**, 590–599 (2019)[Crossref](https://doi.org/10.1016/j.future.2019.05.042)
8. 8.Wang, Y., Bracciali, A., Li, T., Li, F., Cui, X., Zhao, M.: Randomness invalidates criminal smart contracts. Inf. Sci. **477**, 291–301 (2019)[Crossref](https://doi.org/10.1016/j.ins.2018.10.057)
9. 9.Zhang, L., Wang, Y., Li, F., Hu, Y., Au, M.H.: A game-theoretic method based on q-learning to invalidate criminal smart contracts. Inf. Sci. **498**, 144–153 (2019)[Crossref](https://doi.org/10.1016/j.ins.2019.05.061)
10. 10.Ren, W., Hu, J., Zhu, T., Ren, Y., Choo, K.-K.R.: A flexible method to defend against computationally resourceful miners in blockchain proof of work. Inf. Sci. **507**, 161–171 (2020)[Crossref](https://doi.org/10.1016/j.ins.2019.08.031)
11. 11\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr11"></a>Shao, W., Wang, Z., Wang, X., Qiu, K., Jia, C., Jiang, C.: Lsc: Online auto-update smart contracts for fortifying blockchain-based log systems. Inf. Sci. **512**, 506–517 (2020)[Crossref](https://doi.org/10.1016/j.ins.2019.09.073)
12. 12\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr12"></a>Zheng, Z., Xie, S., Dai, H.-N., Chen, W., Chen, X., Weng, J., Imran, M.: An overview on smart contracts: challenges, advances and platforms. Future Gener. Comput. Syst. **105**, 475–491 (2020)[Crossref](https://doi.org/10.1016/j.future.2019.12.019)
13. 13\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr13"></a>Xie, S., Zheng, Z., Chen, W., Wu, J., Dai, H.-N., Imran, M.: Blockchain for cloud exchange: a survey. Comput. Electr. Eng. **81**, 106526 (2020)[Crossref](https://doi.org/10.1016/j.compeleceng.2019.106526)
14. 14\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr14"></a>Han, Q., Wu, J., Zheng, Z.: Long-range dependence, multi-fractality and volume-return causality of ether market. Chaos **30**(1), 011101 (2020)[Crossref](https://doi.org/10.1063/1.5135739)
15. 15\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr15"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: T-EDGE: temporal weighted multidigraph embedding for ethereum transaction network analysis. Front. Phys. **8**(204), 1–9 (2020)
16. 16\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr16"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. (2020). [https://doi.org/10.1109/TSMC.2020.3016821](https://doi.org/10.1109/TSMC.2020.3016821)
17. 17\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr17"></a>Bartoletti, M., Carta, S., Cimoli, T., Saia, R.: Dissecting ponzi schemes on ethereum: identification, analysis, and impact. Future Gener. Comput. Syst. **102**, 259–277 (2020)[Crossref](https://doi.org/10.1016/j.future.2019.08.014)
18. 18\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr18"></a>Huang, Y., Wang, H., Wu, L., Tyson, G., Luo, X., Zhang, R., Liu, X., Huang, G., Jiang, X.: Understanding (mis)behavior on the EOSIO blockchain. In: Proc. ACM Meas. Anal. Comput. Syst., vol. 4, no. 2, pp. 1–28 (2020)
19. 19\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr19"></a>Zheng, P., Zheng, Z., Wu, J., Dai, H.-N.: Xblock-eth: extracting and exploring blockchain data from ethereum. IEEE Open J. Comput. Soc. **1**, 95–106 (2020)[Crossref](https://doi.org/10.1109/OJCS.2020.2990458)
20. 20\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr20"></a>Wu, J., Liu, J., Chen, W., Huang, H., Zheng, Z., Zhang, Y.: Detecting mixing services via mining bitcoin transaction network with hybrid motifs. IEEE Trans. Syst. Man Cybern. Syst., 1–13 (2021, to be published). [https://doi.org/10.1109/TSMC.2021.3049278](https://doi.org/10.1109/TSMC.2021.3049278)
21. 21\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr21"></a>Dai, H.-N., Wu, J., Zheng, Z. (eds.) Blockchain Intelligence. Springer Singapore, Singapore (2021)
22. 22\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr22"></a>Philippon, T.: The fintech opportunity. National Bureau of Economic Research, Working Paper 22476 (August 2016)
23. 23\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr23"></a>Anagnostopoulos, I.: Fintech and regtech: impact on regulators and banks. J. Econ. Bus. **100**, 7–25 (2018)[Crossref](https://doi.org/10.1016/j.jeconbus.2018.07.003)
24. 24\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr24"></a>Chen, T., Li, Z., Zhu, Y., Chen, J., Luo, X., Lui, J.C.-S., Lin, X., Zhang, X.: Understanding Ethereum via graph analysis. ACM Trans. Internet Technol. **20**(2), 1–32 (2020)[Crossref](https://doi.org/10.1145/3381036)
25. 25\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr25"></a>Bai, Q., Zhang, C., Xu, Y., Chen, X., Wang, X.: Evolution of ethereum: a temporal graph perspective. arXiv preprint arXiv:2001.05251 (2020)
26. 26\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr26"></a>Liu, H., Zhou T., et al.: Uncovering the network evolution mechanism by link prediction. Sci. Sin. Phys. Mech. Astron. **41**(7), 816–823 (2011)[Crossref](https://doi.org/10.1360/132010-922)
27. 27\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr27"></a>Lü, L.: Link prediction on complex networks. J. Univ. Electron. Sci. Technol. China **39**(5), 651–661 (2010)
28. 28\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr28"></a>Kumar, A., Singh, S.S., Singh, K., Biswas, B.: Link prediction techniques, applications, and performance: a survey. Physica A **553**, 124289 (2020)[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4107879)[Crossref](https://doi.org/10.1016/j.physa.2020.124289)
29. 29\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr29"></a>Yuan, L., Bin, J., Wei, Y., Hu, Z., Sun, P.: Transaction prediction in blockchain: a negative link prediction algorithm based on the sentiment analysis and balance theory. Wirel. Commun. Mob. Comput. **2021**, 1–11 (2021)[Crossref](https://doi.org/10.1155/2021/8871150)
30. 30\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr30"></a>Zheng, P., Zheng, Z., Wu, J., Dai, H.-N.: XBlock-ETH: extracting and exploring blockchain data from Ethereum. IEEE Open J. Comput. Soc. **1**(Apr.), 95–106 (2020)[Crossref](https://doi.org/10.1109/OJCS.2020.2990458)
31. 31\.<a id="oebps-html-619883_1_en_3_chapter-xhtml-cr31"></a>Chen, T., Zhang, Y., Li, Z., Luo, X., Wang, T., Cao, R., Xiao, X., Zhang, X.: TokenScope: automatically detecting inconsistent behaviors of cryptocurrency tokens in Ethereum. In: Proc. ACM SIGSAC Conf. Comput. Commun. Secur., pp. 1503–1520 (Nov. 2019)

<a id="oebps-html-619883_1_en_4_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_4](https://doi.org/10.1007/978-981-97-4430-5_4)

# 4. Evolution and Voting Behaviors in the EOSIO Networks

Jieli Liu[1](#oebps-html-619883_1_en_4_chapter-xhtml-aff4) , Zhe Chen[2](#oebps-html-619883_1_en_4_chapter-xhtml-aff5) , Weilin Zheng[1](#oebps-html-619883_1_en_4_chapter-xhtml-aff4) , Dingyuan Lu[1](#oebps-html-619883_1_en_4_chapter-xhtml-aff4) , Jiajing Wu[1](#oebps-html-619883_1_en_4_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_4_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_4_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_4_chapter-xhtml-aff5"></a>

(2)The University of Hong Kong, Pok Fu Lam, Hong Kong

<a id="oebps-html-619883_1_en_4_chapter-xhtml-contactofauthor1"></a>

**Jieli LiuEmail:** [liujli7@mail2.sysu.edu.cn](mailto:liujli7@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_4_chapter-xhtml-contactofauthor3"></a>

**Weilin ZhengEmail:** [zhengwlin@mail2.sysu.edu.cn](mailto:zhengwlin@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_4_chapter-xhtml-contactofauthor4"></a>

**Dingyuan LuEmail:** [ludy3@mail2.sysu.edu.cn](mailto:ludy3@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_4_chapter-xhtml-contactofauthor5"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_4_chapter-xhtml-contactofauthor6"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

As one of the most popular blockchain systems, EOSIO has been widely used in decentralized applications. It achieves high transaction throughput and so-called decentralization through a delegated proof-of-stake (DPoS) consensus protocol. However, recent reports have claimed that there are voting collusion and manipulation behaviors in the DPoS consensus process of EOSIO, which may greatly reduce the decentralization, fault tolerance, and reliability of the entire system. In this chapter, we obtain data from up to 135 million EOSIO blocks and conduct data-driven decentralized analysis. Specifically, we describe the decentralized evolution of DPoS in two stages, namely block producer election and block production. In addition, we study voters with similar voting behaviors and propose a method to detect abnormal mutual voting behavior in EOSIO. The analysis results show how EOSIO gradually evolves from decentralization to oligopoly. Our method can effectively capture abnormal voting phenomena in EOSIO, which can also provide important insights for the design and maintenance of other DPoS-based blockchains.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec1"></a>

## 4.1 Introduction

Both Bitcoin and Ethereum suffer from the problem of low scalability and cannot meet today’s growing demand for applications. Different from traditional PoW-based blockchain systems, EOSIO \[[1](#oebps-html-619883_1_en_4_chapter-xhtml-cr1)] adopts a more efficient consensus protocol—Delegated Proof-of-Stake (DPoS) \[[2](#oebps-html-619883_1_en_4_chapter-xhtml-cr2)] and a novel architectural design. The consensus process in EOSIO can be briefly summarized into the block producer election phase and the block production phase. It concentrates the block production process in the hands of a small set of block producers (also called super nodes) elected by the entire network, and thus improves the transaction throughput.

Intuitively, if a blockchain system is not decentralized enough, it may be easily controlled by a small minority of parties. In this case, the blockchain system is fragile and cannot ensure the facticity of the ledger records when facing threats like 51% attack \[[3](#oebps-html-619883_1_en_4_chapter-xhtml-cr3)] and selfish mining \[[4](#oebps-html-619883_1_en_4_chapter-xhtml-cr4)].

Existing few studies have considered the issue of decentralization evolution in EOSIO. Though some studies measured the decentralization of DPoS-based blockchain systems with Shannon entropy \[[5](#oebps-html-619883_1_en_4_chapter-xhtml-cr5), [6](#oebps-html-619883_1_en_4_chapter-xhtml-cr6)] and pointed out several clear vulnerabilities of EOSIO from a theoretical view \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7)], there is still a lack of study to capture and reveal the abnormal voting phenomena such as malicious voting collusion from the on-chain data. Thus unlike existing work which usually evaluates the decentralization of blockchain systems from a theoretical and static view, in this study, we conduct a data-driven and evolutionary analysis with the blockchain data from EOSIO.

The overall framework of this chapter is shown in Fig. [4.1](#oebps-html-619883_1_en_4_chapter-xhtml-fig1). Firstly, we collect the blockchain transaction data by running an EOSIO full node and replaying all transactions. Our comprehensive blockchain dataset consists of data from up to 135,000,000 blocks. Secondly, based on the data, we quantify the decentralization of EOSIO from an evolutionary view. We characterize the activities of voters, voting proxies, and block producers during the DPoS consensus process, and find that EOSIO gradually evolves from decentralization to oligopoly during the observation time. We further investigate the abnormal voting behaviors that may affect the decentralization, and propose methods to reveal the voting gangs with similar voting behaviors and mutual voting behaviors from voting relationship analysis.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig1"></a>

***Fig. 4.1***

The analysis framework

Finally, we try to answer two questions according to the analysis results: (1) **What is the root cause** of the oligopoly trend and voting anomalies in EOSIO? (2) **How can we adjust the DPoS consensus mechanism** to make the system more decentralized? Combining the time period covered by the collected data, the comparison between voting proxies in EOSIO and mining pools in Bitcoin, and the cost of voting manipulation, we draw a conclusion that the system design is more likely to be the root cause rather than the bootstrapping phase. We introduce some feasible solutions to improve the DPoS consensus mechanism, such as adjusting the number of votes allowed per account and assigning different voting weights to the multiple chosen candidates based on rating.

In summary, we make the following contributions in this chapter:

- To the best of our knowledge, our work is the first data-driven study on the decentralization evolution of EOSIO.
- We develop methods for detecting abnormal voting gangs in EOSIO and apply them to perform a network analysis of voting relationships.
- Based on our analysis, we discuss the root cause of the oligopoly trend and how to increase the decentralization degree in EOSIO, which can provide a reference for other DPoS-based blockchains.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec2"></a>

## 4.2 Preliminaries

In this section, we provide the background required to understand the operation mechanism of EOSIO and the DPoS consensus mechanism in EOSIO.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec3"></a>

### 4.2.1 Accounts and Transactions in EOSIO

Unlike Ethereum, the identity of an account in EOSIO is a human-defined string with up to 12 characters in length. Each account is created by an existing account via the new account interface and can deploy a contract on itself via the set code interface of the system account ‘eosio’. The main currency circulating in EOSIO is EOS tokens, and resources of smart contracts such as CPU and RAM can be obtained via EOS token mortgage. A transaction in EOSIO contains multiple actions, and each action corresponds to an invocation of a contract. According to the initiator in contract invocation, these actions can be divided into calling actions and inline actions, and they are called by users and triggered by contracts respectively \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7)]. In addition, EOSIO provides flexible role-based permission management allowing users to delegate their permissions to achieve high-level control over other users.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec4"></a>

### 4.2.2 DPoS and DPoS in EOSIO

The DPoS consensus mechanism has become increasingly popular and is widely adopted in blockchain systems such as EOSIO, Tron \[[8](#oebps-html-619883_1_en_4_chapter-xhtml-cr8)] and BNB Chain \[[9](#oebps-html-619883_1_en_4_chapter-xhtml-cr9)]. Instead of solving the PoW puzzles, DPoS decides its block producers according to the votes of the entire stakeholders, thus achieving high scalability in block production. The DPoS consensus mechanism consists of the block producer election phase and the block production phase, and the details of these in EOSIO are provided as follows:

Phase 1: Block Producer Election. This phase elects 21 block producers for block production. To become a block producer candidate, anyone in EOSIO who possesses enough hardware resources and the full ledger data can register via the *regproducer* interface of *‘eosio’*. Then the top 21 candidates with the highest voting weight can become block producers and obtain block production rewards.

Anyone in EOSIO can vote for the block producer candidates in two ways. The first way is voting directly through setting the *producers* parameter of the *voteproducer* interface as the list of at most 30 selected candidates. The second way is voting through a proxy by setting the *proxy* parameter of the *voteproducer* interface as the chosen proxy, and then the proxy can vote for block producer candidates on behalf of all proxied users. A user can register to become a voting proxy by setting the *isproxy* parameter of the *regproxy* interface as 1, otherwise, a user can cancel the registration by setting the *isproxy* parameter as 0.

The voting weight of a voter is related to the voting time and the staked tokens for CPU and bandwidth, which can be calculated as:

\$$\\displaystyle \\begin{aligned} weight = 10000 * stake * 2 ^{index}, \\end{aligned} $$

(4.1)

where *stake* is equal to the amount of delegated bandwidth and computation, and *index* can grow incrementally every week if voters update their voting, calculated as: \$$ index = \\frac {1}{52} * \\lfloor \\frac {t\_{vote} - t\_{init}}{7 * t_{day}}\\rfloor . $$ In this formula, \$\$t_{vote}\$$ represents the Unix timestamp when a user performs the *voteproducer* operation, \$\$t_{init}\$$ represents the Unix timestamp of Jan. 1, 2000, and \$\$t_{day}\$$ denotes the number of seconds per day. As we can see, with the same amount of stakes, the voting weight of recent votes is higher than that of earlier votes. This design can encourage voters to keep their votes updated. Moreover, once a user updates the number of stakes via *delegatebw* (increase mortgage) or *undelegatebw* (reduce mortgage), the voting weight will be automatically updated. For a voting proxy, its voting weight is the sum of the voting weight owned by all proxied voters. If a voter votes for multiple candidates, each chosen candidate can receive an equal voting weight according to the stakes and voting time of the voter.

Phase 2: Block Production. In this phase, the elected 21 block producers from the block producer election begin a round of block production on behalf of the stakeholders in EOSIO. They validate the transactions, construct the valid transactions into blocks, and then produce blocks orderly. Each elected block producer has a fixed 3-second to produce 6 blocks. Therefore, a round of block production lasts 63 seconds. If a block is not produced at the scheduled time because of network delay or other reasons, this block will be skipped and will not affect the subsequent block production. The new block confirmation process is also conducted among the 21 block producers. Once a new block is confirmed by more than 2/3 of the block producers (i.e. at least \$\$21\\times 2/3 +1 = 15\$$ block producers) through signed messages, this block will be appended to the blockchain. With DPoS, EOSIO can generate a new block every 0.5 seconds average with a throughput of up to 8000 TPS \[[10](#oebps-html-619883_1_en_4_chapter-xhtml-cr10)], which achieves higher performance than many other blockchain systems.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec5"></a>

## 4.3 Related Work

We present the related work in this section, which mainly includes the decentralization analyses of DPoS-based blockchain systems and existing analyses in EOSIO.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec6"></a>

### 4.3.1 Decentralization Analysis of DPoS-Based Blockchains

Decentralization is an important characteristic that can tell blockchain systems from traditional centralized systems. At present, there have been some studies on analyzing the decentralization of blockchain systems. Most of the existing research pointed out that Bitcoin and Ethereum have not achieved true decentralization in terms of mining power, network resources such as bandwidth, etc. \[[11](#oebps-html-619883_1_en_4_chapter-xhtml-cr11)–[13](#oebps-html-619883_1_en_4_chapter-xhtml-cr13)]. Since PoW-based blockchains become more and more centralized, Chen et al. \[[14](#oebps-html-619883_1_en_4_chapter-xhtml-cr14)] proposed tools to timely quantify the decentralization in terms of mining power in PoW-based blockchain systems. DPoS-based blockchains, on the other hand, do not require every node in the network to directly participate in block production. Instead, users can vote for a specified number of block production candidates, and the elected block producers generate blocks in turns. Thus in DPoS-based blockchains, the mining power is a weak influence factor of decentralization.

For DPoS-based blockchain systems, Jeongy \[[15](#oebps-html-619883_1_en_4_chapter-xhtml-cr15)] explored the relationship between decentralization and the number of votes allowed per account and found that the “one vote per account” rule for centralization mitigation may not be necessary. Rebello et al. \[[16](#oebps-html-619883_1_en_4_chapter-xhtml-cr16)] analyzed several quorum-based consensus protocols including the EOSIO protocol and pointed out some clear vulnerabilities of these protocols. Kwon et al. \[[5](#oebps-html-619883_1_en_4_chapter-xhtml-cr5)] measured the degree of decentralization in several blockchain systems based on PoW, PoS, and DPoS with the entropy metric and explain why it is difficult to design a fully decentralized system. Li and Palanisamy \[[6](#oebps-html-619883_1_en_4_chapter-xhtml-cr6)] conducted a comparison of decentralization between Bitcoin and Steem \[[17](#oebps-html-619883_1_en_4_chapter-xhtml-cr17)], which are based on PoW and DPoS respectively. They found that compared with Steem, Bitcoin tends to be less decentralized in general and more decentralized among top stakeholders via some distributions and the entropy metric. However, there is a lack of in-depth analyses studying the decentralization evolution and uncovering the abnormal voting phenomena in DPoS-based systems.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec7"></a>

### 4.3.2 EOSIO Analysis

Existing studies on blockchain systems cover several aspects including blockchain architecture and performance \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7), [18](#oebps-html-619883_1_en_4_chapter-xhtml-cr18)], privacy and security \[[19](#oebps-html-619883_1_en_4_chapter-xhtml-cr19)–[22](#oebps-html-619883_1_en_4_chapter-xhtml-cr22)], smart contracts and transactions \[[23](#oebps-html-619883_1_en_4_chapter-xhtml-cr23)–[26](#oebps-html-619883_1_en_4_chapter-xhtml-cr26)], etc. As one of the earliest and most typical DPoS-based blockchain systems, EOSIO has received attention of scholars these years.

In terms of architecture and security, Xu et al. \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7)] provided a comprehensive analysis on EOSIO’s architecture, performance, and economy. Lee et al. \[[27](#oebps-html-619883_1_en_4_chapter-xhtml-cr27)] introduced four attacks in EOSIO, whose root cause lies in the characteristics of EOSIO. Quan et al. \[[28](#oebps-html-619883_1_en_4_chapter-xhtml-cr28)] proposed a static analysis tool to detect the fake-transfer vulnerabilities of EOSIO’s smart contracts. He et al. \[[29](#oebps-html-619883_1_en_4_chapter-xhtml-cr29)] proposed a tool that can detect four popular vulnerabilities in EOSIO smart contracts at the WebAssembly code level. Lee et al. \[[30](#oebps-html-619883_1_en_4_chapter-xhtml-cr30)] proposed a kind of attack that can disturb the fairness of incentive policy by manipulating the block production schedule in EOSIO, and this attack can bring additional rewards or losses to block producers. In terms of blockchain transaction analysis, Huang et al. \[[10](#oebps-html-619883_1_en_4_chapter-xhtml-cr10)] investigated EOSIO and the associated DApps via measurement study. With a focus on security issues, they discovered some real-world attacks and developed detection techniques for fraudulent activities in EOSIO. Zheng et al. \[[31](#oebps-html-619883_1_en_4_chapter-xhtml-cr31)] performed a statistical analysis on 7 well-processed datasets in EOSIO, and outlined some possible research directions based on the proposed datasets. Zhao et al. \[[32](#oebps-html-619883_1_en_4_chapter-xhtml-cr32)] abstracted the records of four major activities in EOSIO as complex networks \[[33](#oebps-html-619883_1_en_4_chapter-xhtml-cr33), [34](#oebps-html-619883_1_en_4_chapter-xhtml-cr34)] and obtained some interesting observations via network metric analysis. However, none of them quantify the decentralization characteristic and investigate the abnormal voting phenomena based on the real transaction data in EOSIO.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec8"></a>

## 4.4 Data Preparation for EOSIO Blockchain Analysis

Our investigation spans over 135 million blocks within the EOSIO blockchain, encompassing transaction data from June 8, 2018, to August 5, 2020. To evaluate EOSIO’s decentralization, we amassed three distinct datasets: block headers, transaction actions, and voting weights by operating a full EOSIO node and replaying all transactions. This comprehensive dataset is hosted on the *XBLOCK.PRO*<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn1_source"></a>[1](#oebps-html-619883_1_en_4_chapter-xhtml-fn1) platform.

- **Block Headers:** Serving as a concise summary of each block, the block header includes vital details such as the identity of the block producer, the timestamp, and the transaction Merkle root. We sourced this data through *Nodeos* \[[35](#oebps-html-619883_1_en_4_chapter-xhtml-cr35)], the core service daemon of EOSIO, ensuring real-time synchronization with the mainnet.
- **Transaction Actions:** Within EOSIO, transactions are composed of actions, each representing a smart contract invocation. Notably, the blockchain records only user-initiated actions, leaving inline actions—those triggered by other actions—unrecorded. To capture this nuanced data, we utilized the *history\_file\_plugin* \[[31](#oebps-html-619883_1_en_4_chapter-xhtml-cr31)] to gather all action traces in JSON format, extracting significant actions such as *delegatebw*, *undelegatebw*, *regproxy*, and *voteproducer* from these traces.
- **Voting Weight Data:** Reflecting the dynamic nature of EOSIO’s electoral landscape, the voting weight assigned to block producer candidates fluctuates with voter activity and staked tokens. We meticulously tracked these variations by analyzing transaction actions, periodically updating our comprehensive dataset to accurately reflect the changing voting weights.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec9"></a>

## 4.5 Measuring Decentralization in EOSIO

In this section, we present a decentralization measurement study in EOSIO considering the processes of block producer election and block production. We try to characterize all voters, proxies, and block producers participating in the DPOS consensus process. Based on the analysis results, we reveal the evolution of decentralization and discuss some findings in the EOSIO network.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec10"></a>

### 4.5.1 Block Producer Election in EOSIO

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec11"></a>

#### 4.5.1.1 Overview of Block Producer Election

Based on the statistics of the collected comprehensive blockchain dataset, we find out that there are a total of 2,009,168 accounts. Among these accounts, 1,739,839 accounts have staked EOS tokens as stakeholders while only 84,668 accounts have participated in the block producer election procedure as voters, occupying 4.87% of all stakeholders. The result indicates that only a small fraction of all stakeholders have taken part in the voting process.

We then calculate the number evolution of accounts for voters and all stakeholders, as shown in Fig. [4.2](#oebps-html-619883_1_en_4_chapter-xhtml-fig2)a. We found that the number of stakeholders and voters increases over time, but the number growth rate of voters is far short of the number growth rate of all stakeholders. This infers that many stakeholders do not care about the block production election, or even do not understand the voting mechanism in EOSIO. The power to decide who will become block producers thereby is held by a small number of stakeholders. Furthermore, from the amount evolution of staked tokens held by voters and all accounts shown in Fig. [4.2](#oebps-html-619883_1_en_4_chapter-xhtml-fig2)b, we observe that the staked tokens held by voters account for half or less of the total network for a long time. Moreover, with the passage of time, the proportion of staked tokens held by voters increases. Since the waiver of trading fees in EOSIO provides a user-friendly environment, the DApp users will have less incentive to mortgage their EOS tokens. However, application developers, voters, and block producer candidates have a strong motivation to mortgage their EOS tokens. Especially, block producer candidates always canvass other stakeholders for electoral support to ensure their position, and thus the amount of staked tokens of the voters exhibits an increasing trend.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig2"></a>

***Fig. 4.2***

The number evolution and staked token evolution of voters and all stakeholders. (**a**) Number evolution. (**b**) Staked token evolution

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec12"></a>

#### 4.5.1.2 Distribution Statistics

We investigate the staked token distribution among all voters and the received voting weight distribution among all block producer candidates. After mapping the continuous values to 100,000 equally spaced intervals, the distributions with a fitting line \$\$y\\sim x^{-\\alpha }\$$ are shown in Fig. [4.3](#oebps-html-619883_1_en_4_chapter-xhtml-fig3)a and b. Both of the two distributions are in line with the power-law distribution, which indicates that a small number of voters hold a large amount of staked tokens, and a few block producer candidates have received a large voting weight. We then calculate the fraction of stakes held by the richest voters, and find out that the top 5% of the voters possess more than 95% of the stakes. As for block producer candidates, the top 10% of the candidates have received more than 95% of the voting weight in the whole network. Hence, the voting resource is unevenly distributed among both voters and block producer candidates. As one of the security risks, most of the voting powers are concentrated in only a few rich voters so that the voting results basically depend on a small number of voters. On the other hand, the extremely uneven distribution of received voting weight among block producer candidates can lead to the rich-get-richer phenomenon, also named the *Matthew effect* \[[36](#oebps-html-619883_1_en_4_chapter-xhtml-cr36)]. In the long run, it is easy to form block production oligopoly among the most popular block producers.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig3"></a>

***Fig. 4.3***

The staked token distribution of voters (the tokens of proxied accounts are accumulated on proxies) and the received voting weight distribution of block producer candidates, calculated at the end of the 135,000,000 blocks. (**a**) Staked token distribution of voters. (**b**) Received voting weight distribution of block producer candidates

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec13"></a>

#### 4.5.1.3 Statistics of Voting Proxies

Although anyone who stakes EOS tokens can participate in the governance of EOSIO with their voting power, block producer candidates should be carefully chosen by considering some factors such as resources, community contribution, and location of block producer candidates. However, not every stakeholder has enough incentive to investigate different candidates and stays abreast of every new proposal in EOSIO, especially those who only hold a tiny amount of EOS tokens.

Voting proxies are accounts that perform voting on behalf of other accounts. They vote for block producer candidates with voting power collected from proxied accounts, and communicate to the proxied accounts which block producer candidate they choose. Each user can delegate its voting power to a voting proxy, and can also withdraw its voting power from the proxy at any time. In general, voting proxies can remove the high barrier of participating in governance for users and fully arouse the initiative of individual users, thereby increasing user participation in the voting process.

According to our statistics, 1792 accounts have registered to become voting proxies, and 924 of them have been delegated as proxies via the *voteproducer* interface. It is worth noting that 40,561 of the 84,668 voters have voted through voting proxies, which means more than 47% of the voters execute their voting power via voting proxies. Figure [4.4](#oebps-html-619883_1_en_4_chapter-xhtml-fig4)a–c show the account number evolution, staked token evolution, and voting weight evolution of all voters and proxied voters. By cooperating with the corresponding value share evolution of the proxied voters in all voters in Fig. [4.4](#oebps-html-619883_1_en_4_chapter-xhtml-fig4)d–f, the increasing use of proxies can be observed. Moreover, after May 2019, nearly 70% of the voting weights are delegated to voting proxies. Under this trend, the votes of voting proxies can exercise considerable influence over the election results, since most of the voting powers are centralized in the voting proxies. A valuable research issue is whether there exist abuses of rights among the voting proxies, and we will discuss this issue in Sect. [4.6](#oebps-html-619883_1_en_4_chapter-xhtml-sec17).<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig4"></a>

***Fig. 4.4***

Statistics about the proxied voters. (**a**)–(**c**) show the account number evolution, staked token evolution, and voting weight evolution of all voters and proxied voters. (**d**)–(**f**) display the value share evolution of the proxied voters in all voters for account number, staked tokens, and voting weights

**Finding 1** Stakeholders increase rapidly with the boom of the EOSIO DApp ecology, but only a small number of them participated in the voting. The voting power is concentrated in a small number of voters.

**Finding 2** The received voting weights are unevenly distributed among the block producers, making it possible to form a block production oligopoly in the future.

**Finding 3** Proxies account for an increasingly large proportion of the total voting power. Though the use of proxies can arouse more stakeholders to participate in the consensus government, it also centralizes most of the voting power in a small part of the accounts.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec14"></a>

### 4.5.2 Block Production in EOSIO

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec15"></a>

#### 4.5.2.1 Overview of Block Production

When focusing on block production, we found that there are 615 accounts registering to become block producer candidates. Among these candidates, 602 candidates have received voting weights from the voters and 62 candidates have become block producers. Figure [4.5](#oebps-html-619883_1_en_4_chapter-xhtml-fig5)a shows the number evolution of block producers, and both the monthly number and accumulated number are given. Although the 21 elected block producers can be updated in each round according to their real-time voting weight, only around 25 different accounts are elected as block producers each month. Moreover, the chosen block producers are relatively fixed after September 2019.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig5"></a>

***Fig. 4.5***

Statistics about block producers, including (**a**) the number evolution and (**b**) distribution of days participating in block production

Figure [4.5](#oebps-html-619883_1_en_4_chapter-xhtml-fig5)b shows the distribution of days that block producers participate in block production, from which we can observe that about 10 block producers participated in block production for more than 600 days during the 135,000,000 blocks which cover about 790 days. These statistics illustrate that despite a large number of candidates, the set of block producers has small variations. Many accounts participate in block production for a long term. Once these accounts are in collusion, it is easy to achieve double-spend attacks since EOSIO can only tolerate no more than 1/3 of malicious block producers. In theory, the block producers acting in malicious manners can be voted out. Yet in practice, block producers can earn considerable rewards in block production so that most of them possess a large number of EOS tokens and can become one of the largest stakeholders, making it even harder to vote the malicious block producers out.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec16"></a>

#### 4.5.2.2 Quantitative Analysis with Information Entropy

Previous studies have introduced the information entropy metric to quantify the degree of decentralization in block production \[[6](#oebps-html-619883_1_en_4_chapter-xhtml-cr6), [37](#oebps-html-619883_1_en_4_chapter-xhtml-cr37)]. Here we adopt information entropy to compare the decentralization degree of different months. The information entropy metric for a month *i*, namely \$\$H(X_i)\$$, can be calculated as follows:

\$$\\displaystyle \\begin{aligned} p_j = \\frac{x_j}{\\sum_{j=1}^{n}x_j}, \\mathrm{where}\\ x_j \\in X_i, \\end{aligned} $$

(4.2)

\$$\\displaystyle \\begin{aligned} H(X_i) = -\\sum_{j=1}^{n}p_jlog_2p_j, \\end{aligned} $$

(4.3)

where \$\$X_i\$$ stores the number of blocks produced by each producer in month *i*, \$\$x_j\$$ denotes the number of blocks produced by block producer *j*, and *n* denotes the measuring range of top-*n* block producers. The greater the value of \$\$H(X_i)\$$ is, the greater the decentralization degree is in the month, since the block production is more random and disorderly.

We display the quantitative results of information entropy in Fig. [4.6](#oebps-html-619883_1_en_4_chapter-xhtml-fig6) by setting \$\$n = 10, 20,\$$ and the number of block producers in each month. From Fig. [4.6](#oebps-html-619883_1_en_4_chapter-xhtml-fig6)a and b, we can observe that the information entropy of the first month is much smaller than that of the latter months for \$\$n = 10\$$ and \$\$n = 20\$$, which indicates that block production in the early days of EOSIO was more centralized among the top stakeholders. While as shown in Fig. [4.6](#oebps-html-619883_1_en_4_chapter-xhtml-fig6)c, block production in months Oct. 2018–Apr. 2019, Jul. 2019, Oct. 2019–Jul. 2020 were also relatively centralized in general. Combining Figs. [4.6](#oebps-html-619883_1_en_4_chapter-xhtml-fig6)c and [4.5](#oebps-html-619883_1_en_4_chapter-xhtml-fig5)a, we can infer that this phenomenon may be due to the less replacement of block producers in these months.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig6"></a>

***Fig. 4.6***

Evolution of the information entropy. (**a**) Entropy with \$\$n=10\$$. (**b**) Entropy with \$\$n=20\$$. (**c**) Entropy with \$\$n=\$$ the number of all block producers

**Finding 4** Despite the relatively large amount of candidates, the set of block producers has small variations in general.

**Finding 5** In the early days of EOSIO, block production was centralized among the top stakeholders. While in the latest months, block production has been centralized in a specific group due to the small variations of the block producer set.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec17"></a>

## 4.6 Exploring the Voting Gang Anomalies

In the previous section, the voting election and block production in EOSIO are characterized statistically. The obtained observations have exposed some problems that may give rise to power centralization such as large stakeholders working together, proxies abusing their power, and block producers colluding. To further discover these associated abnormal voting behaviors, in this section, we first develop a voter clustering method to detect those who potentially work together and share their voting targets. After that, we discuss the mutual voting behaviors in EOSIO and propose methods to identify and analyze suspicious mutual voting relationships.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec18"></a>

### 4.6.1 Voter Clustering Analysis

A great concern is that some large stakeholders can form alliances and communicate with each other before voting to solidify the positions of specific block producer candidates \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7)], causing voting manipulation and unfair competition. According to the statistics given in Sect. [4.5.2](#oebps-html-619883_1_en_4_chapter-xhtml-sec14), there are a total of 615 accounts registering as block producer candidates. Since each voter can vote for up to 30 block producer candidates and the votes can be updated in each round, the probability that two voters often vote for two similar groups of candidates is relatively low. Therefore, voters who often support similar block producer candidates are more abnormal and likely to be motivated by common interests.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec19"></a>

#### 4.6.1.1 Method Design

**Algorithm 1 Voter clustering based on similar voting behaviors**

To group the voters which have similar voting behaviors into a cluster, we take the similarity of the historical voting records of voters into account. Firstly, the block producer candidates are numbered and the candidates voted by a voter *u* are recorded in a set \$\$R_i(u)\$$ with a maximum length of 30 for sampling time *i*. Based on Jaccard’s coefficient, the voting similarity of voter *u* and *v* can be calculated as:

\$$\\displaystyle \\begin{aligned} S(u,v)=\\frac{\\sum\_{i=1}^{n}|R_i(u)\\cap R_i(v)|}{\\sum_{i=1}^{n}|R_i(u)\\cup R_i(v)|}, \\end{aligned} $$

(4.4)

where *n* is the sampling number. In the experiment, we record the voting results at the end of each month from Jun. 8, 2018 to Aug. 5, 2020 and thus \$\$n=26\$$. Secondly, we propose a similarity-based voter clustering method that can automatically output the clusters with similar voting behaviors. Algorithm 1 shows the pseudocode of the method, where the input contains the set of voters *V* , the voting similarity *S*, and a similarity threshold \$$\\theta $$. The set *visited* in the algorithm is used to mark the visited voters, and we treat each unvisited voter as a center. For each center, we select out voters whose voting similarity is greater than or equal to \$$\\theta $$, and add them to *visited* and the cluster that the center belongs to. And then, if a center \$\$v_i\$$ has members behaving similarly in its cluster \$\$C_i\$$, voters who are similar to these members are also added into \$\$C_i\$$. Finally, the cluster \$\$C_i\$$ is added to the output cluster set *C*.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec20"></a>

#### 4.6.1.2 Detecting in Large Stakeholders

As mentioned in Sect. [4.5.1](#oebps-html-619883_1_en_4_chapter-xhtml-sec10), the staked token distribution among all voters is extremely uneven. About 5% of the voters possess more than 95% of the stakes in the statistics. Hence the votes of large stakeholders have a great effect on the governance of EOSIO. To investigate the abnormally large stakeholders with similar voting behaviors, we apply Algorithm 1 with \$\$\\theta = 0.9\$$ on the top 5% richest voters in the sampled voting records (the proxied stakes are accumulated on the proxies when ranking). And 88 clusters including 293 voters are detected from a total of 2723 voters.

**Voting Snapshot and Time Distribution Analysis**

Figure [4.7](#oebps-html-619883_1_en_4_chapter-xhtml-fig7)a displays three voting snapshots of the large stakeholders in the top 10 detected clusters with the most staked tokens, where the y-axis depicts the index of the detected large stakeholders and the x-axis depicts the index of the candidates. If a voter *y* votes for block producer candidates \$\$x_1, x_2\$$ and \$\$x_3\$$, then (\$\$x_1\$$, *y*), (\$\$x_2\$$, *y*) and (\$\$x_3\$$, *y*) will be colored in the corresponding color of its cluster. From this figure, we can observe that voters in the same detected cluster have similar voting behaviors in both time and space, which can be illustrated by the very similar block producer candidates they support in these different snapshots. Figure [4.7](#oebps-html-619883_1_en_4_chapter-xhtml-fig7)b shows the distribution of time when the large stakeholders in the top 10 detected clusters with the most staked tokens operate the *voteproducer* action, where different clusters are assigned different colors. To our surprise, though the voters in the same cluster are grouped according to the sampled voting records, the voting actions of these voters occur at very similar timestamp sequences.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig7"></a>

***Fig. 4.7***

(**a**) Three voting snapshots and (**b**) the voting time distribution of the top 10 detected clusters with the most staked tokens among the large stakeholders, where votes in the same cluster are assigned the same color

**Account Creation Relationship Analysis**

We further analyze the account creators of the detected voters, and visualize the relationships between account creators and the 88 clusters in Fig. [4.8](#oebps-html-619883_1_en_4_chapter-xhtml-fig8)a. In each edge of the figure, a target node represents a detected cluster of large stakeholders, a source node represents an account creator that creates one or more stakeholders in a cluster, and the edge thickness is related to the number of accounts created. From the figure, we can observe that most accounts in the same cluster are created by the same account, implying that these voters are likely to be controlled by the same entity and therefore they have similar voting behaviors. Such kind of gathering phenomena in voting among large stakeholders can easily cause block production monopoly—the allies of these large stakeholders can obtain a solid position in the election. Moreover, they will earn more rewards (i.e., EOS tokens) from block production to consolidate their advantage in the election.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig8"></a>

***Fig. 4.8***

Relationships between account creators and the detected clusters, where clusters owning one account creator are colored red. (**a**) Large stakeholders. (**b**) Proxies

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec21"></a>

#### 4.6.1.3 Detecting in Voting Proxies

Voting proxies are accounts that can execute the voting power of proxied accounts. Recently, we have seen the rising use of proxies in voting. Usually, users delegate their voting rights to a proxy out of trust in the proxy’s voting decision. However, we can not exclude the presence of “selfish” proxies that only vote for their alliance members but do not consider the governance of the community. In this way, if users delegate their voting power to these proxies, they will actually increase the competitiveness of a particular alliance and the degree of centralization. Therefore, there is an urgent need to understand the voting behaviors of voting proxies. Particularly, proxies having similar voting behaviors deserve our attention. And these proxies are suspected of being manipulated by the same entity and using different identities to attract the authorization of other stakeholders. To this end, we apply Algorithm 1 to all proxies in our comprehensive blockchain dataset with \$\$\\theta =0.9\$$. We totally detect 35 clusters including 162 proxies.

**Voting Snapshot and Time Distribution Analysis**

Figure [4.9](#oebps-html-619883_1_en_4_chapter-xhtml-fig9)a and b visualize three voting snapshots and the voting time distribution of proxies in the top 10 detected clusters with the most staked tokens, where different clusters are assigned different colors. Similar to the observations drawn from Figs. [4.7](#oebps-html-619883_1_en_4_chapter-xhtml-fig7)a and b, the proxies in the same detected clusters vote for almost the same group of block producer candidates across time, and the time they operate the *voteproducer* action shows a convergent trait.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig9"></a>

***Fig. 4.9***

(**a**) Three voting snapshots and (**b**) the voting time distribution of the top 10 detected clusters with the most staked tokens among the proxies, where votes in the same cluster are assigned the same color

**Account Creation Relationship Analysis**

Figure [4.8](#oebps-html-619883_1_en_4_chapter-xhtml-fig8)b displays the account creation relationships between account creators and the 35 detected clusters, where a target node denotes a cluster of voting proxies and a source node denotes an account creator that creates one or more proxies in a cluster. As we can see, among 17 of the 35 clusters, proxies in the same cluster are created by one account. Furthermore, we observe that many proxies in the same cluster have common features in their account name. For example, proxies *‘hashfineos44’*, *‘hashfineos14’*, *‘hashfineos33’*, *‘hashfineos55’* and *‘hashfineos13’* have the common prefix ‘hashfineos-’ in their name, proxies *‘reallyreally’*, *‘windowwindow’*, *‘citycitycity’*, *‘familyfamily’*, etc. have reduplicated words in their name. We also observe that the account *‘octgenerator’* creates 53 proxies detected in the same cluster, and all these proxies only vote for *‘oraclegogogo’*. Though it is impossible to verify that the detected accounts in the same cluster belong to an entity due to the pseudonymous nature, the analysis results from multiple voting snapshots, the voting time distribution, and the relationships between account creators and the detected clusters indicate the abnormality of these addresses.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec22"></a>

### 4.6.2 Mutual Voting Anomaly Detection

In this part, we aim to investigate the mutual voting anomalies, which are suspected of trading votes and sharing the rewards of block production with gang members. We first propose and discuss three mutual voting patterns, and then we develop an algorithm to explore the potential mutual voting anomalies.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec23"></a>

#### 4.6.2.1 Mutual Voting Pattern Analysis

As shown in Fig. [4.10](#oebps-html-619883_1_en_4_chapter-xhtml-fig10)a, we consider three types of mutual voting patterns in the analysis: (a) ***linear-shaped*** pattern, in which two voters vote for each other directly to enhance their roles; (b) ***triangular-shaped*** pattern, where a voter *a* use a proxy to vote for another voter *b* and receive the vote back from the voter *b*; and (c) ***eight-shaped*** pattern, in which two proxies and two proxied voters are involved and the two proxied voters vote for each other via proxies. Among these three kinds of mutual voting patterns, the linear-shaped pattern and the triangular-shaped pattern are relatively abnormal voting behaviors since there exist votes from non-proxy entities.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig10"></a>

***Fig. 4.10***

(**a**) Three mutual voting patterns and (**b**) their number evolution

The number evolution of these patterns in different months is displayed in Fig. [4.10](#oebps-html-619883_1_en_4_chapter-xhtml-fig10)b, and the occurring time of the mutual voting actions in each pattern is constrained to seven days. From the figure and the voting records, we obtain the following observations:

- Linear-shaped pattern: We observe that this most straightforward mutual voting pattern occurred mainly between some famous super nodes such as *‘eosnationftw’*, *‘eoslaomaocom’*, and *‘argentinaeos’* in June 2018.
- Triangular-shaped pattern: The occurrence number of triangular-shaped patterns reached a peak in May 2019. By analyzing the voting records, we find that the occurrence of this peak is related to the obvious mutual voting behaviors between *‘games.eos’*, *‘eos.fish’*, *‘starteosiobp’*, and *‘dilidilifans’*. Firstly, the votes between *‘starteosiobp’* and *‘eos.fish’*, *‘games.eos’* and *‘eos.fish’*, *‘dilidilifans’* and *‘eos.fish’* are in triangular-shaped patterns with proxy *‘start13.io’*, *‘proxyfordili’*, and *‘starteos.io’* respectively. Secondly, *‘dilidilifans’* and *‘games.eos’*, *‘starteosiobp’* and *‘dilidilifans’*, *‘games.eos’* and *‘starteosiobp’* are in eight-shaped patterns via their proxy, which provides further proof of the close relationship among these voters.
- Eight-shaped pattern: It occurs more frequently than the linear-shaped pattern and triangular-shaped pattern because voting proxies are active. The maximum occurrence number peak of the eight-shaped pattern reached in October 2018, mainly caused by the frequently mutual voting of *‘acroeos12345’* and *‘eoseouldotio’* with a common proxy *‘votetochange’*. This mutual voting relationship is natural since *‘acroeos12345’* and *‘eoseouldotio’* are both the organizers of the proxy *‘votetochange’*.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn2_source"></a>[2](#oebps-html-619883_1_en_4_chapter-xhtml-fn2) For the second peak reached in May 2019, we observe that there exists a large connected component formed by the mutual voting relationships of proxied voters. And among the 17 proxied voters in this connected component, the average clustering coefficient is 0.431 and 26 triangles are constructed by their relationships, indicating that these voters tend to gather together.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec24"></a>

#### 4.6.2.2 Mutual Voting Gang Detection

To investigate the mutual voting gang anomalies, we build a voting network based on the voting actions, where each node denotes an account and each edge denotes the voting relationship between a pair of accounts. Then, we visualize the voting network by randomly selecting 5000 edges. As shown in Fig. [4.11](#oebps-html-619883_1_en_4_chapter-xhtml-fig11)a, the voting network contains many hub nodes whose one-hop neighborhood (also named egonet) is in a near-star pattern and the one-hop neighbors are almost not connected. While for mutual voting gangs, more connections and higher relation intensity tend to exist within these gangs to maintain the status of the gang members. Therefore, there are some abnormal nodes whose one-hop neighbors are very well connected in the gangs, which can be described by the near-clique anomalies (Fig. [4.11](#oebps-html-619883_1_en_4_chapter-xhtml-fig11)b). And in the previous part, we have described three special cases of this anomaly.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig11"></a>

***Fig. 4.11***

Visualization of the voting network (**a**) and near-clique anomaly (**b**)

Based on this observation, we first define the voting intensity between a pair of nodes by taking the voting frequency, duration, and voting weight into account. The voting intensity from node *i* to node *j* (denoted by \$\$I_{ij}\$$) is calculated as: <a id="oebps-html-619883_1_en_4_chapter-xhtml-equ5"></a>

\$$\\displaystyle \\begin{aligned} {} I\_{ij} = \\frac{1}{3} * (\\frac{F\_{ij}}{\\sum\_{u\\in N(i)}F\_{iu}} + \\frac{T\_{ij}}{\\sum\_{u\\in N(j)}T\_{uj}} + \\frac{P\_{ij}}{\\sum\_{u\\in N(j)}P_{uj}}), \\end{aligned} $$

(4.5)

where \$\$N(\\cdot )\$$ represents the neighbors of a node, \$\$F_{ij}\$$ represents the voting frequency from *i* to *j*, \$\$T_{ij}\$$ is the cumulative voting time duration and \$\$P_{ij}\$$ is the average voting weight from *i* to *j*. The item about the voting frequency measures the willingness of *i* to vote to *j*, and the items about the voting time duration and average voting weight measure *i*’s voting share of *j*. We then assign a weight to each edge in the voting network to represent the voting intensity between a pair of nodes. And the weight \$\$w_{ij}\$$ of the edge between nodes *i* and *j* is decided by the voting intensity from *i* to *j* and the voting intensity from *j* to *i*, i.e., \$\$w\_{ij} = I\_{ij} + I_{ji}\$$.

After obtaining the weighted voting network, we detect near-clique anomalies among the block producer candidates with the OddBall algorithm \[[38](#oebps-html-619883_1_en_4_chapter-xhtml-cr38)], and reconstruct the network by only keeping the relationships between the block producer candidates in the egonet of the detected accounts. Finally, we apply the Louvain algorithm \[[39](#oebps-html-619883_1_en_4_chapter-xhtml-cr39)] on the weighted network to detect suspicious voting gangs. The community detection results are obtained according to the voting intensity calculated by Eq. ([4.5](#oebps-html-619883_1_en_4_chapter-xhtml-equ5)) and modularity optimization. After obtaining the clustering results, we weed out the accounts with only one edge in the reconstructed network since these accounts have less possibility to participate in voting collusion in their cluster. And the outputs are clusters with more than one node.

**Results**

We obtain 11 abnormal voting gangs which totally include 334 nodes from community detection on the reconstructed network. In particular, we find out that a detected cluster, which includes 41 accounts, has 14 accounts coinciding with more than half of the accounts allegedly involved in mutual voting reported in \[[40](#oebps-html-619883_1_en_4_chapter-xhtml-cr40)]. The voting relationships in this cluster are shown in Fig. [4.12](#oebps-html-619883_1_en_4_chapter-xhtml-fig12), where the detected labeled accounts and their relationships are assigned the color orange. As we can see in this figure, though there are some accounts having not been reported in \[[40](#oebps-html-619883_1_en_4_chapter-xhtml-cr40)], they have strong voting relationships with the cluster members. Furthermore, 24 of the 26 reported accounts have been detected in the output clusters.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig12"></a>

***Fig. 4.12***

Visualization of the voting relationships in the detected cluster of *‘eoshuobipool’*, where the accounts reported in \[[40](#oebps-html-619883_1_en_4_chapter-xhtml-cr40)] are labeled and assigned the color orange

Moreover, we observed that there is a huge detected cluster consisting of 105 accounts. Among these accounts, 102 are named in a regular pattern with ‘hayd’ or ‘g44t’ as the first four letters and ‘ge’ as the last two letters, such as *‘haydiojxgege’*, *‘haydiojygage’*, *‘g44tomrygige’* and *‘g44tomzugqge’*. And 2 of the last 3 accounts are created by two accounts in this naming rule. These observations illustrate that the method can help us notice some abnormal mutual voting gangs.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec25"></a>

## 4.7 Discussion

Previous sections have presented a decentralization evolution analysis on EOSIO, a famous DPoS-based blockchain system, and reported some abnormal voting phenomena in the system. In this section, we attempt to answer two questions and provide insights into decentralization enhancement for EOSIO and other DPoS-based blockchain systems.

***Q1: What is the root cause of the oligopoly trend and voting anomalies in EOSIO? The bootstrapping phase or the system design?***

We prefer to attribute the root cause of the oligopoly trend and voting anomalies in EOSIO to the system design. On the one hand, the EOSIO voting data studied in previous sections cover more than two years. The collected data include the most prosperous phase of EOSIO to date,<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn3_source"></a>[3](#oebps-html-619883_1_en_4_chapter-xhtml-fn3) which is much longer than the bootstrapping phase.

On the other hand, we find that voting proxies have recently become popular in the analysis. Some proxies even try to attract new users by claiming that delegating the voting power to them will result in high profit with zero risk, e.g., a proxy of newpool as shown in Fig. [4.13](#oebps-html-619883_1_en_4_chapter-xhtml-fig13). These proxies are likely to grow into large staking pools, which not only violates the original design intention of voting proxies but also raises some security concerns similar to those brought by mining pools in Bitcoin \[[13](#oebps-html-619883_1_en_4_chapter-xhtml-cr13)], such as 51% attacks. It is rather difficult for a stakeholder to resist the temptation of high profits claimed by these proxies. As a result, we can see that with the passage of time, the majority of the voting weight becomes concentrated in voting proxies. Similarly, the phenomenon that the mining power is concentrated in mining pools also exists in Bitcoin and Ethereum, which are relatively mature platforms now.<a id="oebps-html-619883_1_en_4_chapter-xhtml-fig13"></a>

***Fig. 4.13***

The introduction of a proxy belonging to the newpool decentralized staking pool on alohaeos.com, claiming that “High profit, Zero risk”

In addition, the cost of voting manipulation is low since each voter can vote for up to 30 block producer candidates at the same time with no reduction in the voting weight that each candidate can receive. Not surprisingly, we can observe that there are some abnormal voting gangs with similar voting behaviors or mutual voting behaviors in the analysis. These anomalies are obviously driven by interests and are closely related to the design of the incentive mechanism of EOSIO. Therefore, the root cause of the oligopoly trend and voting anomalies is closely related to the system design and not necessarily related to the bootstrapping phase of EOSIO.

***Q2: Are there any mechanisms to adjust the DPoS consensus mechanism and make the system more decentralized?***

First, voters in EOSIO only account for a small fraction of stakeholders, and their voting power is distributed unevenly. This means a few voters possessing a large number of stakes are sufficient to centralize the network. Furthermore, as we discussed earlier, each voter can vote for multiple block producer candidates at the same time with no discount on the voting weight, which leads to a low cost of voting manipulation. Therefore, except to encourage the stakeholders to be active in the governance of EOSIO, the community can also look for a more reasonable value for the number of votes allowed per account. Existing work \[[15](#oebps-html-619883_1_en_4_chapter-xhtml-cr15)] has studied how to find the optimal number of votes allowed per account in DPoS with the governance game. Moreover, another possible solution can be the introduction of an attenuation coefficient when a user votes for multiple candidates. In this manner, a voter can assign different voting weights to the multiple chosen candidates based on their ratings.

Second, the voting weights in EOSIO are increasingly concentrated in voting proxies, and the block production is also centralized in a small group of block producers with little variation. This fact makes the system rather vulnerable to centralized control and malicious attacks. For example, Xu et al. \[[7](#oebps-html-619883_1_en_4_chapter-xhtml-cr7)] proposed a type of voting attack executed by block producers—the block producers can collude to blacklist the voters with large stakes which will threaten the authority of the block producers themselves. Moreover, in our analysis, we reveal some abnormal voting gangs working in collusion. To tackle this problem, we notice that some researchers have proposed a theory-based reward and punishment incentive mechanism for DPoS to improve the voting enthusiasm of nodes and deal with the voting anomalies in the system \[[41](#oebps-html-619883_1_en_4_chapter-xhtml-cr41)]. In addition, our analysis method can also help voters investigate the voting behaviors of voting proxies and block producer candidates before making a choice.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-sec26"></a>

## 4.8 Conclusion

This chapter performed the first decentralization evolution study on EOSIO, a typical DPoS-based blockchain system. We analyzed how EOSIO gradually evolves from decentralization to oligopoly by characterizing the activities of voters, voting proxies, and block producers participating in the DPOS consensus process, and obtained many insightful findings. Moreover, we put forward methods to discover the abnormal voting gangs with similar voting behaviors and mutual voting behaviors. Some suspected voting manipulation phenomena have been revealed in our analysis. Besides, we discussed the root cause of the oligopoly trend and the mechanisms for enhancing the decentralization of EOSIO according to the analysis results, which can also provide a reference for other DPoS-based blockchain systems.

<a id="oebps-html-619883_1_en_4_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr1"></a>Block.one: EOS.IO technical white paper v2. [https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md](https://github.com/EOSIO/Documentation/blob/master/TechnicalWhitePaper.md) (2018)
2. 2\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr2"></a>Block.one: Consensus protocol. [https://developers.eos.io/welcome/v2.0/protocol/consensus_protocol](https://developers.eos.io/welcome/v2.0/protocol/consensus_protocol) (2020)
3. 3\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr3"></a>Ye, C., Li, G., Cai, H., Gu, Y., Fukuda, A.: Analysis of security in blockchain: case study in 51%-attack detecting. In: Proc. Int. Conf. Dependable Syst. Their Appl., pp. 15–24. IEEE, Dalian (2018)
4. 4\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr4"></a>Eyal, I., Sirer, E.G.: Majority is not enough: Bitcoin mining is vulnerable. In: Proc. Int. Conf. Financ. Cryptogr. Data Secur., pp. 436–454. Springer, Barbados (2014)
5. 5\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr5"></a>Kwon, Y., Liu, J., Kim, M., Song, D., Kim, Y.: Impossibility of full decentralization in permissionless blockchains. In: Proc. 1st ACM Conf. Adv. Financ. Technol., pp. 110–123. Association for Computing Machinery, Zurich (2019)
6. 6\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr6"></a>Li, C., Palanisamy, B.: Comparison of decentralization in DPoS and PoW blockchains. In: Proc. Int. Conf. Blockchain. Virtual Conference, pp. 18–32. Springer International Publishing (2020)
7. 7\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr7"></a>Xu, B., Luthra, D., Cole, Z., Blakely, N.: EOS: an architectural, performance, and economic analysis. [https://whiteblock.io/wp-content/uploads/2019/07/eos-test-report.pdf](https://whiteblock.io/wp-content/uploads/2019/07/eos-test-report.pdf) (2018)
8. 8\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr8"></a>Foundation, T.: Tron: advanced decentralized blockchain platform. [https://tron.network/static/doc/white_paper_v_2_0.pdf](https://tron.network/static/doc/white_paper_v_2_0.pdf) (2018)
9. 9\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr9"></a>Binance: Binance Smart Chain. [https://github.com/binance-chain/bsc](https://github.com/binance-chain/bsc) (2020)
10. 10\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr10"></a>Huang, Y., Wang, H., Wu, L., Tyson, G., Luo, X., Zhang, R., Liu, X., Huang, G., Jiang, X.: Understanding (mis)behavior on the EOSIO blockchain. In: Proc. ACM Meas. Anal. Comput. Syst. Association for Computing Machinery, Boston (2020)
11. 11\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr11"></a>Beikverdi, A., Song, J.: Trend of centralization in Bitcoin’s distributed network. In: Proc. 2015 IEEE/ACIS 16th Int. Conf. Softw. Eng. Artif. Intell. Netw. Parallel/Distributed Comput., pp. 1–6. IEEE, Takamatsu (2015)
12. 12.Gencer, A.E., Basu, S., Eyal, I., van Renesse, R., Sirer, E.G.: Decentralization in Bitcoin and Ethereum networks. In: Proc. Int. Conf. Financ. Cryptogr. Data Secur., pp. 439–457. Springer, Curaçao (2018)
13. 13\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr13"></a>Wang, C., Chu, X., Qin, Y.: Measurement and analysis of the Bitcoin networks: a view from mining pools. In: Proc. 6th Int. Conf. Big Data Comput. Commun. BigCom 2020, pp. 180–188. IEEE (2020)
14. 14\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr14"></a>Chen, R., Tu, I.-P., Chuang, K.-E., Lin, Q.-X., Liao, S.-W., Liao, W.: Endex: degree of mining power decentralization for proof-of-work based blockchain systems. IEEE Netw. **34**(6), 266–271 (2020)[Crossref](https://doi.org/10.1109/MNET.011.2000178)
15. 15\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr15"></a>Jeong, S.E.: Centralized decentralization: Does voting matter? Simple economics of the DPoS blockchain governance. [https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3575654](https://papers.ssrn.com/sol3/Papers.cfm?abstract_id=3575654) (2020)
16. 16\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr16"></a>Rebello, G.A.F., Camilo, G.F., Guimaraes, L.C., de Souza, L.A.C., Duarte, O.C.M.: Security and performance analysis of quorum-based blockchain consensus protocols. [https://www.gta.ufrj.br/ftp/gta/TechReports/RCG20c.pdf](https://www.gta.ufrj.br/ftp/gta/TechReports/RCG20c.pdf) (2020)
17. 17\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr17"></a>Li, C., Palanisamy, B.: Incentivized blockchain-based social media platforms: a case study of Steemit. In: Proc. 10th ACM Conf. Web Sci., pp. 145–154. Association for Computing Machinery, Boston (2019)
18. 18\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr18"></a>Zheng, Z., Xie, S., Dai, H., Chen, X., Wang, H.: An overview of blockchain technology: architecture, consensus, and future trends. In: Proc. 2017 IEEE Int. Congr. Big Data, pp. 557–564. IEEE, Honolulu (2017)
19. 19\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr19"></a>Khalilov, M.C.K., Levi, A.: A survey on anonymity and privacy in Bitcoin-like digital cash systems. IEEE Commun. Surv. Tutor. **20**(3), 2543–2585 (2018)[Crossref](https://doi.org/10.1109/COMST.2018.2818623)
20. 20.Wu, J., Liu, J., Chen, W., Huang, H., Zheng, Z., Zhang, Y.: Detecting mixing services via mining Bitcoin transaction network with hybrid motifs. IEEE Trans. Syst. Man Cybern. Syst. **52**(4), 2237–2249 (2021)[Crossref](https://doi.org/10.1109/TSMC.2021.3049278)
21. 21.Xia, Y., Liu, J., Wu, J.: Phishing detection on Ethereum via attributed ego-graph embedding. IEEE Trans. Circuits Syst. II Express Briefs **69**(5), 2538–2542 (2022)
22. 22\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr22"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
23. 23\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr23"></a>Durieux, T., Ferreira, J.a.F., Abreu, R., Cruz, P.: Empirical review of automated analysis tools on 47,587 Ethereum smart contracts. In: Proc. ACM/IEEE 42nd Int. Conf. Softw. Eng., pp. 530–541. Association for Computing Machinery, Seoul (2020)
24. 24.Wu, J., Liu, J., Zhao, Y., Zheng, Z.: Analysis of cryptocurrency transactions from a network perspective: an overview. J. Netw. Comput. Appl. **190**, 103139 (2021)[Crossref](https://doi.org/10.1016/j.jnca.2021.103139)
25. 25.Lin, D., Chen, J., Wu, J., Zheng, Z.: Evolution of Ethereum transaction relationships: toward understanding global driving factors from microscopic patterns. IEEE Trans. Comput. Soc. Syst. **9**(2), 559–570 (2022)[Crossref](https://doi.org/10.1109/TCSS.2021.3093384)
26. 26\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr26"></a>Liu, J., Zheng, J., Wu, J., Zheng, Z.: FA-GNN: filter and augment graph neural networks for account classification in Ethereum. IEEE Trans. Netw. Sci. Eng. **9**(4), 2579–2588 (2022)[Crossref](https://doi.org/10.1109/TNSE.2022.3166655)
27. 27\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr27"></a>Lee, S., Kim, D., Kim, D., Son, S., Kim, Y.: Who spent my EOS? On the (in)security of resource management of EOS.IO. In: Proc. 13th USENIX Work. Offensive Technol. USENIX Association, Santa Clara (2019)
28. 28\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr28"></a>Quan, L., Wu, L., Wang, H.: EVulHunter: detecting fake transfer vulnerabilities for EOSIO’s smart contracts at webassembly-level. arXiv preprint arXiv:1906.10362 (2019)
29. 29\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr29"></a>He, N., Zhang, R., Wang, H., Wu, L., Luo, X., Guo, Y., Yu, T., Jiang, X.: EOSAFE: security analysis of EOSIO smart contracts. In: Proc. 30th USENIX Secur. Symp. Virtual Conference, pp. 1271–1288. USENIX Association (2021)
30. 30\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr30"></a>Lee, D., Lee, D.H.: Push and pull: manipulating a production schedule and maximizing rewards on the EOSIO blockchain. In: Proc. Third ACM Work. Blockchains, Cryptocurrencies Contract., pp. 11–21. Association for Computing Machinery, Auckland (2019)
31. 31\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr31"></a>Zheng, W., Zheng, Z., Dai, H., Chen, X., Zheng, P.: Xblock-EOS: extracting and exploring blockchain data from EOSIO. Inf. Process. Manag. **58**(3), 102477 (2021)[Crossref](https://doi.org/10.1016/j.ipm.2020.102477)
32. 32\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr32"></a>Zhao, Y., Liu, J., Han, Q., Zheng, W., Wu, J.: Exploring EOSIO via graph characterization. In: Proc. Int. Conf. Blockchain Trust. Syst., pp. 475–488. Springer, Dali (2020)
33. 33\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr33"></a>Huang, Y., Wu, J., Ren, W., Tse, C.K., Zheng, Z.: Sequential restorations of complex networks after cascading failures. IEEE Trans. Syst. Man Cybern. Syst. **51**(1), 400–411 (2021)[Crossref](https://doi.org/10.1109/TSMC.2018.2874822)
34. 34\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr34"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding Ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. II Express Briefs **67**(11), 2737–2741 (2020)
35. 35\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr35"></a>EOSIO: EOSIO core nodeos. [https://eos.io/for-developers/build/nodeos/](https://eos.io/for-developers/build/nodeos/). Accessed 31 Jan 2021
36. 36\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr36"></a>Perc, M.: The Matthew effect in empirical data. J. R. Soc. Interface **11**(98), 20140378 (2014)[Crossref](https://doi.org/10.1098/rsif.2014.0378)
37. 37\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr37"></a>Wu, K., Peng, B., Xie, H., Huang, Z.: An information entropy method to quantify the degrees of decentralization for blockchain systems. In: Proc. 2019 IEEE Int. Conf. Electron. Inf. Emerg. Commun., pp. 1–6. IEEE, Beijing (2019)
38. 38\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr38"></a>Akoglu, L., McGlohon, M., Faloutsos, C.: Oddball: spotting anomalies in weighted graphs. In: Proc. Pacific-Asia Conf. Knowl. Discov. Data Min., pp. 410–421. Springer, Hyderabad (2010)
39. 39\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr39"></a>Blondel, V.D., Guillaume, J.-L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. J. Stat. Mech. Theory Exp. **2008**(10), P10008 (2008)[Crossref](https://doi.org/10.1088/1742-5468/2008/10/P10008)
40. 40\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr40"></a>Berman, A.: EOS developer acknowledges claims of ‘collusion’ and ‘mutual voting’ between nodes. [https://cointelegraph.com/news/eos-developer-acknowledges-claims-of-collusion-and-mutual-voting-between-nodes](https://cointelegraph.com/news/eos-developer-acknowledges-claims-of-collusion-and-mutual-voting-between-nodes) (2018)
41. 41\.<a id="oebps-html-619883_1_en_4_chapter-xhtml-cr41"></a>Wei, Y., Liang, L., Zhou, B., Feng, X.: A modified blockchain DPoS consensus algorithm based on anomaly detection and reward-punishment. In: Proc. 13th Int. Conf. Commun. Softw. Networks, pp. 283–288. IEEE, Chongqing (2021)

**Footnotes**

[1](#oebps-html-619883_1_en_4_chapter-xhtml-fn1_source)<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn1"></a>

[http://xblock.pro/](http://xblock.pro/).

[2](#oebps-html-619883_1_en_4_chapter-xhtml-fn2_source)<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn2"></a>

[https://www.alohaeos.com/vote/proxy/votetochange](https://www.alohaeos.com/vote/proxy/votetochange).

[3](#oebps-html-619883_1_en_4_chapter-xhtml-fn3_source)<a id="oebps-html-619883_1_en_4_chapter-xhtml-fn3"></a>

[https://coinmarketcap.com/currencies/eos/](https://coinmarketcap.com/currencies/eos/).

# Part IIIBlockchain Transaction Network Mining

<a id="oebps-html-619883_1_en_5_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_5](https://doi.org/10.1007/978-981-97-4430-5_5)

# 5. Account Classification Based on the Homophily-Heterophily Graph Neural Networks

Han Yang[1](#oebps-html-619883_1_en_5_chapter-xhtml-aff4) , Junyuan Fang[2](#oebps-html-619883_1_en_5_chapter-xhtml-aff5) , Jiajing Wu[1](#oebps-html-619883_1_en_5_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_5_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_5_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_5_chapter-xhtml-aff5"></a>

(2)City University of Hong Kong, Kowloon, Hong Kong

<a id="oebps-html-619883_1_en_5_chapter-xhtml-contactofauthor1"></a>

**Han Yang (Corresponding author)Email:** [yangh396@mail2.sysu.edu.cn](mailto:yangh396@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_5_chapter-xhtml-contactofauthor2"></a>

**Junyuan FangEmail:** [junyufang2-c@my.cityu.edu.hk](mailto:junyufang2-c@my.cityu.edu.hk)

<a id="oebps-html-619883_1_en_5_chapter-xhtml-contactofauthor3"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_5_chapter-xhtml-contactofauthor4"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

As the largest blockchain platform supporting smart contracts, financial crimes including scams and hacking frequently happen on Ethereum and have caused serious losses. Therefore, it is necessary to classify Ethereum accounts in order to better identify those involved in illegal transactions and analyze the behavior patterns of different classes of accounts. In this chapter, we construct an Ethereum transaction network based on transaction records and find that this network is with heterophily. However, most of the current work on account classification ignores the role of this heterophily information. We first figure out that the heterophily information of the neighborhood may also be beneficial for the final predictions. Based on this, we propose a new graph neural network (GNN) model, named BPA-GNN, which incorporates both homophilic and heterophilic information into the neighborhood aggregations. Specifically, BPA-GNN consists of three main modules including bi-path neighbor sampling, separated neighborhood aggregation, and attention-based node representation learning. Comprehensive experiments on a real Ethereum transaction dataset demonstrate the state-of-the-art performance of BPA-GNN, showing that the model can effectively extract and utilize neighborhood information to improve the distinguishability of node representations. As an effective solution for Ethereum account de-anonymization, BPA-GNN can help identify illegal activities and promote the healthy development of the Ethereum ecosystem.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec1"></a>

## 5.1 Introduction

Cryptocurrency market increasingly serves as a breeding ground for illicit and criminal activities due to the anonymity or pseudonymity of those involved in transactions. Consequently, the gradual increase in financial crimes, including phishing and money laundering, has exerted a detrimental effect on the market \[[1](#oebps-html-619883_1_en_5_chapter-xhtml-cr1)]. According to the latest crypto crime report \[[2](#oebps-html-619883_1_en_5_chapter-xhtml-cr2)] provided by a blockchain data platform named Chainalysis, illegal addresses received $20 billion from cryptocurrency-based crimes in 2022, which reached a record high. Therefore, in order to find the perpetrators and then maintain a healthy market economy environment, it is necessary to classify the accounts, i.e., account de-anonymization. Additionally, some account classes unrelated to illegal transactions, such as Exchanges and Mining pools, are also crucial to the blockchain ecosystem. Understanding the transaction characteristics of these accounts is of great importance. Consequently, besides market regulation, account classification can also help us better analyze the behavior patterns of accounts in different classes and gain a deeper insight into this market.

Specifically, in this chapter, we focus on the account classification on Ethereum. As smart contracts offer new technological avenues for phishing, money laundering, and other criminal activities, Ethereum has gradually become a platform where such illegal activities are frequent. As a result, Ethereum account classification enhances the transparency of the system, which helps preserve the financial security of the Ethereum ecosystem and further exploit this market.

Due to the openness of public blockchain data, we can easily obtain Ethereum transaction records and even trace transactions \[[3](#oebps-html-619883_1_en_5_chapter-xhtml-cr3)]. The rich Ethereum transaction records also give us the chance to classify accounts by analyzing the corresponding properties of transactions \[[4](#oebps-html-619883_1_en_5_chapter-xhtml-cr4)]. The transaction model of Ethereum is account-centric, where each transaction is associated with two accounts. Based on the transaction relationships between different accounts, we can construct the corresponding transaction network for further analysis. In this transaction network, accounts are represented as nodes, and edges indicate the transactions between accounts. Furthermore, a recent study \[[5](#oebps-html-619883_1_en_5_chapter-xhtml-cr5)] pointed out that the Ethereum transaction network is with heterophily (i.e., low homophily), indicating that nodes in this network tend to connect with nodes in different classes. Taking phishing accounts in the Ethereum transaction network as an example, as shown in Fig. [5.1](#oebps-html-619883_1_en_5_chapter-xhtml-fig1). In brief, phishing accounts are those involved in phishing scams, exchange accounts are intermediaries for making transactions between fiat currencies and cryptocurrencies, and ordinary accounts are those controlled by ordinary investors with normal transaction behaviors. It can be observed that phishing accounts tend to establish connections with exchange accounts and ordinary accounts more frequently than with other phishing accounts.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fig1"></a>

***Fig. 5.1***

A common local transaction (i.e., neighborhood) pattern example in the Ethereum transaction network, where accounts have the disposition to connect with accounts belonging to other classes

Recently, graph neural networks (GNNs) have demonstrated remarkable success in various graph-related tasks, including node classification and link prediction. Therefore, we choose the GNN-based methods to address the Ethereum account classification task. There are already some GNN-based methods \[[5](#oebps-html-619883_1_en_5_chapter-xhtml-cr5)–[11](#oebps-html-619883_1_en_5_chapter-xhtml-cr11)] focusing on classifying Ethereum accounts. However, they fail to solve the following issues. Firstly, most existing methods are designed based on GNNs under the homophily assumption without taking into account the heterophily property of the Ethereum transaction network. However, the message-passing mechanism of GNNs designed for homophilic networks is not well-suited for heterophilic networks. This is because it tends to make the representations of neighboring nodes more similar, leading to unsatisfactory prediction performance on such networks. Secondly, the key idea of the very few GNN-based methods considering heterophily is generally how to get the homophilic information from the neighborhood while ignoring the heterophilic information. However, incorporating heterophilic information could also help enhance the prediction performance of models. For example, as shown in Fig. [5.1](#oebps-html-619883_1_en_5_chapter-xhtml-fig1), if two ordinary accounts are connected to the same phishing account, it indicates that they tend to have more similar behavior patterns. Meanwhile, the behavior patterns between ordinary accounts and phishing accounts are usually quite different, which can be considered as heterophilic features. Hence, to utilize all effective feature information instead of directly discarding the heterophilic features, we would like to combine such information to further enhance the prediction performance of GNN-based methods.

To address the limitations mentioned above, in this work, we propose a novel GNN-based Ethereum account classification model named Bi-path Aware Graph Neural Network (BPA-GNN). Specifically, the proposed BPA-GNN has the following three modules. Firstly, we propose a bi-path sampling module that samples neighbors with similar or dissimilar features separately by calculating the feature similarity of connected node pairs. This approach aims to preserve corresponding homophilic or heterophilic neighborhood information. Especially in the path of heterophilic neighbor sampling, we incorporate a penalty mechanism to prevent large-degree nodes from disturbing effective information extraction. Then, in the neighborhood aggregation module, we aggregate similar and dissimilar neighbors separately. Finally, we utilize an attention-based node representation learning module combining both homophilic and heterophilic neighborhood representations with raw features to obtain the final predictions.

To sum up, the major contributions of this work are as follows:

- We solve the Ethereum account classification problem by considering the heterophily of the Ethereum transaction network. Particularly, besides the homophilic information between connected nodes, we figure out that heterophilic information can also help improve the prediction performance of models.
- We propose a novel GNN-based Ethereum account classification model, BPA-GNN, that considers both homophilic and heterophilic information. By aggregating these two kinds of information separately, BPA-GNN can well retain the characteristics of nodes rather than ignore the heterophilic information of neighbors.
- We conduct extensive experiments on a real Ethereum transaction dataset to compare the proposed BPA-GNN with state-of-the-art models, demonstrating the superiority of our model.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec2"></a>

## 5.2 Preliminaries

In this section, we first introduce some preliminaries related to the main used notations and graph neural networks. Then, the definition of homophily and heterophily will be given.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec3"></a>

### 5.2.1 Notations

We can construct the Ethereum transaction network as an undirected and unweighted graph \$$G=\\left ( V, E \\right ) $$, where nodes and edges represent accounts and transactions, respectively. Specifically, \$$V=\\left \\{ v\_{1},...,v_{n} \\right \\} $$ is the set of *N* nodes and \$$E\\subseteq \\left \\{ (v\_{i}, v\_{j}) \\mid v\_{i}, v_{j} \\in V\\right \\} $$ is the set of *M* edges. Moreover, \$\$A \\in \\left \\{ 0,1\\right \\} ^{N \\times N}\$$ is the adjacent matrix of *G*, where \$\$A_{ij}=1\$$ if \$\$\\left (v\_{i},v_{j}\\right ) \\in E\$$, otherwise \$\$A_{ij}=0\$$. \$$X \\in \\mathbb {R}^{N\\times d} $$ is the feature matrix where the *i*-th row \$\$x_{i}\$$ means the feature of node \$\$v_{i}\$$ and *d* is the feature dimension. \$\$Y \\in \\left \\{ 0,1 \\right \\} ^{N \\times C}\$$ is the label matrix and *C* is the number of label classes. We summarize the main notations used in this chapter in Table [5.1](#oebps-html-619883_1_en_5_chapter-xhtml-tab1). <a id="oebps-html-619883_1_en_5_chapter-xhtml-tab1"></a>

***Table 5.1***

Main notations used in this chapter

| Symbol | Definition |
| --- | --- |
| *G* | Graph |
| *V* | Node set |
| *E* | Edge set |
| *N*, *M* | The number of nodes, the number of edges |
| \$\$N(v_{i})\$$ | 1-Hop neighborhood of node \$\$v_{i}\$$ |
| *A* | Adjacent matrix |
| *X*, \$\$x_{i}\$$ | Node feature matrix, feature vector of node \$\$v_{i}\$$ |
| *Y* , \$\$y_{i}\$$, \$\$\\hat {y_{i}}\$$ | Label matrix, label of node \$\$v_{i}\$$, predicted label of node \$\$v_{i}\$$ |
| \$\$S(v_{i})\$$ | Sampled 1-hop homophilic neighbors of node \$\$v_{i}\$$ |
| \$\$D(v_{i})\$$ | Sampled 1-hop heterophilic neighbors of node \$\$v_{i}\$$ |
| \$$\\lambda $$ | Sampling rate |
| *K*, *k* | Total number of aggregation layers, layer number |
| \$\$h_{s,i}^{k}\$$ | Homophilic representation of node \$\$v_{i}\$$ at layer *k* |
| \$\$h_{d,i}^{k}\$$ | Heterophilic representation of node \$\$v_{i}\$$ at layer *k* |
| \$\$h_{i}^{\\mathrm {combine}}\$$ | Combined representation of node \$\$v_{i}\$$ |
| \$$\\alpha $$ | Attention coefficients |

As we mentioned before, in this chapter, the account classification problem can be transformed into a semi-supervised node classification task. Specifically, given a training set \$\$V_{train} \\subset V\$$ with known labels, our goal is to predict the label of nodes in \$\$V\_{test} \\subseteq V \\setminus V_{train}\$$.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec4"></a>

### 5.2.2 Graph Neural Networks

Generally, GNNs follow the message passing mechanism \[[12](#oebps-html-619883_1_en_5_chapter-xhtml-cr12)], or, in other words, neighborhood aggregations. In each propagation layer, each node aggregates the messages from its local neighbors first and then updates the latest representation by combining its own message and neighbored messages. The above process can be simply expressed as follows.

\$$\\displaystyle \\begin{aligned} a^{k+1}\_{i} = \\mathrm{AGGREGATE}\\left ( \\left \\{ h\_{j}^{k} \\mid v\_{j} \\in N(v_{i})\\right \\} \\right ) , \\end{aligned} $$

(5.1)

\$$\\displaystyle \\begin{aligned} h\_{i}^{k+1} = \\mathrm{COMBINE}(h\_{i}^{k}, a_{i}^{k+1}), \\end{aligned} $$

(5.2)

where \$\$N(v\_{i})=\\left \\{ v\_{j}\\mid \\left (v\_{i},v_{j}\\right )\\in E \\right \\}\$$ means the 1-hop neighbors of node \$\$v_{i}\$$, \$\$h_{i}^{k}\$$ means the representation of \$\$v_{i}\$$ at the *k*-th layer, and \$\$h\_{i}^{0} =x_{i}\$$ particularly. Moreover, \$$\\mathrm {AGGREGATE}\\left ( \\cdot \\right ) $$ is the function aggregating all the neighbors’ representations for each node, such as \$\$\\mathrm {Mean}(\\cdot )\$$, and \$\$a_{i}^{k+1}\$$ denotes the information aggregated from the neighbors of \$\$v_{i}\$$ at the layer \$\$k+1\$$. Finally, a \$$\\mathrm {COMBINE}\\left ( \\cdot \\right ) $$ function is used to combine each node’s ego- and neighbor-representations, such as \$\$\\mathrm {Mean}(\\cdot )\$$ and \$\$\\mathrm {Concat}(\\cdot )\$$.

Taking the classic graph convolutional network (GCN) \[[13](#oebps-html-619883_1_en_5_chapter-xhtml-cr13)] as an example, the formulation used to update representations at each layer in GCN can be denoted as follows. <a id="oebps-html-619883_1_en_5_chapter-xhtml-equ3"></a>

\$$\\displaystyle \\begin{aligned} h\_{i}^{k+1} = \\sigma (\\sum\_{v\_{j} \\in \\hat{N}(v\_{i}) }\\frac{1}{\\sqrt{|\\hat{N}(v\_{i})|\\cdot |\\hat{N}(v\_{j})|} }h_{j}^{k}W^{k}), {} \\end{aligned} $$

(5.3)

where \$\$\\hat {N}(v\_{i})=N(v\_{i}) \\cup v_{i}\$$, \$\$W^{k}\$$ is a learnable weight matrix, and \$$\\sigma $$ is a nonlinear activation function (e.g., ReLU). If we consider all nodes in the network, Eq. [5.3](#oebps-html-619883_1_en_5_chapter-xhtml-equ3) can be further expressed as follows.

\$$\\displaystyle \\begin{aligned} H^{k+1} = \\sigma (\\hat{A}H^{k}W^{k}), \\end{aligned} $$

(5.4)

where \$\$H^{k}\$$ is the node representation matrix at the *k*-th layer. The normalized adjacent matrix with self-loops is denoted as \$\$\\hat {A} = \\tilde {D}^{-\\frac {1}{2} } (A+I_{N}) \\tilde {D}^{-\\frac {1}{2} }\$$ with the degree matrix \$\$\\tilde {D}\_{ii}=\\sum \_{j} {(A+I\_{N})}_{ij}\$$.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec5"></a>

### 5.2.3 Homophily and Heterophily of Networks

A network with high homophily/heterophily means nodes in this network tend to connect to nodes belonging to the same/different classes. In this chapter, we use the two most popular homophily ratio measurements, edge homophily ratio \[[14](#oebps-html-619883_1_en_5_chapter-xhtml-cr14)] and node homophily ratio \[[15](#oebps-html-619883_1_en_5_chapter-xhtml-cr15)], to measure the homophily of networks, which are denoted as follows.

\$$\\displaystyle \\begin{aligned} \\mathcal{H} \_{edge} = \\frac{1}{M} \\left | \\left \\{ \\left ( v\_{i},v\_{j} \\right ) \\mid \\left ( v\_{i},v\_{j} \\right ) \\in E \\wedge y\_{i}=y_{j} \\right \\} \\right | , \\end{aligned} $$

(5.5)

\$$\\displaystyle \\begin{aligned} \\mathcal{H} \_{node} = \\frac{1}{N} \\sum\_{v\_{i}\\in V}\\frac{\\left | \\left \\{ v\_{j} \\mid v\_{j} \\in N\\left ( v\_{i} \\right ) \\wedge y\_{i}=y\_{j} \\right \\} \\right | }{\\left | N\\left ( v_{i}\\right ) \\right | } . \\end{aligned} $$

(5.6)

The ranges of the above two kinds of homophily ratios are both from 0 to 1. The closer the ratios are to 1, the lower heterophily the corresponding network has. On the contrary, a network shows strong heterophily if these two ratios are closer to 0.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec6"></a>

## 5.3 Related Work

In this section, we first introduce the classic works on graph representation learning. Then we review previous works on graph neural networks under heterophily and account classification on Ethereum in brief.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec7"></a>

### 5.3.1 Graph Representation Learning

Graph representation learning has emerged as a popular research field in recent years, demonstrating significant potential across various domains. Specifically, the main goal of graph representation learning is to transform graph-structured data into low-dimensional representation vectors, which mainly includes the following two categories of methods, namely graph embedding and graph neural networks (GNNs). Graph embedding focuses on learning the embedding vector of nodes, subgraphs, or the whole graph, and then applying the learned vectors to traditional machine-learning models for final predictions. For example, Perozzi et al. \[[16](#oebps-html-619883_1_en_5_chapter-xhtml-cr16)] proposed DeepWalk by combining the random walk mechanism on graphs with the skip-gram model \[[17](#oebps-html-619883_1_en_5_chapter-xhtml-cr17)] to learn node embeddings. Grover and Leskovec further presented node2vec \[[18](#oebps-html-619883_1_en_5_chapter-xhtml-cr18)], which designed a biased random walk procedure considering both breadth-first search and depth-first search strategies. Besides, Tang et al. \[[19](#oebps-html-619883_1_en_5_chapter-xhtml-cr19)] developed an effective embedding method named LINE via retaining first- and second-order proximity information, which can be employed in large-scale networks. Nevertheless, as the learned representation vectors still require integration with machine-learning models for final predictions, graph embedding methods cannot enhance the quality of the vectors based on feedback from machine-learning models. Differing from traditional graph embedding methods, GNNs have been proposed by taking the graph data as input and directly outputting the prediction results in an end-to-end mechanism. Specifically, Kipf and Welling \[[13](#oebps-html-619883_1_en_5_chapter-xhtml-cr13)] proposed the graph convolutional network (i.e., GCN) by utilizing a localized first-order approximation to simplify the graph convolution process. Hamilton et al. \[[20](#oebps-html-619883_1_en_5_chapter-xhtml-cr20)] proposed GraphSAGE by first sampling neighbors of the target nodes and then aggregating information across the sampled subgraph, aiming at employing this model in large-scale graphs. Velickovic et al. introduced graph attention network (i.e., GAT) \[[21](#oebps-html-619883_1_en_5_chapter-xhtml-cr21)] by incorporating the attention mechanism into the propagation process, which can adaptively assign weights to neighbors. Moreover, Wu et al. \[[22](#oebps-html-619883_1_en_5_chapter-xhtml-cr22)] reduced the complexity of the original GCNs by removing the nonlinearities between GCN layers and transforming multiple layers of linear transformations into a single transformation.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec8"></a>

### 5.3.2 Graph Neural Networks Under Heterophily

Classic GNNs, such as GCN and GAT, are designed under the homophily assumption where the connected node pairs have similar features. As a result, these homophilic GNNs usually cannot achieve satisfactory performance on heterophilic networks. In recent years, some researchers start turning their attention to GNNs under heterophily. Based on a recent study \[[23](#oebps-html-619883_1_en_5_chapter-xhtml-cr23)], current heterophilic GNNs can be commonly divided into two classes including neighbor extension and GNN architecture refinement.

For neighbor extensions, Abu-El-Haija et al. \[[24](#oebps-html-619883_1_en_5_chapter-xhtml-cr24)] proposed MixHop, which used the power operation to aggregate neighbors in different hops. H2GCN \[[14](#oebps-html-619883_1_en_5_chapter-xhtml-cr14)], proposed by Zhu et al., also mixed higher-hop neighbors in each GNN layer. Besides aggregating neighbors from higher hops as traditional GNNs do, a few studies also try to break the wall of local aggregations by exploring potential neighbors among the whole graph. For example, Pei et al. \[[15](#oebps-html-619883_1_en_5_chapter-xhtml-cr15)] proposed a novel aggregation scheme that not only aggregated original local neighbors but also aggregated new neighbors in the latent space obtained based on the similarity of nodes. Liu et al. \[[25](#oebps-html-619883_1_en_5_chapter-xhtml-cr25)] proposed NLGNN by sorting all nodes in the graph based on the attention scores and further aggregating nodes with close scores. Wang et al. \[[26](#oebps-html-619883_1_en_5_chapter-xhtml-cr26)] applied the homophily degree matrix denoting the probability of the nodes belonging to the same class to guide the graph convolution process. Moreover, a few works attempt to restructure the graphs to decrease the level of heterophily. Huang et al. \[[27](#oebps-html-619883_1_en_5_chapter-xhtml-cr27)] trained a binary classifier to predict whether each edge is homophilic or heterophilic and deleted heterophilic edges from the graphs. Bi et al. \[[28](#oebps-html-619883_1_en_5_chapter-xhtml-cr28)] proposed a method termed DHGR to rewire the graphs by removing and adding edges according to the similarity of node pairs’ label-distribution and feature-distribution.

Moreover, there are other works focusing on refining the GNN architecture. Bo et al. \[[29](#oebps-html-619883_1_en_5_chapter-xhtml-cr29)] proposed FAGCN with a shared self-gating mechanism to adaptively aggregate low-frequency and high-frequency signals from the spectral domain. Chien et al. \[[30](#oebps-html-619883_1_en_5_chapter-xhtml-cr30)] adopted the generalized PageRank technique to learn weights for combining intermediate representations. Jin et al. \[[31](#oebps-html-619883_1_en_5_chapter-xhtml-cr31)] and Sun et al. \[[32](#oebps-html-619883_1_en_5_chapter-xhtml-cr32)] both integrated random walk sampling strategies into basic GNNs, and further proposed novel path-based aggregation mechanisms.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec9"></a>

### 5.3.3 Account Classification on Ethereum

For account classification on Ethereum, the early works can be divided into two categories including manual feature engineering methods and graph representation learning methods. Manual feature engineering is highly related to the quality of manual-designed features, requiring corresponding domain knowledge and expert experience. Kumar et al. \[[33](#oebps-html-619883_1_en_5_chapter-xhtml-cr33)] adopted an information gain algorithm to select features for EOAs and smart contract accounts, and then used four machine learning classifiers to classify malicious addresses. Chen et al. \[[34](#oebps-html-619883_1_en_5_chapter-xhtml-cr34)] proposed a graph-based cascade feature extraction method to extract ego and neighbor features, then developed a lightGBM-based classifier to detect phishing nodes.

For the methods belonging to the graph representation learning category, Wu et al. \[[35](#oebps-html-619883_1_en_5_chapter-xhtml-cr35)] proposed Trans2vec via biased random walks, an improved framework of node2vec \[[18](#oebps-html-619883_1_en_5_chapter-xhtml-cr18)], to learn node embeddings in the Ethereum transaction network. Wang et al. \[[36](#oebps-html-619883_1_en_5_chapter-xhtml-cr36)] proposed a heterogeneous network embedding method with random walks on the meta-path. Besides graph embedding methods via random walks, recent studies also utilize GNNs to solve the account classification task on Ethereum. For example, Yu et al. \[[6](#oebps-html-619883_1_en_5_chapter-xhtml-cr6)] utilized a 3-layer GCN model to detect the Ponzi scheme on Ethereum. Liu et al. \[[7](#oebps-html-619883_1_en_5_chapter-xhtml-cr7)] proposed a GCN-based model combining network features such as transaction density and asymmetric proximity to infer the identities on Ethereum. Yu et al. \[[8](#oebps-html-619883_1_en_5_chapter-xhtml-cr8)] proposed MP-GCN by using the message passing mechanism to learn node embeddings containing the information of both network topologies and node features. Moreover, Liu et al. \[[5](#oebps-html-619883_1_en_5_chapter-xhtml-cr5)] took heterophily into consideration and further introduced FA-GNN to tackle the account classification problem by utilizing a GNN-based framework with neighbor filtering and feature augmentation components. Also considering heterophily, Huang et al. \[[11](#oebps-html-619883_1_en_5_chapter-xhtml-cr11)] proposed EH-GCN, not only aggregating first-order neighborhood information but also obtaining higher-order similar neighborhood information by a network-based sampling strategy. Except for the above studies focusing on the view of nodes, some works have been proposed to solve the account classification task from the perspective of graph classification. Shen et al. \[[37](#oebps-html-619883_1_en_5_chapter-xhtml-cr37)] presented a GCN-based model to classify subgraphs that were sampled based on total transaction volume between node pairs. Zhou et al. \[[10](#oebps-html-619883_1_en_5_chapter-xhtml-cr10)] sampled subgraphs based on edge attributes including transaction amount and times, and then utilized a GNN-based model with an attention mechanism to achieve the subgraph classification.

Though many methods have been proposed to solve the account classification task on Ethereum, most of them ignore the positive impact of the heterophilic neighborhood information. Therefore, in this work, we propose a bi-path neighbor sampling method to retain the information of both homophilic and heterophilic neighbors and verify the effect of heterophilic information.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec10"></a>

## 5.4 Methodology of Account Classification

In this section, we propose a GNN-based model, BPA-GNN, that jointly makes use of homophilic and heterophilic information in the neighborhood. As shown in Fig. [5.2](#oebps-html-619883_1_en_5_chapter-xhtml-fig2), the BPA-GNN model is primarily composed of three modules. (1) A bi-path neighbor sampling module in which the homophilic and heterophilic neighbors of the target node are sampled separately. (2) A separated neighborhood aggregation module that aggregates messages from the sampled homophilic and heterophilic neighbors separately. (3) An attention-based node representation learning module that adopts a shared self-gating mechanism to learn attention weights for combining different parts of representations of neighbors. Then this module obtains the final prediction for each node via a two-layer fully connected neural network. In the following, we will present the details of each module.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fig2"></a>

***Fig. 5.2***

The overall framework of BPA-GNN

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec11"></a>

### 5.4.1 Bi-path Neighbor Sampling

Since the constructed Ethereum transaction network is an extremely large-scale network, we adopt the neighbor sampling mechanism to reduce the consumption of aggregation on exponentially expanding neighborhoods and retain more effective information at the same time.

Intuitively, intra-class nodes are more similar, which results in a higher feature similarity among them. In contrast, inter-class nodes are more likely to show lower feature similarity. Under this assumption, we first use the Euclidean distance metric to measure the feature similarity of connected node pairs, determining their relationship as homophilic or heterophilic based on these similarity values. Specifically, a higher Euclidean distance between two feature vectors suggests lower feature similarity, indicating a heterophilic relationship between the two nodes, and the reverse implies a homophilic relationship. As we want to retain both homophilic and heterophilic information in the neighborhood of nodes, we propose a bi-path neighbor sampling module. This module independently samples neighbors with similar and dissimilar features (i.e., homophilic and heterophilic neighbors) for each node based on the measured feature similarity.

Specifically, for each node \$\$v_{i}\$$ in \$$ V\$$, we first calculate the Euclidean distance between feature vectors of \$\$v_{i}\$$ and each node in its 1-hop neighborhood. In the path of homophilic neighbor sampling, we rank the distance list from small to large. Based on a given sampling rate \$$\\lambda $$, we only retain the top \$$\\left \\lceil \\lambda \\left | N(v_{i}) \\right | \\right \\rceil $$ neighbors with the smallest distance as \$\$S(v_{i})\$$. The above sampling operation can be expressed as follows.

\$$\\displaystyle \\begin{aligned} S\\left ( v\_{i} \\right ) = \\left \\{ v\_{j} \\mid v\_{j} \\in MinDisK\\left (v\_{i}, N(v\_{i}) , \\left \\lceil \\lambda \\left | N(v_{i}) \\right | \\right \\rceil \\right ) \\right \\}, {} \\end{aligned} $$

(5.7)

where \$\$MinDisK(v,s,k)\$$ is a function that returns the nodes in set *s* with the minimum *k* Euclidean distance values to target node *v*.

Similarly, in the path of heterophilic neighbor sampling, we also rank the calculated distance list, but from an opposite direction (i.e., from large to small). Meanwhile, we find that some large-degree nodes are repeatedly sampled by nodes in different classes, probably because they connect to lots of nodes in different classes and their attributes differ from those nodes. Our experiments show that such sampling results indeed reduce the distinguishability of the sampled information among the nodes in different classes. Hence, to maintain the distinguishability of the sampled neighbors and mitigate the adverse effects of large-degree nodes, we further introduce a large-degree penalty mechanism into this sampling path. In general, for each node, we get its heterophilic neighbors and then use the large-degree penalty mechanism among them to obtain more effective heterophilic neighbors. For the specific implementation, we first sample 50% of neighbors with the largest distance. Then we reorder these sampled neighbors based on their degrees in an ascending order to get a new neighbor list. In this new list, we finally retain the \$$\\left \\lceil \\lambda \\left | N(v_{i}) \\right | \\right \\rceil $$ neighbors with the smallest degree as \$\$D(v_{i})\$$ based on a given sampling rate \$$\\lambda $$. By employing the above operation, the sampled neighbors can not only retain the heterophilic information but also avoid the negative influence of the nodes with extremely large degree values. The above operation can be further denoted as follows.

\$$\\displaystyle \\begin{aligned} \\begin{array}{l} D(v\_{i})=\\left \\{ v\_{j} \\mid v\_{j} \\in MinDegK\\left (N'(v\_{i}) , \\left \\lceil \\lambda \\left | N(v\_{i}) \\right |\\right \\rceil \\right ) \\right \\}, \\\\ {}  s.t.N'(v\_{i})=\\left \\{ v\_{j} \\mid v\_{j} \\in MaxDisK\\left (v\_{i}, N(v\_{i}) , \\left \\lceil \\frac{\\left | N(v_{i}) \\right |}{2}\\right \\rceil \\right ) \\right \\}, \\end{array} {} \\end{aligned} $$

(5.8)

where \$\$MaxDisK(v,s,k)\$$ is a function that returns the nodes in set *s* with the maximum *k* Euclidean distance values to target node *v*, and \$\$MinDegK(s,k)\$$ is a function that returns the nodes in set *s* with the minimum *k* degree values.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec12"></a>

### 5.4.2 Separated Neighborhood Aggregation

We then propose a neighborhood aggregation module that separately aggregates homophilic and heterophilic neighbors based on previous sampling results. We refer to the idea that “*the enemy of my enemy is my friend, and the friend of my friend is also my friend*” from a previous study \[[38](#oebps-html-619883_1_en_5_chapter-xhtml-cr38)]. Specifically, when aggregating information from homophilic neighbors, we utilize their homophilic representations at the previous layer to update the homophilic representation of the target node. However, when aggregating information from heterophilic neighbors, we also use their homophilic representations at the previous layer to update the heterophilic representation of the target node, rather than using their heterophilic representations, for the following reasons. Based on the assumption of “*the enemy of my enemy is my friend*”, if we update the heterophilic representation of the target node by using the heterophilic representations of its neighbors at the previous layer, we will actually aggregate the homophilic information of the target node. Therefore, when aggregating the information from the heterophilic neighbors, we use their homophilic representations to get the information from “*the friend of my enemy*” instead. The above aggregation process can be formally written as follows.

\$$\\displaystyle \\begin{aligned} {a\_{s,i}^{k+1}}=\\sum\_{v\_{j}\\in S(v\_{i})}\\frac{1}{\\sqrt{\\left | S(v\_{i}) \\right |\\cdot\\left | S(v\_{j}) \\right | } } h_{s,j}^{k}, {} \\end{aligned} $$

(5.9)

\$$\\displaystyle \\begin{aligned} a\_{d,i}^{k+1}=\\sum\_{v\_{j}\\in D(v\_{i})}\\frac{1}{\\sqrt{\\left | D(v\_{i}) \\right |\\cdot\\left | D(v\_{j}) \\right | } } h_{s,j}^{k}, {} \\end{aligned} $$

(5.10)

where \$\$h_{s,i}^{k}\$$ and \$\$h_{d,i}^{k}\$$ mean the homophilic and heterophilic representations of node \$\$v_{i}\$$ at layer *k*, respectively. \$\${a_{s,i}^{k+1}}\$$ and \$\$a_{d,i}^{k+1}\$$ mean the homophilic and heterophilic information aggregating from the neighborhood of node \$\$v_{i}\$$ at layer \$\$k+1\$$, respectively. Particularly, we set \$\$h\_{s,i}^{0} = h\_{d,i}^{0} = x_{i}\$$. We utilize the normalization method in GCN while removing the self-loops in the adjacent matrix. To further separate the information of the target node and its neighbors, we adopt the ego- and neighbor-embedding separation design \[[14](#oebps-html-619883_1_en_5_chapter-xhtml-cr14)]. Therefore, to avoid the exponential growth of dimension when the number of layers increases, we further utilize linear layers to reduce the dimension of node representations, which is as follows.

\$$\\displaystyle \\begin{aligned} h\_{s,i}^{k+1} = \\mathrm{ReLU}(\\left \[ h\_{s,i}^{k}\\parallel a\_{s,i}^{k+1} \\right ] W_{s}^{k}), {} \\end{aligned} $$

(5.11)

\$$\\displaystyle \\begin{aligned} h\_{d,i}^{k+1} = \\mathrm{ReLU}(\\left \[ h\_{d,i}^{k}\\parallel a\_{d,i}^{k+1} \\right ] W_{d}^{k}), {} \\end{aligned} $$

(5.12)

where \$$\\parallel $$ is the concatenation operation. \$\$W_{s}^{k}\$$ and \$\$W_{d}^{k}\$$ denote the learning parameters of the two linear transformations.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec13"></a>

### 5.4.3 Attention-Based Node Representation Learning

After the separated neighborhood aggregation process, we finally adopt an attention mechanism to combine the homophilic and heterophilic information in the neighborhood to determine their importance to each node. Meanwhile, we also concatenate the raw features to well retain the ego information of nodes, which can be expressed as follows. <a id="oebps-html-619883_1_en_5_chapter-xhtml-equ13"></a>

\$$\\displaystyle \\begin{aligned} h\_{i}^{\\mathrm{combine}} = \\left \[ x\_{i}\\parallel \\alpha\_{s,i}h\_{s,i}^{K}+ \\alpha\_{d,i}h_{d,i}^{K} \\right ], {} \\end{aligned} $$

(5.13)

where \$\$h_{i}^{\\mathrm {combine}}\$$ means the combined representation of node \$\$v_{i}\$$ consisting of its raw feature, homophilic representation, and heterophilic representation. \$\$\\alpha _{s,i}\$$ and \$\$\\alpha _{d,i}\$$ are attention weights to be optimized, and *K* is the total number of aggregation layers.

Instead of training the two weight coefficients \$\$\\alpha _{s,i}\$$ and \$\$\\alpha _{d,i}\$$ independently, we further employ a system of linear equations together with a shared self-gating mechanism to better learn them jointly following a previous study \[[29](#oebps-html-619883_1_en_5_chapter-xhtml-cr29)]. The employed attention mechanism can be denoted as follows.

\$$\\displaystyle \\begin{aligned} \\left\\{\\begin{matrix} \\alpha\_{s,i}+\\alpha\_{d,i}=1 \\\\ \\alpha\_{s,i}-\\alpha\_{d,i}=\\alpha_{g,i} \\end{matrix}\\right., {} \\end{aligned} $$

(5.14)

\$$\\displaystyle \\begin{aligned} \\alpha\_{g,i}=tanh(p^{T}\\left \[ h\_{s,i}^{K}\\parallel h_{d,i}^{K} \\right ] ), {} \\end{aligned} $$

(5.15)

where \$\$\\alpha _{g,i}\$$ measures the importance of homophilic and heterophilic information. \$\$\\alpha _{g,i} &amp;gt; 0\$$ means that the homophilic information is more helpful to node representations and vice versa. *p* is a learnable parameter vector and \$\$tanh(\\cdot )\$$ is a hyperbolic tangent function producing a value ranging from \$\$-\$$1 to 1. Therefore, by optimizing \$\$\\alpha _{g,i}\$$, we can obtain the two attention weights via the following.

\$$\\displaystyle \\begin{aligned} \\alpha\_{s,i}=\\frac{1+\\alpha_{g,i}}{2}, {} \\end{aligned} $$

(5.16)

\$$\\displaystyle \\begin{aligned} \\alpha\_{d,i}=\\frac{1-\\alpha_{g,i}}{2}. {} \\end{aligned} $$

(5.17)

At last, we use the combined node representations as the input of a two-layer fully connected neural network to obtain the label predictions.

\$$\\displaystyle \\begin{aligned} \\hat{y\_{i}} = \\mathrm{LogSoftmax}(\\mathrm{ReLU}(h_{i}^{\\mathrm{combine}}W^{0})W^{1}), \\end{aligned} $$

(5.18)

where \$\$\\hat {y_{i}}\$$ is the label prediction of node \$\$v_{i}\$$. \$\$W^{0}\$$ and \$\$W^{1}\$$ are the learnable parameters. We optimize our model with the cross-entropy loss function.

The detailed pipeline of our proposed model is given in Algorithm [2](#oebps-html-619883_1_en_5_chapter-xhtml-fpar1). Firstly, we sample the homophilic and heterophilic neighbors for each node, respectively. Secondly, for each node, we aggregate homophilic and heterophilic information in the neighborhood and update the corresponding node representations separately. Thirdly, we calculate the attention weights for homophilic and heterophilic representations and further combine them with the raw features via concatenation. Finally, we utilize a two-layer neural network to learn the final predictions. In addition, we analyze the space complexity of our model, i.e., the total number of parameters in our model. The number of parameters in the separated neighborhood aggregation is \$$\\mathcal {O} \\left ( 4Kd^{2} \\right ) $$, where K and d represent the total number of aggregation layers and the dimension of node features, respectively. And the number of parameters in the final two-layer neural network is \$$\\mathcal {O} \\left ( 3d^{2} \\right ) $$, where we set the hidden dimension and output dimension to feature dimension *d* for simplicity. Hence, the total space complexity of BPA-GNN is \$$\\mathcal {O} \\left (4Kd^{2}+ 3d^{2} \\right ) $$.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-fpar1"></a>

**Algorithm 2 BPA-GNN model**

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec14"></a>

## 5.5 Experiments of Account Classification

In this section, the details of the Ethereum transaction dataset, baseline methods for comparison, and implementation details are introduced. Experiments on the node classification task are then conducted to demonstrate the superior performance of BPA-GNN.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec15"></a>

### 5.5.1 Experimental Settings

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec16"></a>

#### 5.5.1.1 Ethereum Transaction Dataset

We conduct the experiments on an Ethereum transaction dataset for account classification \[[11](#oebps-html-619883_1_en_5_chapter-xhtml-cr11)] from the XBlock website.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fn1_source"></a>[1](#oebps-html-619883_1_en_5_chapter-xhtml-fn1) As shown in Table [5.2](#oebps-html-619883_1_en_5_chapter-xhtml-tab2), this dataset contains 1,402,220 nodes and 2,815,028 edges in total. Among all nodes, 816 nodes have a ground-truth label and can be further classified into 6 classes of accounts, including 139 Converter, 171 Exchange, 27 Gambling, 167 ICO, 60 Mining, and 252 Phish/Hack. Moreover, each node has 12 features, such as transaction amount, account balance, and frequency of transactions. To estimate the homophily level of the Ethereum transaction network, we extract a vertex-induced subgraph by retaining all labeled nodes and the edges between them. Then, we calculate the edge homophily ratio and node homophily ratio based on this subgraph. As a result, the edge homophily ratio of the subgraph is about 0.28 and the node homophily ratio is about 0.21. Therefore, just like seeing a world with a grain of sand, we can infer that the whole Ethereum transaction network tends to be a network with high heterophily. <a id="oebps-html-619883_1_en_5_chapter-xhtml-tab2"></a>

***Table 5.2***

Ethereum dataset statistics

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec17"></a>

#### 5.5.1.2 Baselines for Comparison

To evaluate the superiority of the proposed BPA-GNN, we compare our method with the following representative methods and state-of-the-art GNNs under homophily or heterophily.

- MLP \[[39](#oebps-html-619883_1_en_5_chapter-xhtml-cr39)]: Multi-layer perceptron is a fully connected multi-layer neural network. MLP only makes use of feature information and does not use any graph structure information.
- GCN \[[13](#oebps-html-619883_1_en_5_chapter-xhtml-cr13)]: GCN is one of the most popular graph neural networks, which utilizes a localized first-order approximation to simplify the convolution process. In GCN, each node will aggregate the information from its local neighborhood layer by layer.
- GAT \[[21](#oebps-html-619883_1_en_5_chapter-xhtml-cr21)]: GAT is an attention-based graph neural network that adaptively assigns different weights to different neighbors of the target node during neighborhood aggregation.
- GraphSAGE \[[20](#oebps-html-619883_1_en_5_chapter-xhtml-cr20)]: GraphSAGE is an inductive graph neural network that samples local neighbors of nodes, then aggregates information from the sampled neighbors with improved aggregators, such as Mean, LSTM, and Pooling. Finally, GraphSAGE concatenates the current representation of nodes with the aggregated neighborhood information.
- LINKX \[[40](#oebps-html-619883_1_en_5_chapter-xhtml-cr40)]: LINKX is a simple yet effective heterophilic model for large-scale networks that firstly applies two MLPs to learn feature information and adjacency information separately, then combines them via a concatenation operator and skip connections, and finally uses another MLP to make predictions.
- NLGNN \[[25](#oebps-html-619883_1_en_5_chapter-xhtml-cr25)]: NLGNN is a heterophilic graph neural network with a non-local aggregation framework that first sorts all nodes in the graph with the scores obtained by the attention mechanism, and then only aggregates the nodes with similar scores. We choose two variants of NLGNN with different node embedding methods including MLP and GCN, which are denoted as NLMLP and NLGCN, respectively.
- FAGCN \[[29](#oebps-html-619883_1_en_5_chapter-xhtml-cr29)]: FAGCN is another heterophilic graph neural network with a shared self-gating mechanism to adaptively aggregate low-frequency and high-frequency signals from the neighborhood of the target node.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec18"></a>

#### 5.5.1.3 Implementation Details

For the dataset, nodes in each class are divided into 70%, 10%, and 20% for training, validation, and testing, respectively. Additionally, the node features are normalized. We adopt Adam \[[41](#oebps-html-619883_1_en_5_chapter-xhtml-cr41)] as the optimization method. For all methods, we set the hidden dimension to 128, the dropout ratio to 0.5, and the learning rate to 0.01. For GAT, we set the attention heads to 8. For GraphSAGE, we set the sampling size for each layer to 100 and choose the Mean aggregator. Besides, we run 1000 epochs in each experiment and set the patience of the early stop to 100. For our model, we choose the sampling rate \$$\\lambda $$ from {0.1, 0.2, 0.3} and the number of aggregation layers *K* from {1, 2, 3, 4, 5}, and report the average results under the best parameters learned with a grid search. We run 10 independent experiments with different random seeds and report the average results with standard deviations for all methods.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec19"></a>

### 5.5.2 Account Classification Results

We first evaluate the performance of our proposed model, BPA-GNN, in the account classification task by comparing it with several baseline methods. As the experimental results in Table [5.3](#oebps-html-619883_1_en_5_chapter-xhtml-tab3) show, the performance of BPA-GNN is significantly higher than all baselines. Specifically, BPA-GNN achieves positive improvements on all four evaluation metrics, compared to the best results of the baselines. <a id="oebps-html-619883_1_en_5_chapter-xhtml-tab3"></a>

***Table 5.3***

Ethereum account classification performance (Precision(%) \$$\\pm $$ Std., Recall(%) \$$\\pm $$ Std., Micro-F1(%) \$$\\pm $$ Std., and Macro-F1(%) \$$\\pm $$ Std.). The best results and the second-best results are boldfaced and underlined, respectively

| Method | Precision | Recall | Micro-F1 | Macro-F1 |
| --- | --- | --- | --- | --- |
| MLP | 84.67\$$\\pm $$1.23 | 78.11\$$\\pm $$2.57 | 85.58\$$\\pm $$1.87 | 80.22\$$\\pm $$2.21 |
| GCN | 80.77\$$\\pm $$1.27 | 79.43\$$\\pm $$1.42 | 82.64\$$\\pm $$1.20 | 79.69\$$\\pm $$1.32 |
| GAT | 71.10\$$\\pm $$6.94 | 68.12\$$\\pm $$5.37 | 79.33\$$\\pm $$2.94 | 67.20\$$\\pm $$6.61 |
| GraphSAGE | 86.29\$$\\pm $$2.50 | 84.97\$$\\pm $$1.00 | 86.99\$$\\pm $$1.45 | 84.82\$$\\pm $$1.40 |
| LINKX | 78.05\$$\\pm $$15.35 | 70.41\$$\\pm $$9.75 | 78.10\$$\\pm $$6.64 | 71.25\$$\\pm $$12.14 |
| NLMLP | 59.00\$$\\pm $$8.67 | 59.58\$$\\pm $$2.60 | 76.99\$$\\pm $$1.83 | 56.67\$$\\pm $$3.41 |
| NLGCN | 78.05\$$\\pm $$2.61 | 76.07\$$\\pm $$2.50 | 80.55\$$\\pm $$2.13 | 76.44\$$\\pm $$2.55 |
| FAGCN | 73.99\$$\\pm $$3.48 | 64.45\$$\\pm $$3.88 | 70.25\$$\\pm $$4.35 | 66.28\$$\\pm $$3.93 |
| BPA-GNN | **89.68**\$$\\pm $$**0.76** | **91.42**\$$\\pm $$**1.30** | **91.66**\$$\\pm $$**0.79** | **90.34**\$$\\pm $$**0.92** |

For the baselines, two classic homophilic GNNs, i.e., GCN and GAT, perform poorly, which is even worse than the performance of MLP. This result suggests that, in a heterophilic network, aggregating information from all neighbors during the aggregation process may result in more noise. Although GAT has assigned attention weights to neighbors during aggregations, it still propagates some noise to some extent. Different from the previous two GNNs, GraphSAGE randomly samples a fixed number of neighbors and adopts the design of separating ego and neighbor representations. It can be seen that the performance of GraphSAGE is clearly superior to that of GCN or GAT. Furthermore, our BPA-GNN outperforms GraphSAGE, which indicates that the bi-path neighbor sampling module we proposed is more target-oriented by preserving more useful neighborhood information.

For the four heterophilic models, they all perform worse than the simplest MLP. As a method designed for large-scale networks, LINKX shows fluctuating performance on the Ethereum transaction network. This result may be attributed to the fact that LINKX only utilizes the topological information in the neighborhood and ignores the feature information in it, which indicates the necessity of neighborhood feature information in the Ethereum transaction network. Meanwhile, since NLGCN employs GCN to preserve the feature information of nearby neighbors, the performance difference between NLGCN and NLMLP further demonstrates the important role of neighborhood aggregations. Nevertheless, during the local node embedding phase, NLGCN does not distinguish homophilic and heterophilic information in the neighborhood either. Furthermore, as a spectral domain based method, FAGCN performs poorly because it does not filter the neighbors, resulting in the fact that even though the low- and high-frequency information of each neighbor is separated, the information of some neighbors still negatively affects the results.

Hence, compared with all baselines, our proposed BPA-GNN achieves the best classification performance because it can retain both important and diverse neighborhood information by selectively sampling the 1-hop neighbors based on low and high feature similarity.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec20"></a>

### 5.5.3 Timing Performance Analysis

Next, we compare the time per epoch with the baselines to evaluate the timing performance of BPA-GNN. Specifically, we record the training time of all epochs and compute the mean value after the training process is completed.

As shown in Fig. [5.3](#oebps-html-619883_1_en_5_chapter-xhtml-fig3), MLP achieves superior timing performance by only conducting linear transformations on the feature matrix without the topology-based aggregation process. Likewise, LINKX, an MLP-based method, shows good timing performance. Compared to homophilic GNNs, such as GCN and GAT, the timing performance of BPA-GNN is slightly poorer. These homophilic GNNs directly aggregate all the neighborhood information together, whereas BPA-GNN employs a separated neighborhood aggregation module to aggregate homophilic and heterophilic information separately, potentially requiring additional processing time. Nevertheless, it is notable that the timing performance of BPA-GNN surpasses that of the three heterophilic GNNs, namely NLMLP, NLGCN, and FAGCN. This improvement is attributed to our utilization of the neighbor sampling method, which enables the retention of important neighbors, thereby reducing computational costs and enhancing aggregation speed. Moreover, our experimental results show that on the Ethereum transaction network, NLMLP and NLGCN have the worst timing performance since their method of sorting the attention scores of all nodes is unsuitable for large-scale networks. In summary, with the best classification accuracy, the timing performance of BPA-GNN is within an acceptable range and is competitive among heterophilic GNNs.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fig3"></a>

***Fig. 5.3***

Timing performance of BPA-GNN and all baseline methods

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec21"></a>

### 5.5.4 Effect of Heterophilic Information

Then, we study how heterophilic information affects neighborhood aggregations. Specifically, our goal is to determine whether or not account classification benefits from the aggregation of such heterophilic information in the Ethereum transaction network. To achieve this goal, we design a variant of our model (w/o HE) for better analysis, whose details are as follows. Firstly, we remove neighborhood sampling and aggregation for heterophilic neighbors. In the last node representation learning module, we remove the attention mechanism and simply concatenate the raw feature and homophilic representation of nodes. Following the aforementioned procedures, a new variant model removing the heterophilic aggregation design is built, namely BPA-GNN(w/o HE). We then compare the performance of this variant model with that of the original BPA-GNN. For this variant model, we also employ a grid search to select the optimal results with the sampling rate \$\$\\lambda =0.2\$$ and the number of aggregation layers \$\$K=5\$$. As shown in Table [5.4](#oebps-html-619883_1_en_5_chapter-xhtml-tab4), the original BPA-GNN performs better than this variant model in all four metrics, basically achieving a gain of greater than 1%. These results support the idea that combining effective heterophilic information of nodes can enhance the learning capability of GNN models. <a id="oebps-html-619883_1_en_5_chapter-xhtml-tab4"></a>

***Table 5.4***

Comparison between the original BPA-GNN and BPA-GNN without aggregating heterophilic information in Ethereum account classification (Precision(%) \$$\\pm $$ Std., Recall(%) \$$\\pm $$ Std., Micro-F1(%) \$$\\pm $$ Std., and Macro-F1(%) \$$\\pm $$ Std.)

| Method | Precision | Recall | Micro-F1 | Macro-F1 |
| --- | --- | --- | --- | --- |
| BPA-GNN (w/o HE) | 88.60\$$\\pm $$1.69 | 90.18\$$\\pm $$1.36 | 90.43\$$\\pm $$1.17 | 89.06\$$\\pm $$1.54 |
|  | \$$\\downarrow $$ 1.08 | \$$\\downarrow $$ 1.24 | \$$\\downarrow $$ 1.23 | \$$\\downarrow $$ 1.28 |
| BPA-GNN | **89.68**\$$\\pm $$**0.76** | **91.42**\$$\\pm $$**1.30** | **91.66**\$$\\pm $$**0.79** | **90.34**\$$\\pm $$**0.92** |

The best results are marked in bold

Furthermore, we conduct an analysis of the importance of homophilic and heterophilic information aggregated from the neighborhood by examining their attention weights in Eq. [5.13](#oebps-html-619883_1_en_5_chapter-xhtml-equ13), namely \$\$\\alpha _{s,i}\$$ and \$\$\\alpha _{d,i}\$$. Specifically, we average the two attention weights for the homophilic and heterophilic information for all nodes in each class among 10 independent experiments. We report the results in Fig. [5.4](#oebps-html-619883_1_en_5_chapter-xhtml-fig4). In detail, heterophilic information predominates over homophilic information in node representations for Converter and Exchange. For Gambling and Mining, the weight gaps between the two kinds of information are smaller, and heterophilic information is slightly more useful than homophilic information. In contrast, for ICO and Phish/Hack, homophilic information plays a more crucial role compared to the other one. Generally speaking, the two weights of all six classes fall within the range of 0.4 to 0.6, much larger than 0. This observation indicates the importance of both homophilic and heterophilic information across all classes. In particular, the non-zero weights of \$\$\\alpha _{d,i}\$$ also reflect the positive influence of heterophilic information.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fig4"></a>

***Fig. 5.4***

Average attention weights of nodes belonging to different classes: \$\$\\alpha _{s}\$$ is the weight for homophilic information and \$\$\\alpha _{d}\$$ is the weight for heterophilic information

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec22"></a>

### 5.5.5 Ablation Studies

We conduct the following ablation studies in order to examine the impact of various designs in our model on prediction performance in more detail. Specifically, we perform the corresponding experiments by removing one or both of the two important components of our model, i.e., the large-degree penalty mechanism for preserving useful heterophilic information and the attention mechanism for weighing the importance of homophilic and heterophilic information. In Table [5.5](#oebps-html-619883_1_en_5_chapter-xhtml-tab5), we compare the original BPA-GNN and other variant models without the large-degree penalty mechanism (w/o DP), without the attention mechanism (w/o AM), and without both of the above two designs (w/o BT). The removal of the large-degree penalty mechanism means that when sampling heterophilic neighbors, we sample the heterophilic neighbors directly after sorting based on feature similarity, but no longer sort the neighbors with the lowest 50% feature similarity by degree. The removal of the attention mechanism is to concatenate the raw feature, homophilic representation, and heterophilic representation of nodes directly without adaptively learning the optimal weights in the node representation learning module. The optimal results are all parameterized with the sampling ratio \$\$\\lambda =0.2\$$ and the number of aggregation layers \$\$K=5\$$. <a id="oebps-html-619883_1_en_5_chapter-xhtml-tab5"></a>

***Table 5.5***

Results of ablation studies in Ethereum account classification (Precision(%) \$$\\pm $$ Std., Recall(%) \$$\\pm $$ Std., Micro-F1(%) \$$\\pm $$ Std., and Macro-F1(%) \$$\\pm $$ Std.)

| Method | Precision | Recall | Micro-F1 | Macro-F1 |
| --- | --- | --- | --- | --- |
| BPA-GNN (w/o DP) | 88.85\$$\\pm $$1.56 | 89.39\$$\\pm $$2.10 | 90.61\$$\\pm $$1.20 | 88.88\$$\\pm $$1.86 |
|  | \$$\\downarrow $$ 0.83 | \$$\\downarrow $$ 2.03 | \$$\\downarrow $$ 1.05 | \$$\\downarrow $$ 1.46 |
| BPA-GNN(w/o AM) | 88.07\$$\\pm $$1.22 | 89.47\$$\\pm $$1.56 | 90.37\$$\\pm $$1.13 | 88.49\$$\\pm $$1.23 |
|  | \$$\\downarrow $$ 1.61 | \$$\\downarrow $$ 1.95 | \$$\\downarrow $$ 1.29 | \$$\\downarrow $$ 1.85 |
| BPA-GNN(w/o BT) | 87.43\$$\\pm $$1.92 | 88.47\$$\\pm $$1.84 | 89.69\$$\\pm $$1.28 | 87.68\$$\\pm $$1.93 |
|  | \$$\\downarrow $$ 2.25 | \$$\\downarrow $$ 2.95 | \$$\\downarrow $$ 1.97 | \$$\\downarrow $$ 2.66 |
| BPA-GNN | **89.68**\$$\\pm $$**0.76** | **91.42**\$$\\pm $$**1.30** | **91.66**\$$\\pm $$**0.79** | **90.34**\$$\\pm $$**0.92** |

The best results are marked in bold

When the large-degree penalty mechanism is removed, we can observe a decline in the performance of the model, which indicates that this mechanism can effectively preserve useful and distinguishable heterophilic information in the neighborhood of target nodes. In particular, there are some large-degree nodes in the Ethereum transaction network, especially for the exchange accounts that serve as the platforms for trading fiat money and cryptocurrencies. However, their particular properties, such as extremely large degree and high total transaction value, lead to a significant difference between them and their neighbors in the feature domain. Therefore, if we do not utilize such a large-degree penalty mechanism, the nodes belonging to different classes will all sample a large number of identical exchange nodes with a high probability, resulting in a significant decrease in the distinguishability of extracted heterophilic information. Our large-degree penalty mechanism greatly reduces the impact of such large-degree nodes on neighbor sampling, thus increasing the diversity of heterophilic information in different classes.

For the attention mechanism, the performance of the model also decreases when we remove this part, indicating that the roles played by homophilic and heterophilic information are not the same. Usually, the neighborhood distribution of intra-class nodes tends to be similar, while the neighborhood distribution of inter-class nodes tends to differ from each other. Therefore, the homophilic and heterophilic information extracted by nodes belonging to the same class is similar, and vice versa. More importantly, these two kinds of information may have dissimilar effects on different classes. Simply combining them via a concatenation operation cannot characterize the importance of different information. Therefore, to learn much stronger representations for nodes, we can further weigh the roles they play. The nodes can adaptively learn the optimal attention weights and get the most beneficial information by incorporating the attention mechanism.

Furthermore, the model removing the attention mechanism performs worse than the model removing the large-degree penalty mechanism. This result suggests that even in the absence of the large-degree penalty mechanism, the attention mechanism can effectively weigh the sampled information and aggregate more useful information based on the assigned attention weights to some extent.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec23"></a>

### 5.5.6 Parameter Sensitivity Analysis

Finally, we analyze the influence of two important parameters, i.e., sampling ratio \$$\\lambda $$ and the number of aggregation layers *K*, on the performance of our model. Specifically, we vary the number of aggregation layers from 1 to 5, and the sampling rate from 0.1 to 0.3. The detailed results are shown in Fig. [5.5](#oebps-html-619883_1_en_5_chapter-xhtml-fig5). From the perspective of aggregation layers, we can observe that the performance of BPA-GNN improves with the increment of *K*, and all four metrics basically get the best results at \$\$K=5\$$. The above results also indicate that high-order neighborhood information is helpful in the Ethereum transaction network. Meanwhile, from the perspective of the sampling rate, we can find that the results are basically best at any *K* when \$\$\\lambda =0.1\$$, which indicates that the amount of information preserved is less yet relevant under this setting. With the increment of \$$\\lambda $$, more information is retained. Nonetheless, more noise is also introduced, which leads to a slight drop in performance.<a id="oebps-html-619883_1_en_5_chapter-xhtml-fig5"></a>

***Fig. 5.5***

Parameter sensitivity analysis on sampling ratio \$$\\lambda $$ and the number of aggregation layers *K*. (**a**) Precision. (**b**) Recall. (**c**) Micro-F1. (**d**) Macro-F1

<a id="oebps-html-619883_1_en_5_chapter-xhtml-sec24"></a>

## 5.6 Conclusion

In this chapter, aiming to better analyze the behavior patterns of different accounts on Ethereum, we model the transaction records on Ethereum as a transaction network and further propose a GNN-based model, BPA-GNN, to solve the Ethereum account classification task by incorporating both homophilic and heterophilic information. Specifically, BPA-GNN first samples homophilic and heterophilic neighbors based on feature similarity. Then, BPA-GNN separately aggregates the bi-path information in the neighborhood. Finally, BPA-GNN combines a self-gating mechanism to jointly learn the attention weights for the homophilic and heterophilic information, and then utilizes a fully connected network to obtain the final predictions. Experimental results conducted on the real Ethereum transaction network demonstrate the effectiveness of the proposed BPA-GNN. Meanwhile, the superiority of BPA-GNN indicates the usefulness of combining heterophilic information in the neighborhood aggregations in the Ethereum account classification task. Combining the characteristics of the Ethereum transaction network, the proposed model provides a better reference solution for Ethereum illegal activity identification and supports the better development of the cryptocurrency market.

<a id="oebps-html-619883_1_en_5_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr1"></a>Wu, J., Lin, K., Lin, D., Zheng, Z., Huang, H., Zheng, Z.: Financial crimes in web3-empowered metaverse: taxonomy, countermeasures, and opportunities. IEEE Open J. Comput. Soc. **4**, 37–49 (2023)[Crossref](https://doi.org/10.1109/OJCS.2023.3245801)
2. 2\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr2"></a>Chainalysis: The 2023 crypto crime report (2023). \[Online]. Available: [https://go.chainalysis.com/2023-crypto-crime-report.html](https://go.chainalysis.com/2023-crypto-crime-report.html)
3. 3\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr3"></a>Wu, Z., Liu, J., Wu, J., Zheng, Z., Chen, T.: TRacer: scalable graph-based transaction tracing for account-based blockchain trading systems. IEEE Trans. Inf. Forensics Secur. **18**, 2609–2621 (2023)[Crossref](https://doi.org/10.1109/TIFS.2023.3266162)
4. 4\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr4"></a>Wu, J., Liu, J., Zhao, Y., Zheng, Z.: Analysis of cryptocurrency transactions from a network perspective: an overview. J. Netw. Comput. Appl. **190**, 103139 (2021)[Crossref](https://doi.org/10.1016/j.jnca.2021.103139)
5. 5\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr5"></a>Liu, J., Zheng, J., Wu, J., Zheng, Z.: FA-GNN: filter and augment graph neural networks for account classification in Ethereum. IEEE Trans. Netw. Sci. Eng. **9**(4), 2579–2588 (2022)[Crossref](https://doi.org/10.1109/TNSE.2022.3166655)
6. 6\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr6"></a>Yu, S., Jin, J., Xie, Y., Shen, J., Xuan, Q.: Ponzi scheme detection in Ethereum transaction network. In: Proc. Commun. Comput. Info. Sci., pp. 175–186 (Aug. 2021)
7. 7\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr7"></a>Liu, X., Tang, Z., Li, P., Guo, S., Fan, X., Zhang, J.: A graph learning based approach for identity inference in DApp platform blockchain. IEEE Trans. Emerg. Top. Comput. **10**(1), 438–449 (2022)[Crossref](https://doi.org/10.1109/TETC.2020.3027309)
8. 8\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr8"></a>Yu, T., Chen, X., Xu, Z., Xu, J.: MP-GCN: a phishing nodes detection approach via graph convolution network for Ethereum. Appl. Sci. **12**(14), 7294 (2022)[Crossref](https://doi.org/10.3390/app12147294)
9. 9.Wu, J., Liu, J., Chen, W., Huang, H., Zheng, Z., Zhang, Y.: Detecting mixing services via mining bitcoin transaction network with hybrid motifs. IEEE Trans. Syst. Man Cybern. Syst. **52**(4), 2237–2249 (2022)[Crossref](https://doi.org/10.1109/TSMC.2021.3049278)
10. 10\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr10"></a>Zhou, J., Hu, C., Chi, J., Wu, J., Shen, M., Xuan, Q.: Behavior-aware account de-anonymization on Ethereum interaction graph. IEEE Trans. Inf. Forensics Secur. **17**, 3433–3448 (2022)[Crossref](https://doi.org/10.1109/TIFS.2022.3208471)
11. 11\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr11"></a>Huang, T., Lin, D., Wu, J.: Ethereum account classification based on graph convolutional network. IEEE Trans. Circuits Syst. Express Briefs **69**(5), 2528–2532 (2022)[Crossref](https://doi.org/10.1109/TCSII.2022.3161112)
12. 12\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr12"></a>Gilmer, J., Schoenholz, S.S., Riley, P.F., Vinyals, O., Dahl, G.E.: Neural message passing for quantum chemistry. In: Proc. Int. Conf. Machin. Learn., pp. 1263–1272 (Aug. 2017)
13. 13\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr13"></a>Kipf, T.N., Welling, M.: Semi-supervised classification with graph convolutional networks. In: Proc. Int. Conf. Learn. Represent. (Apr. 2017)
14. 14\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr14"></a>Zhu, J., Yan, Y., Zhao, L., Heimann, M., Akoglu, L., Koutra, D.: Beyond homophily in graph neural networks: current limitations and effective designs. In: Proc. Adv. Neural Inf. Proces. Syst., pp. 7793–7804 (Dec. 2020)
15. 15\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr15"></a>Pei, H., Wei, B., Chang, K.C.-C., Lei, Y., Yang, B.: Geom-GCN: geometric graph convolutional networks. In: Proc. Int. Conf. Learn. Represent. (Apr. 2020)
16. 16\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr16"></a>Perozzi, B., Al-Rfou, R., Skiena, S.: DeepWalk: Online learning of social representations. In: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 701–710 (2014)
17. 17\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr17"></a>Church, K.W.: Word2vec. Nat. Lang. Eng. **23**(1), 155–162 (2017)[Crossref](https://doi.org/10.1017/S1351324916000334)
18. 18\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr18"></a>Grover, A., Leskovec, J.: node2vec: scalable feature learning for networks. In: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., pp. 855–864 (Aug. 2016)
19. 19\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr19"></a>Tang, J., Qu, M., Wang, M., Zhang, M., Yan, J., Mei, Q.: LINE: large-scale information network embedding. In: Proc. Int. Conf. World Wide Web, pp. 1067–1077 (May 2015)
20. 20\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr20"></a>Hamilton, W., Ying, Z., Leskovec, J.: Inductive representation learning on large graphs. In: Proc. Adv. Neural Inf. Proces. Syst. (Dec. 2017)
21. 21\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr21"></a>Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., Bengio, Y.: Graph attention networks. In: Proc. Int. Conf. Learn. Represent. (2018)
22. 22\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr22"></a>Wu, F., Souza, A., Zhang, T., Fifty, C., Yu, T., Weinberger, K.: Simplifying graph convolutional networks. In: Proc. Int. Conf. Machin. Learn., pp. 6861–6871 (Jun. 2019)
23. 23\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr23"></a>Zheng, X., Liu, Y., Pan, S., Zhang, M., Jin, D., Yu, P.S.: Graph neural networks for graphs with heterophily: a survey. arXiv preprint arXiv:2202.07082 (2022)
24. 24\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr24"></a>Abu-El-Haija, S., Perozzi, B., Kapoor, A., Alipourfard, N., Lerman, K., Harutyunyan, H., Steeg, G.V., Galstyan, A.: MixHop: higher-order graph convolutional architectures via sparsified neighborhood mixing. In: Proc. Int. Conf. Machin. Learn., pp. 21–29 (Jun. 2019)
25. 25\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr25"></a>Liu, M., Wang, Z., Ji, S.: Non-local graph neural networks. IEEE Trans. Pattern Anal. Mach. Intell. **44**(12), 10270–10276 (2022)[Crossref](https://doi.org/10.1109/TPAMI.2021.3134200)
26. 26\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr26"></a>Wang, T., Jin, D., Wang, R., He, D., Huang, Y.: Powerful graph convolutional networks with adaptive propagation mechanism for homophily and heterophily. In: Proc. AAAI Conf. Artif. Intell., pp. 4210–4218 (Jun. 2022)
27. 27\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr27"></a>Huang, J., Li, P., Huang, R., Na, C., Zhang, A.: Revisiting the role of heterophily in graph representation learning: an edge classification perspective. arXiv preprint arXiv:2205.11322 (2022)
28. 28\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr28"></a>Bi, W., Du, L., Fu, Q., Wang, Y., Han, S., Zhang, D.: Make heterophily graphs better fit GNN: a graph rewiring approach. arXiv preprint arXiv:2209.08264 (2022)
29. 29\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr29"></a>Bo, D., Wang, X., Shi, C., Shen, H.: Beyond low-frequency information in graph convolutional networks. In: Proc. AAAI Conf. Artif. Intell., pp. 3950–3957 (Feb. 2021)
30. 30\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr30"></a>Chien, E., Peng, J., Li, P., Milenkovic, O.: Adaptive universal generalized pagerank graph neural network. In: Proc. Int. Conf. Learn. Represent. (May 2021)
31. 31\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr31"></a>Jin, D., Wang, R., Ge, M., He, D., Li, X., Lin, W., Zhang, W.: RAW-GNN: random walk aggregation based graph neural network. In: Proc. Int. Joint Conf. Artif. Intell., pp. 2108–2114 (Jul. 2022)
32. 32\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr32"></a>Sun, Y., Deng, H., Yang, Y., Wang, C., Xu, J., Huang, R., Cao, L., Wang, Y., Chen, L.: Beyond homophily: structure-aware path aggregation graph neural network. In: Proc. Int. Joint Conf. Artif. Intell., pp. 2233–2240 (Jul. 2022)
33. 33\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr33"></a>Kumar, N., Singh, A., Handa, A., Shukla, S.K.: Detecting malicious accounts on the Ethereum blockchain with supervised learning. In: Proc. Lect. Notes Comput. Sci., pp. 94–109 (Jul. 2020)
34. 34\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr34"></a>Chen, W., Guo, X., Chen, Z., Zheng, Z., Lu, Y.: Phishing scam detection on Ethereum: towards financial security for blockchain ecosystem. In: Proc. Int. Joint Conf. Artif. Intell., pp. 4506–4512 (2020)
35. 35\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr35"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
36. 36\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr36"></a>Wang, Y., Liu, Z., Xu, J., Yan, W.: Heterogeneous network representation learning approach for Ethereum identity identification. IEEE Trans. Comput. Soc. Syst. **10**(3), 890–899 (2022)[Crossref](https://doi.org/10.1109/TCSS.2022.3164719)
37. 37\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr37"></a>Shen, J., Zhou, J., Xie, Y., Yu, S., Xuan, Q.: Identity inference on blockchain using graph neural network. In: Proc. Commun. Comput. Info. Sci., pp. 3–17 (Aug. 2021)
38. 38\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr38"></a>Lei, R., Wang, Z., Li, Y., Ding, B., Wei, Z.: EvenNet: ignoring odd-hop neighbors improves robustness of graph neural networks. In: Proc. Adv. Neural Inf. Proces. Syst. (2022)
39. 39\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr39"></a>Gardner, M., Dorling, S.: Artificial neural networks (the multilayer perceptron)–a review of applications in the atmospheric sciences. Atmos. Environ. **32**(14–15), 2627–2636 (1998)[Crossref](<https://doi.org/10.1016/S1352-2310(97)00447-0>)
40. 40\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr40"></a>Lim, D., Hohne, F., Li, X., Huang, S.L., Gupta, V., Bhalerao, O., Lim, S.-N.: Large scale learning on non-homophilous graphs: new benchmarks and strong simple methods. In: Proc. Adv. Neural Inf. Proces. Syst., pp. 20887–20902 (Dec. 2021)
41. 41\.<a id="oebps-html-619883_1_en_5_chapter-xhtml-cr41"></a>Kingma, D.P., Ba, J.: Adam: a method for stochastic optimization. arXiv preprint arXiv:1412.6980 (2014)

**Footnotes**

[1](#oebps-html-619883_1_en_5_chapter-xhtml-fn1_source)<a id="oebps-html-619883_1_en_5_chapter-xhtml-fn1"></a>

[https://xblock.pro/#/dataset/24](https://xblock.pro/#/dataset/24).

<a id="oebps-html-619883_1_en_6_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_6](https://doi.org/10.1007/978-981-97-4430-5_6)

# 6. Phishing Fraud Detection Based on the Streaming Graph Algorithm

Wenjia Yu[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) , Jingjing Yang[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) , Jieli Liu[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) , Yijun Xia[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) , Baoying Huang[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) , Jiajing Wu[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_6_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor1"></a>

**Wenjia YuEmail:** [yuwj33@ms.sysu.edu.cn](mailto:yuwj33@ms.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor2"></a>

**Jingjing Yang (Corresponding author)Email:** [yangjj93@mail2.sysu.edu.cn](mailto:yangjj93@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor3"></a>

**Jieli LiuEmail:** [liujli7@mail2.sysu.edu.cn](mailto:liujli7@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor4"></a>

**Yijun XiaEmail:** [xiayj6@mail2.sysu.edu.cn](mailto:xiayj6@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor5"></a>

**Baoying HuangEmail:** [huangby27@mail2.sysu.edu.cn](mailto:huangby27@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor6"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-contactofauthor7"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

In recent years, phishing scams have emerged as one of the most serious crimes on Ethereum. Existing phishing scam detection methods typically model public transaction records on the blockchain as a graph, and then identify phishing addresses through manual feature extraction or graph learning frameworks. Meanwhile, these methods model transactions within a period as a static network for analysis. Therefore, these methods lack the ability to capture fine-grained time dynamics, and on the other hand, they cannot handle the large-scale and continuously growing transaction data on the Ethereum blockchain, resulting in lower scalability and efficiency. In this chapter, we propose a two-dimensional streaming framework *2DynEthNet* for Ethereum phishing scam detection. *First*, we cast the transaction series into 6 slices according to block numbers, treating each as a separate task. *In the first dimension*, we treat transaction features as edge features instead of node features within one task, allowing each transaction to be streamed in 2DynEthNet, aiming to capture the evolutionary features of the Ethereum transaction network at a fine-grained level in continuous time. *In the second dimension*, we adopt the strategy of incremental information training between tasks, which utilizes meta-learning to quickly update the model parameters under new slices, thus effectively improving the scalability of the model. *Finally*, experimental results on large-scale real Ethereum phishing scam datasets show that our 2DynEthNet outperforms the state-of-the-art methods and achieves the most efficient training speed, proving the effectiveness of both temporal edge representation and meta-learning. In addition, we provide an Ethereum large-scale dynamic graph transaction dataset, ETGraph, which is in line with the data distribution in real transaction scenarios without sampling and filtering unlabeled accounts.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec1"></a>

## 6.1 Introduction

Phishing scams, a typical crime on Ethereum, have inflicted severe financial losses and affected a considerable number of victims. According to the security risk monitoring of Beosin EagleEye, the total loss caused by hacker attacks and phishing scams in the field of Web3 has reached \$655.61 million only in the first half of 2023, of which 75.6% of the loss amount came from Ethereum, ranking first among all chain platforms \[[1](#oebps-html-619883_1_en_6_chapter-xhtml-cr1)]. This indicates that phishing scams on Ethereum have become a major threat to the security of Web3 users. Therefore, identifying Ethereum phishing scams has become an imperative research topic and attracted widespread attention.

Traditional phishing methods are not well-suited for Ethereum scenarios. While traditional phishing techniques are single and limited, there is no fixed pattern to phishing scams on Ethereum. In traditional phishing scenarios, attackers exploit centralized single-server systems, impersonating legitimate organizations or websites to trick users into disclosing their sensitive information, and then using this information to commit theft. However, on Ethereum, as a decentralized platform based on the automatic execution of smart contracts, phishers are no longer confined to using traditional social engineering tactics to deceive users. Instead, they utilize various means such as social chat or email to disseminate phishing addresses to victims, directly swindling money.

Existing Ethereum phishing detection methods can be broadly divided into two types, traditional feature engineering method \[[2](#oebps-html-619883_1_en_6_chapter-xhtml-cr2), [3](#oebps-html-619883_1_en_6_chapter-xhtml-cr3)] and network representation learning method \[[4](#oebps-html-619883_1_en_6_chapter-xhtml-cr4)–[7](#oebps-html-619883_1_en_6_chapter-xhtml-cr7)], aiming to learn node representations and accomplish node classification tasks. However, traditional machine learning models rely on expert knowledge and manual-designed features, such as node degree, transaction volume, and time interval, resulting in inefficiency and lack of automation. Network representation learning methods, on the other hand, automatically learn representations through random walk \[[8](#oebps-html-619883_1_en_6_chapter-xhtml-cr8)] and graph neural network \[[9](#oebps-html-619883_1_en_6_chapter-xhtml-cr9)] to explore deep node features. However, there are still two remaining problems: **(1) Lack of dynamism.** Existing methods only utilize statistical and structural features of transaction records as node representations, ignoring context information of transaction records, resulting in weak node representations. Moreover, existing dynamic methods treat the evolution of the transaction network as a collection of static snapshots over discrete time periods, resulting in a loss of information between time slices and lacking the capability to capture fine-grained temporal dynamics. **(2) Lack of scalability.** Given the large and rapidly growing scale of Ethereum transaction network, existing static or single dynamic model architectures require substantial GPU memory to store the entire or a large part of the graph, making it inefficient to process continuously growing transaction data. Additionally, these methods need to retrain existing data when new time slices are added, leading to poor scalability and efficiency of the models. Furthermore, both types of methods suffer from a common drawback of using biased datasets that filter out unlabeled accounts. A biased sampling of first and second-order subgraphs of target nodes leads to distortion of data distribution, which does not conform to real-world transaction scenarios. The above shortcomings finally lead to unsatisfactory results of existing Ethereum phishing detection methods.

To address the aforementioned challenges, in this chapter, we propose a continuous dynamic and scalable two-dimensional streaming phishing detection framework 2DynEthNet. The first dimension refers to continuous dynamics within time slices, while the second dimension focuses on incremental scalability between time slices. First, we divide a large-scale Ethereum transaction dataset into different time slices by block. To capture fine-grained dynamic continuity, in the first dimension, we utilize the contextual temporal information of transactions to generate temporal edge features. We then aggregate edge features using broadcasting mechanisms and storage modules to obtain transaction features for nodes, ensuring that the framework can learn the information of each new transaction occurring in the network. To enhance the scalability of the framework, in the second dimension, we employ meta-learning to update parameters for new time slices, which allows the model to quickly achieve optimal solutions on new data without retraining the existing data. Finally, to solve the biased distortion of dataset distribution, we provide ETGraph, a real-world and large-scale dynamic graph dataset of Ethereum transaction scenarios, without biased sampling and filtering of unlabeled transaction accounts to ensure the representativeness and authenticity of the dataset. Extensive experiments are conducted on this dataset to verify the effectiveness of 2DynEthNet.

**Contributions**

Our contributions can be summarized as:

- **2DynEthNet:** We propose a two-dimensional streaming framework to enhance the effectiveness of Ethereum phishing detection, which achieves continuous dynamics within time slices (first dimension) and incremental scalability between time slices (second dimension).
- **Continuity:** The contextual information of Ethereum transactions is utilized as temporal edge features to enable each transaction to be streamed, thus capturing the evolutionary features of Ethereum transaction network at a fine-grained level over continuous time, which is more automated and aligns better with real-world Ethereum transaction scenarios.
- **Incrementalism:** The strategy of incremental information training is adopted, which utilizes meta-learning to update model parameters for new time slices based solely on new information. It enables rapid derivation of new models without retraining the existing data and is better adapted to the large-scale and rapid-growing Ethereum transaction network, thus enhancing the scalability of the model.
- **ETGraph:** We provide a real-world and large-scale dynamic graph dataset of Ethereum transaction scenarios, without biased sampling and filtering of unlabeled accounts. Extensive experiments on this dataset demonstrate that 2DynEthNet outperforms state-of-the-art methods on multiple metrics.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec2"></a>

## 6.2 Related Work

In this section, we briefly review existing work on Ethereum phishing fraud detection and dynamic network representation learning.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec3"></a>

### 6.2.1 Ethereum Phishing Fraud Detection

Phishing fraud detection is one of the hottest research areas in Ethereum. Existing methods for Ethereum phishing fraud detection are typically categorized into two types: traditional machine learning methods relying on feature engineering and network representation learning methods based on random walk or graph neural networks.

Traditional machine learning methods rely on expert knowledge and manually-designed static features. Chen et al. \[[10](#oebps-html-619883_1_en_6_chapter-xhtml-cr10)] manually extracted 219-dimensional features of the first-order and second-order neighbors of the target node, and then used a LighTGBM-based integrated machine learning algorithm to identify phishing nodes.

Network representation learning methods mainly include random walk-based methods such as DeepWalk \[[11](#oebps-html-619883_1_en_6_chapter-xhtml-cr11)], and GNN-based methods such as GCN \[[12](#oebps-html-619883_1_en_6_chapter-xhtml-cr12)]. Wu et al. \[[3](#oebps-html-619883_1_en_6_chapter-xhtml-cr3)] proposed Trans2Vec based on the traditional embedding method Node2Vec \[[13](#oebps-html-619883_1_en_6_chapter-xhtml-cr13)]. Trans2Vec first constructs the Ethereum transaction network as an undirected graph, then incorporates the time and amount information of transactions, and modifies the random walk of Node2vec to a biased random walk to obtain the node sequences, which makes Trans2vec more suitable for phishing fraud detection scenarios on Ethereum. Chen et al. \[[10](#oebps-html-619883_1_en_6_chapter-xhtml-cr10)] introduced E-GCN for phishing node detection, being the first to apply GCN to Ethereum phishing fraud detection tasks. E-GCN initially extracts 8-dimensional statistical features, and then utilizes GCN to learn node embeddings, thereby obtaining structural features of the transaction network. Chen et al. \[[14](#oebps-html-619883_1_en_6_chapter-xhtml-cr14)] proposed a method based on GCN and autoencoders, which effectively integrates the statistical features and structural features of nodes to accurately identify phishing accounts. Li et al. \[[7](#oebps-html-619883_1_en_6_chapter-xhtml-cr7)] introduced a self-supervised incremental deep graph learning (SIEGE) model and designed an incremental learning paradigm and a temporal pretext task to facilitate information flow between different graph splits, thus achieving the identification of Ethereum phishing accounts.

However, all these methods ignore the contextual information of transaction records and lack the ability to capture fine-grained temporal dynamics. Additionally, relying on manually-designed static node features leads to weak node representations for phishing fraud detection, resulting in lower accuracy and efficiency of the models. Therefore, Li et al. \[[15](#oebps-html-619883_1_en_6_chapter-xhtml-cr15)] proposed the temporal transaction aggregation graph network (TTAGN), which integrates transaction, structural, and statistical features of nodes to obtain node representations. TEGDetector \[[6](#oebps-html-619883_1_en_6_chapter-xhtml-cr6)] leverages GCN and GRU to capture the topological structure of transaction evolution graphs and the dynamic evolution features of networks between multiple time slices, ultimately extracting behavioral features of nodes. However, such methods require retraining existing data to update model parameters for new time slices, making it inefficient to handle large and continuously growing Ethereum transaction datasets.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec4"></a>

### 6.2.2 Dynamic Network Representation Learning

Dynamic network representation learning methods focus on capturing the evolving features of networks over time, and existing methods can be categorized into two types.

One is discrete-time dynamic network representation learning. Some of these methods either aggregate graph snapshots first and then apply static methods \[[16](#oebps-html-619883_1_en_6_chapter-xhtml-cr16)–[18](#oebps-html-619883_1_en_6_chapter-xhtml-cr18)], or encode each snapshot to generate a series of embeddings \[[19](#oebps-html-619883_1_en_6_chapter-xhtml-cr19)–[22](#oebps-html-619883_1_en_6_chapter-xhtml-cr22)], and some will also leverage RNN models \[[21](#oebps-html-619883_1_en_6_chapter-xhtml-cr21), [23](#oebps-html-619883_1_en_6_chapter-xhtml-cr23), [24](#oebps-html-619883_1_en_6_chapter-xhtml-cr24)]. The other is continuous-time dynamic network representation learning. Dyrep \[[25](#oebps-html-619883_1_en_6_chapter-xhtml-cr25)] deals with chronological sequences of events, defines two state change scenarios for graph evolution, and maintains a state matrix to update node representations. JODIE \[[26](#oebps-html-619883_1_en_6_chapter-xhtml-cr26)] consists of an update operation, a projection operation, and a prediction operation to update the node memory of the relevant nodes using two coupled RNN models. TGN \[[27](#oebps-html-619883_1_en_6_chapter-xhtml-cr27)] introduces a message-passing and a node storage module to learn node embedding.

However, these dynamic methods require retraining existing data to obtain optimal solutions for new time slices, making it inefficient to handle large and continuously growing Ethereum transaction datasets and unlabeled nodes. Inspired by continuous-time dynamic network representation learning and Ethereum transaction network features, we propose our two-dimensional streaming framework 2DynEthNet.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec5"></a>

## 6.3 Problem Definition

In this chapter, the phishing fraud detection task on Ethereum is described as a graph node classification problem. Assuming that the partially labeled Ethereum transaction network is \$$ G_r = (V, E, X, C) $$, we view the transaction address as a node \$$ v_i $$, where \$$ V = \\{ v_1, ..., v_n \\} $$ is a set of addresses. The transaction between nodes serves as an edge \$$ E_i $$, where \$$ E = \\{E_1, ..., E_R\\} $$ is a transaction set of R relations. The direction, quantity, and time information of transactions are taken as edge attributes \$$ X \\in \\mathbb {R}^{|E| \\times S} $$, where \$$ S $$ is the feature space size for each edge, and \$$ C \\in \\mathbb {R} ^{{|V|} \\times Y} $$ where \$$ Y $$ is the label set. The goal of our model is to effectively learn the embedding representation of nodes \$$ X_E \\in \\mathbb {R} ^{{|V|} \\times d} $$ from large-scale Ethereum transaction data, where d is the dimension of feature representation.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec6"></a>

## 6.4 Methodology of Phishing Fraud Detection

2DynEthNet is a continuous dynamic and scalable two-dimensional streaming phishing fraud detection model. It can adapt to real Ethereum transaction data, enhance the identification ability of phishing nodes, and greatly improve the detection speed of phishing scams. Specifically, 2DynEthNet consists of four objectives: dataset construction, temporal transaction graph generation, two-dimensional network embedding, and phishing node detection.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec7"></a>

### 6.4.1 Ethereum Transaction Dataset Construction

To align with real Ethereum transaction scenarios, we refrain from using biased sampling and filtering unlabeled accounts. Instead, we construct a large-scale dynamic graph dataset ETGraph to ensure the authenticity of data distribution and the continuity of transactions.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec8"></a>

#### 6.4.1.1 Phishing Fraud Data Collection

The raw data of Ethereum transactions is sourced from [http://xblock.pro](http://xblock.pro), one of the reputable blockchain data platforms widely used in academia. We collected data from block height 8,000,000 to block height 8,999,999. Different from traditional Ethereum datasets, considering the significant role of contract accounts in smart contract invocations and internal transaction executions on Ethereum, we did not filter out these unlabeled accounts. Specifically, each transaction record consists of 11 components: (1) Sender account of a transaction. (2) Recipient account of a transaction. (3) Amount of ETH transferred. (4) Maximum gas allowed to be consumed. (5) The number of gas consumed. (6) Price of one unit of gas in the transaction. (7) A unique 66-character identifier of a transaction. (8) Time when a transaction is mined. (9) Block number. (10) Whether the sender is the contract account. (11) Whether the recipient is the contract account.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec9"></a>

#### 6.4.1.2 Phishing Fraud Data Processing

We obtained reported phishing addresses up to August 2023 from three channels: (1) ScamSniffer: ScamSniffer is a real-time Web3 anti-scam blockchain platform that collects malicious accounts luring users into risky transactions. (2) Etherscan: Etherscan is a blockchain explorer that reports various network crimes and scam accounts on Ethereum. (3) Chainabuse: Chainabuse is a blockchain community platform that provides cases of cryptocurrency scam transactions via label filtering. Finally, we labeled 9,032 unique phishing addresses for ETGraph.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec10"></a>

### 6.4.2 Temporal Transaction Graph Generation

Based on the acquired large-scale Ethereum transaction data, we construct a temporal multi-edge transaction-directed graph. Notably, to avoid sampling subgraphs that may distort the real distribution of transaction data, we prefer to construct the full graph that fits real transaction scenarios to ensure the continuity of transactions. In the transaction graph, we use nodes to represent Ethereum transaction addresses, and edges to represent transactions between addresses. The multi-edge directed graph allows multiple directed edges to exist between any pair of nodes, along with each edge carrying transaction information such as the transaction amount and timestamp.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec11"></a>

### 6.4.3 Model Architecture

2DynEthNet is a two-dimensional streaming framework for detecting phishing scam nodes. This framework consists of two dimensions: (1) The first dimension includes a broadcast module, a storage module, and an embedding module to enable continuous dynamics within time slices, as shown in Fig. [6.1](#oebps-html-619883_1_en_6_chapter-xhtml-fig1). (2) The second dimension utilizes meta-learning to rapidly update model parameters, achieving incremental scalability between time slices, as shown in Fig. [6.2](#oebps-html-619883_1_en_6_chapter-xhtml-fig2).<a id="oebps-html-619883_1_en_6_chapter-xhtml-fig1"></a>

***Fig. 6.1***

The overall architecture of 2DynEthNet in the first dimension. Within one time slice, 2DynEthNet inputs streamingly Ethereum transactions to construct the transaction graph. When a new transaction is inputted in 2DynEthNet, 2DynEthNet encodes the transaction information \$$\\xi $$ to the transaction broadcast context. Then two parallel steps will be performed. One is that the broadcast mechanism broadcasts the content to the node’s neighboring nodes and the storage module will be updated. The other one is the embedding module which utilizes the node embedding at time \$$ t- $$ and learns the embedding of the node’s storage module to generate the final node embedding at time \$$ t $$

<a id="oebps-html-619883_1_en_6_chapter-xhtml-fig2"></a>

***Fig. 6.2***

The overall architecture of 2DynEthNet in the second dimension. We treat learning optimal parameters of the transaction network for different time slices as different tasks. Within each task, parameters will be trained and updated according to the model in the first dimension to ensure the continuity of the model. Between tasks, the Reptile algorithm in meta-learning is used to learn the initialization parameters of these tasks, so that the framework can learn the optimal parameters more quickly when processing new transaction data

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec12"></a>

#### 6.4.3.1 First Dimension

***1. Broadcast Module***

The historical behavior of an account plays a crucial role in predicting its future behavior patterns. Meanwhile, the transaction behavior of an account’s neighbors also influences the transaction behavior of the account to some extent. Therefore, to simultaneously learn the historical behavior features of an account and the transaction behavior features of its neighbors, we design a broadcast module that enables our model to more comprehensively and accurately predict future transaction patterns of accounts.

***(a) Message Generation***

Due to the anonymity of accounts on Ethereum, it’s challenging to straightly abstract raw features from accounts. Therefore, traditional methods typically rely on expert knowledge and manual effort to transform transaction features within a certain time threshold into node features through mathematical operations. However, these methods lack automation and overlook the dynamic evolution features of the transaction network. Nevertheless, transactions on Ethereum exhibit continuity and possess rich features such as timestamps and amounts. Therefore, we design edge features to replace node features, which ensures that the model can quickly process each new transaction in real-time without converting them into initial node features. This allows the model to capture the evolutionary features of the transaction network at a fine-grained level and better aligns with Ethereum transaction scenarios where the original information features of accounts are difficult to obtain.

Specifically, we extract features from raw transaction information between accounts as edge features in the network modeling. Additionally, given that smart contracts on Ethereum are transaction-driven and play an important role in transaction execution, we take smart contracts into account to extract more comprehensive edge features. It’s worth noting that if an external account invokes multiple smart contracts to generate multiple internal transactions during a transfer, we aggregate these transactions into one transaction by summing transaction amounts, tracking the transaction count, and setting the transaction timestamp to the first timestamp of original transactions. Finally, we extract 16 transaction features including transaction hash and timestamp, transaction count and amount, gas consumption and cost as edge features.

Due to the differences in units and scales between features, which may affect the subsequent model prediction results, it’s essential to scale the extracted features to treat each dimensional feature equally. We opt for Z-score normalization to normalize the data. This method allows for some form of non-linear scaling and offsetting of transaction data features. Z-score normalization calculates the mean and variance of features in each dimension to scale the features so that the features in each dimension conform to a normal distribution. For the feature matrix \$\$X\\in \\mathbb {R} ^{L\\times d}\$$:

\$$\\displaystyle \\begin{aligned} \\begin{aligned} \\mu\_{r} = \\frac{1}{d}\\sum\_{i=1}^dx^i\_{r}, \\quad  \\sigma_r &amp;amp;=\\sqrt{\\frac{1}{d}\\sum\_{i=1}^d(x^i_{r}-\\mu_r)^{2}},\\quad  r = 1,2,...n\\\\ \\dot{x}_r^i &amp;amp;= \\frac{x_r^i-\\mu_r}{\\sigma_r} \\end{aligned} \\end{aligned} $$

(6.1)

where \$$ x_r^i $$ represents the \$$ i $$-th dimension of the \$$ r $$-th feature, \$$ \\mu _r $$ denotes the mean of the \$$ r $$-th feature, and \$$ \\sigma _r $$ represents the variance of the \$$ r $$-th feature. Standardized eigenvalues fluctuate around 0, with greater than 0 indicating above average and less than 0 indicating below average.

***(b) Broadcast Mechanism***

The broadcast mechanism is responsible for asynchronously disseminating detailed interaction information to the \$$ k $$-order neighbors of the node. Specifically, when a new transaction occurs in the transaction network, the broadcast mechanism first generates transaction features as edge features and then broadcasts them to other nodes. Considering the large scale of the Ethereum network and ensuring the efficiency of the model, we broadcast to the first-order neighbors of the two nodes involved in the transaction. According to the temporal transaction graph constructed in Sect. [6.4.2](#oebps-html-619883_1_en_6_chapter-xhtml-sec10), assuming that a new transaction occurs between node \$$ u $$ and \$$ v $$ at time \$$ t $$, we use the following formula to generate the broadcast content:

\$$\\displaystyle \\begin{aligned} \\beta(t) = z\_{u}(t) + \\xi(t) + z_{v}(t) \\end{aligned} $$

(6.2)

where \$$ \\beta (t) $$ represents the broadcast content at time \$$ t $$, \$$ z_u(t) $$ denotes the embedding representation of node \$$ u $$ at time \$$ t $$, represents the embedding \$$ \\zeta (t) $$ represents the transaction features between node \$$ u $$ and \$$ v $$ at time \$$ t $$. It is evident that the broadcast content contains not only the generated transaction features, but also concatenates the historical features of the two nodes themselves.

It is worth noting that besides delivering the broadcast content to all first-order neighbors of the target node, to enhance the speed of 2DynEthNet, we adopt a strategy of selecting a limited number of broadcast paths. Specifically, since accounts on Ethereum typically remain inactive for long periods, with only short bursts of activity, we employ the principle of temporal proximity which selects the \$$ k $$-order nodes that have the most recent transactions with the target node for broadcasting.

***2. Storage Module***

To maximize the learning of pertinent history information and neighboring transactions of an account, we implement the storage module. Specifically, the storage module is updated in two scenarios: (1) When a node receives broadcast content from other nodes, it stores the broadcast content in its storage module. (2) When a node engages in a new transaction, it also stores the broadcast content generated by its transaction in its storage module.

Considering the objective of minimizing algorithmic memory overhead, we configure the storage module as a fixed-length First-In-First-Out (FIFO) queue. It is obvious that the contents in the FIFO storage module are arranged in chronological order, which implies that the earlier the content is stored, the lower its importance. Based on this, we introduce a decay factor \$$ \\alpha = (\\alpha _1, \\alpha _2, \\ldots , \\alpha _m) $$ to assist in aggregating the contents in the storage module. Once a node necessitates an update, the storage module generates a vector \$$ s(t) $$ supporting the node embedding update according to the following formula:

\$$\\displaystyle \\begin{aligned} s(t) = agg\\left(\\beta\_{1}(t), \\beta\_{2}(t),...,\\beta_{m}(t)\\right) \\end{aligned} $$

(6.3)

\$$\\displaystyle \\begin{aligned} agg\\left(\\beta\_{1}(t), \\beta\_{2}(t),...,\\beta\_{m}(t)\\right) = \\frac{1}{m} \\sum\_{i=1}^m \\alpha\_{i}\\cdotp \\beta_{i}(t) \\end{aligned} $$

(6.4)

where *m* denotes the length of storage module, \$\$\\beta _{i}(t)\$$ denotes the *i*-th broadcast content stored in the storage module.

Notably, due to the presence of a large number of unlabeled accounts in the Ethereum transaction network, traditional methods typically filter out these accounts, which may disrupt the connectivity of the graph and make the originally sparse Ethereum network even sparser. To some extent, this may disrupt broadcast paths and lead to a reduction of information in the storage module. Therefore, our model retains these unlabeled nodes, which allows 2DynEthNet to use them for delivering and storing information, thereby better representing the nodes. Additionally, unlabeled nodes do not participate in the loss function update during the training process, which means the model does not overly rely on unlabeled data, thus avoiding overfitting to noisy or anomalous data and ensuring the accuracy and generalization capability of 2DynEthNet predictions.

***3. Embedding Module***

To integrate the historical embedding representation, historical transaction features, and neighbor transaction features of the account to acquire node embeddings for learning the latest state of accounts, we design an embedding module.

Taking into account the high transaction volume and short lifespan of Ethereum accounts, we choose to update the node’s embedding when the node itself engages in a new transaction, instead of updating the embeddings upon receiving transaction information, but only in the storage module, which conserves computational resources and enhances training speed.

Specifically, when node \$$ i $$ engages in a new transaction at time \$$ t $$, 2DynEthNet only needs two vectors to generate the embedding representation of node \$$ i $$, namely, the historical embedding representation of node \$$ i $$ at time \$$ t- $$ and the embedding vector of the storage module storing the historical transaction and neighbor transaction information of node \$$ i $$. 2DynEthNet utilizes these two embeddings as inputs to multi-head attention and learns the relationship between them to obtain the final embedding representation of node \$$ i $$. The mechanism of a single-head attention layer can be defined as follows:

\$$\\displaystyle \\begin{aligned} \\begin{aligned} Attn(Q, K, V) &amp;amp;=softmax\\left( \\frac{QK^{T}}{\\sqrt{d}} V\\right), \\\\ Q &amp;amp;= z(t-)W\_{Q}, \\\\ K &amp;amp; = \\beta(t)W\_{K},\\\\ V &amp;amp; = \\beta(t)W_{V} \\end{aligned} \\end{aligned} $$

(6.5)

where \$$ Q $$, \$$ K $$, and \$$ V $$ are vectors representing “query”, “key” and “value” respectively. The function \$$ Attn(Q, K, V) $$ denotes the weighted sum over the dot-product attention of entities, where the weights are determined by the interaction of entity pairs \$$ Q - K $$. Essentially, it is a mapping of a “query” to a set of “key”- “value” pairs. \$$ WQ $$, \$$ WK $$, \$$ WV $$ represent the projection weight matrices that are employed to learn the appropriate \$$ Q $$, \$$ K $$, \$$ V $$ to create an attention output with superior performance. In our model, the node embedding at the most recent update time \$$ t- $$ serves as input \$$ Q $$, and the embedding of the node storage module serves as input \$$ K $$ and \$$ V $$ to update the node embedding at time \$$ t $$, which implies that the attention module can capture the relationship between the node embedding at time \$$ t- $$ and its neighbors.

To mitigate potential biases caused by a single-attention mechanism, we employ the multi-head attention mechanism to generate multiple subspaces, which enables the model to learn various aspects of information and capture more diverse feature embeddings. Considering the dimensionality of our features, 2DynEthNet adopts a three-head attention:

\$$\\displaystyle \\begin{aligned} \\begin{aligned} head\_{i} &amp;amp;= Attn(Q\_{i}, V\_{i}, K\_{i}), i=1,2,3, \\\\ MultiHead(Q,K,V) &amp;amp;= Concat(head\_{1}, head\_{2}, head\_{3})W_{o} \\end{aligned} \\end{aligned} $$

(6.6)

where \$$W_{o} \\epsilon R^{d\\times d} $$, \$\$head_{i}\\epsilon R^{\\frac {d}{3}}\$$. Based on this, the node embedding at time \$$ t $$ is represented as:

\$$\\displaystyle \\begin{aligned} \\begin{aligned} \\widetilde{z}(t) = MultiHead(Q,K,V) \\end{aligned} \\end{aligned} $$

(6.7)

Finally, by utilizing a multi-layer perceptron (MLP), we combine the node embedding at time \$$ t $$ with that at time \$$ t- $$ (Eq. [6.8](#oebps-html-619883_1_en_6_chapter-xhtml-equ8)), which corresponds to reintegrating the previous node representation with the current aggregated information, thus enabling the update of the node state. <a id="oebps-html-619883_1_en_6_chapter-xhtml-equ8"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} z(t) = MLP(z(t-) \\Vert \\widetilde{z}(t)) \\end{aligned} \\end{aligned} $$

(6.8)

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec13"></a>

#### 6.4.3.2 Second Dimension

Facing the large scale and rapid growth of the Ethereum transaction network, we require a highly scalable model to efficiently process the continuously growing transaction data on Ethereum. However, existing static network modeling methods and single dynamic model architectures typically store the entire graph in GPU memory, resulting in a large GPU memory consumption. Moreover, for the massive influx of new data, existing methods typically partition the data by time and adopt two training methods: (1) retraining, and (2) parameter sharing. The former involves dividing the data by time and retraining the model on the new data separately to find the optimal solution, thus reducing the model’s storage costs. However, retraining causes additional training time and computational costs, which is an inefficient way. The latter, parameter sharing, makes some adjustments and improvements on this basis. Specifically, parameter sharing allows new data to share the model parameters of a previous time slice when the optimal solution was obtained, thus speeding up training and reducing computational costs. However, the Ethereum transaction network is highly affected by third-party factors such as the fluctuation of virtual digital currency prices like Ether, resulting in differences in the distribution of data features between different time slices. Therefore, sharing the optimal parameters obtained from previous training with the new time slice may lead to bias in model training and cannot guarantee that the model can necessarily achieve the optimal solution on the new time slice.

To address this issue, in the second dimension, we introduce the method of meta-learning, which can handle the issue of inconsistent optimal parameters of the model between time slices. By leveraging multiple tasks to train the meta-learning model, we enable the framework to quickly derive an accurate model under a new time slice, thus effectively enhancing the adaptability and scalability of the model to new data.

Specifically, for the continuously expanding Ethereum transaction network, we partition the newly added transaction data into 6 time slices according to the block dimension. Meta-learning treats learning the optimal parameters of the transaction network for these time slices as 6 distinct tasks. Within each task, parameters are trained and updated according to the model in the first dimension to ensure the continuity of the model. Among different tasks, 2DynEthNet utilizes the Reptile algorithm of meta-learning to learn the initialization parameters of these tasks, which enables the model to learn optimal parameters more rapidly when processing new transaction data.

The algorithmic flow of Reptile is illustrated in Table [6.1](#oebps-html-619883_1_en_6_chapter-xhtml-tab1). In each iteration, we sample a task \$$ \\tau $$ according to the order of block numbers, and then perform \$$ k $$ steps of parameter updates on that task using the model in the first dimension to obtain a new parameter vector \$$ \\widetilde {\\phi } $$. Subsequently, the current parameter vector \$$ \\phi $$ is updated to \$$ \\phi + \\varepsilon (\\widetilde {\\phi } - \\phi ) $$, where the step size \$$ \\varepsilon $$ is a hyperparameter that controls the magnitude of parameter updates. By iterating on different tasks, the Reptile algorithm continuously adjusts the model’s parameters to gradually adapt to the state of multiple tasks, thus enhancing the generalization ability of the model on new tasks. <a id="oebps-html-619883_1_en_6_chapter-xhtml-tab1"></a>

***Table 6.1***

The Reptile algorithm

| **Algorithm 1** Reptile |
| --- |
| Initialize \$$\\phi $$, the vector of initial parameters |
| **for** \$$iteration = 1, 2, \\ldots $$ **do** |
| Sample task \$$\\tau $$ , corresponding to loss \$$L_\\tau $$ on weight vectors \$\$\\widetilde {\\phi }\$$ |
| Compute \$\$\\widetilde {\\phi } = U^k_\\tau (\\phi )\$$, denoting *k* steps of parameter updating proposed by the |
| first dimension framework |
| Update \$\$\\phi \\gets \\phi + \\varepsilon (\\widetilde {\\phi } - \\phi )\$$ |
| **end for** |

The introduction of meta-learning enriches the scalability dimension of our framework, which enables 2DynEthNet to efficiently obtain optimal solutions on new Ethereum transaction data through low-cost model parameter fine-tuning without retraining existing data, thus greatly enhancing the scalability and efficiency of the model.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec14"></a>

### 6.4.4 Phishing Account Detection

In our work, we regard the detection of phishing accounts as a node classification task with the goal of distinguishing between phishing nodes and normal nodes. After the aforementioned operations, we obtain complete representations of the nodes, based on which we learn the differences between the representations of phishing nodes and normal nodes. Therefore, we consider feeding them into an Ethereum phishing node classifier. There are many choices for classifiers, and in this chapter, we choose Multilayer Perceptron (MLP), which is an artificial neural network model capable of modeling complex non-linear relationships. The key concept behind MLP is forward and backward propagation through multiple layers of neurons to optimize model parameters, thus enabling the learning and classification of complex data. The model has the advantages of being adaptable and capable of handling high-dimensional data.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec15"></a>

## 6.5 Experiments of 2DynEthNet

In this section, we perform empirical evaluations to demonstrate the effectiveness of the proposed framework 2DynEthNet. Specifically, we aim to answer the following research questions:

- **RQ1:** How effective is the proposed method 2DynEthNet for detecting phishing scam addresses on the Ethereum transaction network?
- **RQ2:** How does each designed module of 2DynEthNet (i.e., decay factor, broadcast mechanism, and storage module) contribute to the final detection performance?
- **RQ3:** How much does the performance of 2DynEthNet change by providing different numbers of neighbors receiving broadcasts or different lengths of the node storage module?
- **RQ4:** How much does the introduction of meta-learning improve the training speed of 2DynEthNet on new time slices?

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec16"></a>

### 6.5.1 Dataset Description of ETGraph and ETGraph-Labeled

In this experiment, we use two Ethereum datasets, the primary dataset is ETGraph, which contains all transactions from block height 8,000,000 to block height 8,999,999, partitioned into 6 time slices. It’s worth noting that since existing methods do not support unlabeled nodes, to extensively evaluate the performance of 2DynEthNet, we also extract a labeled dataset named ETGraph-labeled that filters unlabeled accounts, whose block height is also from 8,000,000 to 8,999,999. Detailed data information of two datasets is shown in Table [6.2](#oebps-html-619883_1_en_6_chapter-xhtml-tab2). <a id="oebps-html-619883_1_en_6_chapter-xhtml-tab2"></a>

***Table 6.2***

Statistics of the datasets used in our experiments

|  | ETGraph | ETGrpah-labeled |
| --- | --- | --- |
| Nodes | 16,841,883 | 35,386 |
| Edges | 111,262,528 | 2,456,650 |
| Edge feature dim | 16 | 16 |
| Transactions with labels | 47,039,895 | 2,456,650 |
| Scam transactions | 18,112 | 18,112 |
| Nodes with labels | 35,386 | 35,386 |
| Scam nodes | 425 | 425 |

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec17"></a>

### 6.5.2 Experimental Setup

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec18"></a>

#### 6.5.2.1 Comparison Methods

We compare our proposed framework 2DynEthNet with a variety of strong baselines for Ethereum phishing fraud detection, including three static baselines: decision tree classifiers with two different ways of feature aggregation \[[28](#oebps-html-619883_1_en_6_chapter-xhtml-cr28)], the first Ethereum transaction network representation learning method Trans2Vec \[[3](#oebps-html-619883_1_en_6_chapter-xhtml-cr3)], and three dynamic network representation learning frameworks: Dyrep \[[25](#oebps-html-619883_1_en_6_chapter-xhtml-cr25)], JODIE \[[26](#oebps-html-619883_1_en_6_chapter-xhtml-cr26)], and TGN \[[27](#oebps-html-619883_1_en_6_chapter-xhtml-cr27)]. To ensure fairness, we apply the same strategy of data preprocessing and splitting to all these methods.

- Decision Tree (DT) \[[28](#oebps-html-619883_1_en_6_chapter-xhtml-cr28)] is a supervised learning algorithm for classification tasks, which employs a tree structure to partition data layer by layer. Predictions from multiple decision trees can be averaged or summed to get a final ensemble prediction.
- Trans2Vec \[[3](#oebps-html-619883_1_en_6_chapter-xhtml-cr3)] utilizes the skip-gram algorithm of Word2Vec, which treats the neighbors of a node as ”adjacent words” to learn node embedding representations.
- DyRep \[[25](#oebps-html-619883_1_en_6_chapter-xhtml-cr25)] is a dynamic graph representation learning method that uses a Long Short-Term Memory (LSTM) network to model the evolutionary process of nodes.
- JODIE \[[26](#oebps-html-619883_1_en_6_chapter-xhtml-cr26)] adopts an RNN-based model to capture the dynamic evolution of information propagation and utilizes a graph neural network to learn user representations.
- TGN \[[27](#oebps-html-619883_1_en_6_chapter-xhtml-cr27)] is a graph neural network suitable for dynamic graph data, which considers both temporal information and graph structure to model the evolution of nodes and edges.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec19"></a>

#### 6.5.2.2 Evaluation Metrics

In this work, we use the following four metrics to have a comprehensive evaluation of the performance of different methods in Ethereum phishing fraud detection:

- **Recall:** Recall refers to the proportion of phishing accounts that are correctly predicted as phishing accounts.
- **AUC (Area Under Curve):** The AUC metric calculates the area under the ROC curve formed by TPR and FPR for multiple thresholds, which is commonly used in binary classification tasks. The higher the AUC-ROC value, the better the model’s ability to discriminate between true positives and false positives, which indicates more accurate classification judgments between positive and negative examples.
- **F1-score:** F1-score is a combined evaluation of Precision and Recall, which is the harmonic mean of the two, where Precision refers to the percentage of real phishing nodes among the accounts determined to be suspicious, and Recall refers to the percentage of known phishing node samples detected.
- **FPR (False Positive Rate):** FPR refers to the proportion of normal accounts that are incorrectly predicted as phishing accounts.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec20"></a>

#### 6.5.2.3 Implementation Details

For both datasets, train/val/test sets are split with a ratio of 70/15/15. We use the Adam optimizer with a learning rate of 0.0001, a dropout rate of 0.1, and early stopping with patience of 5. Since timestamp is treated as an independent feature, we input a feature dimension of 15 for the multi-headed attention, with the number of attention heads set to 3. For the MLP network, we employ a two-layer neural network with a hidden layer dimension of 7. The node embedding dimension of our framework is fixed as 10. Notably, the number of neighbors receiving the broadcast and the length of the storage module are variable, and we perform subsequent experiments to compare their impact on the performance of 2DynEthNet in different settings. The experiments are conducted on a Linux server equipped with an Intel Core i9-9940X CPU (14 cores, 3.30 GHz) and RTX 2080 Ti GPU.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec21"></a>

### 6.5.3 Effectiveness Results

To answer RQ1, we evaluate the performance of all the compared methods in the task of Ethereum phishing scam detection. As baseline methods do not support unlabeled data, we conduct experiments on baselines on the labeled dataset ETGraph-labeled and 2DynEthNet on the unlabeled dataset ETGraph. Additionally, since nodes in the Ethereum dataset lack original features and static methods rely on nodes’ original features as model inputs, we manually aggregate edge features into node features to conduct experiments for static baselines.

Experimental results of 2DynEthNet and all baseline methods on six time slices for Ethereum phishing fraud detection are presented in Table [6.3](#oebps-html-619883_1_en_6_chapter-xhtml-tab3). We can draw the following conclusions: <a id="oebps-html-619883_1_en_6_chapter-xhtml-tab3"></a>

***Table 6.3***

Performance comparison results w.r.t. Recall, AUC, F1-score and FPR on six time slices

| Method | Metric | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2DynEthNet | Recall | **88.26** | **71.98** | **90.32** | **89.53** | **91.25** | **90.34** |
|  | AUC | **89.27** | **84.47** | **88.43** | **90.62** | **94.07** | **91.51** |
|  | F1-score | **84.52** | **82.31** | **89.34** | **88.75** | **90.21** | **89.31** |
|  | FPR | 15.00 | 15.05 | **10.21** | 14.00 | 21.00 | 25.03 |
| DT-Mean | Recall | 39.52 | 50.33 | 47.76 | 51.89 | 59.14 | 53.27 |
|  | AUC | 46.89 | 56.24 | 52.18 | 63.75 | 63.90 | 54.32 |
|  | F1-score | 36.30 | 42.84 | 39.88 | 58.19 | 61.52 | 49.87 |
|  | FPR | 15.73 | 18.24 | 12.89 | 12.43 | 14.32 | 20.13 |
| DT-Sum | Recall | 38.21 | 52.64 | 49.15 | 57.21 | 61.78 | 55.67 |
|  | AUC | 49.81 | 57.61 | 55.37 | 69.70 | 70.25 | 59.83 |
|  | F1-score | 58.21 | 53.78 | 59.45 | 72.90 | 71.32 | 60.51 |
|  | FPR | 14.63 | 20.11 | 11.79 | 15.42 | 13.35 | 18.43 |
| Trans2Vec | Recall | 46.72 | 50.43 | 48.12 | 56.57 | 52.48 | 49.21 |
|  | AUC | 56.94 | 60.83 | 58.92 | 69.19 | 71.21 | 61.25 |
|  | F1-score | 58.31 | 60.71 | 61.24 | 59.43 | 73.21 | 64.31 |
|  | FPR | 17.89 | 16.85 | 20.31 | 15.43 | **13.24** | 12.12 |
| TGN | Recall | 79.28 | 72.15 | 80.73 | 67.89 | 66.42 | 73.51 |
|  | AUC | 83.27 | 74.91 | 79.56 | 82.03 | 70.48 | 86.72 |
|  | F1-score | 71.23 | 86.45 | 72.89 | 81.57 | 75.32 | 84.68 |
|  | FPR | 14.76 | 19.82 | 10.49 | 23.57 | 12.93 | 17.35 |
| JODIE | Recall | 61.24 | 59.89 | 62.47 | 68.92 | 71.11 | 67.35 |
|  | AUC | 83.72 | 75.89 | 72.56 | 79.34 | 86.21 | 71.48 |
|  | F1-score | 71.28 | 83.67 | 76.45 | 81.89 | 88.12 | 72.55 |
|  | FPR | 15.42 | **10.87** | 13.56 | 24.09 | 14.78 | 21.35 |
| DyRep | Recall | 57.24 | 62.89 | 55.78 | 68.32 | 51.67 | 59.45 |
|  | AUC | 72.36 | 69.12 | 73.89 | 86.24 | 70.57 | 88.93 |
|  | F1-score | 54.76 | 59.32 | 52.89 | 63.45 | 56.78 | 86.21 |
|  | FPR | **12.47** | 16.89 | 21.32 | **9.78** | 14.56 | **8.21** |

The best results are marked in bold

1. (1)

   Our 2DynEthNet outperforms all the other compared methods by a significant margin on Recall, AUC, and F1-score three evaluation metrics. In phishing fraud detection tasks, it is crucial to ensure that as many phishing accounts as possible are detected to minimize false negatives. This is because in the Ethereum network, phishing accounts typically defraud large sums of money from multiple accounts, and false negatives in detecting phishing accounts could lead to significant economic losses, severely impacting the Ethereum transaction ecosystem. Recall reflects the coverage of detected phishing accounts among all actual phishing accounts, making it a critical metric in scam detection tasks. 2DynEthNet demonstrates superior performance in Recall compared to other methods, indicating that our model possesses stronger capabilities in identifying phishing accounts and achieves better performance in scam detection tasks.

   However, placing excessive emphasis on the Recall metric may increase the probability of the model incorrectly identifying normal accounts as phishing nodes, thus affecting normal transactions on the Ethereum platform. Therefore, the model also needs to pay attention to the performance of the FPR metric. A high FPR value indicates that the model generates a large number of false alarms, so the model is ideally expected to achieve as low an FPR value as possible. The results illustrate that although our method did not achieve the optimal result in terms of FPR, it perform comparably to baseline methods.

   To comprehensively evaluate the performance of the model, we also introduced AUC and F1-score metrics. AUC provides a comprehensive assessment of the model’s performance in terms of both Recall and FPR, while F1-score evaluates the model’s performance in terms of both precision and Recall. The results indicate that our method achieved the best results on both of these metrics, outperforming other baseline methods in overall scam detection performance.

2. (2)

   Compared to static methods, our 2DynEthNet significantly outperforms them in terms of Recall, AUC, and F1-score metrics. DT-Mean and DT-Sum aggregate transaction features of each node and their first-order transaction neighbors using different strategies (taking the average or sum) to form node features, and then train decision trees for node classification, thus neglecting the network’s topological and dynamic evolution features. Although Trans2Vec can learn some network topological features through random walks, it still fails to capture the network’s dynamic evolution features, and the biased random walk may lead to information loss to some extent. It’s worth noting that the transaction features used here are extracted from our dataset ETGraph. Although DT-Mean and DT-Sum perform poorly in scam detection tasks, their Recall and AUC values exceeding 50% on partial time slices can effectively demonstrate the validity of the edge features we extracted.

3. (3)

   Compared to dynamic methods, our 2DynEthNet performs better overall on evaluation metrics. While dynamic methods can learn certain dynamic features of Ethereum transaction network evolution, they do not generally perform as well as 2DynEthNet on the evaluation metrics. This suggests that these three dynamic methods may not be well-suited for the Ethereum scenario. The reason lies in the fact that the graph querying and reasoning processes of these dynamic methods are not decoupled. These methods are constrained by their inability to handle unlabeled nodes, thus being limited to training and learning on locally labeled graphs, resulting in the loss of topological structure information of the network. Consequently, these models can not adapt well to the large-scale and feature-sparse Ethereum transaction data. On the other hand, our 2DynEthNet comprehensively considers the historical behavioral features of accounts and neighbor transaction features, and propagates information across the entire graph using unlabeled nodes, mitigating to some extent the impact of imbalanced positive and negative samples on model training. Additionally, as the Ethereum transaction network is highly sparse, our model supports processing data across the entire graph to allow 2DynEthNet to learn more implicit features, thus enhancing its ability to identify phishing accounts.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec22"></a>

### 6.5.4 Ablation Study

To answer RQ2 and validate the effectiveness of our innovation, we eliminated the decay factor (i.e., 2DynEthNet/d), the broadcasting mechanism (i.e., 2DynEthNet/b), and the storage module (i.e., 2DynEthNet/s) respectively. As shown in Table [6.4](#oebps-html-619883_1_en_6_chapter-xhtml-tab4), different module designs have varying degrees of improvement in the phishing fraud detection performance of 2DynEthNet. The corresponding observation results have the following aspects: <a id="oebps-html-619883_1_en_6_chapter-xhtml-tab4"></a>

***Table 6.4***

AUC, Recall, FPR and F1-score results of 2DynEthNet and its variant

|  | AUC | Recall | FPR | F1-score |
| --- | --- | --- | --- | --- |
| 2DynEthNet/d | 94.35 | 65.31 | 11.23 | 92.15 |
| 2DynEthNet/b | 78.34 | 32.81 | 10.00 | 75.82 |
| 2DynEthNet/s | 65.03 | 27.48 | 18.05 | 61.95 |
| 2DynEthNet | 96.26 | 90.08 | 13.79 | 92.39 |

1. (1)

   The storage module contributes the most to the performance of phishing fraud detection. After removing the storage module, the performance of 2DynEthNet/s dramatically declines, with decreases of 32.4% and 69.4% compared to 2DynEthNet in AUC and Recall positive evaluation metrics respectively. This indicates that in the Ethereum transaction network, both the historical behavior of accounts and neighbor information have a significant impact on the subsequent behavior of accounts, and learning from this feature information can significantly improve the accuracy of representation learning models. Additionally, we find that encoding the importance of historical information in the storage module also improves the model’s performance to some extent. 2DynEthNet/d exhibits decreases of 2% and 27.5% in AUC and Recall metrics compared to 2DynEthNet respectively, indicating that the importance of transaction information varies depending on the node’s neighbors.

2. (2)

   Removing the broadcasting mechanism, 2DynEthNet/b also shows a significant decline in performance on the evaluation metrics AUC and Recall, with decreases of 18.6% and 63.6% compared to 2DynEthNet respectively. This implies that our framework relies solely on the historical transaction information of target nodes to learn node embeddings, which cannot yield accurate detection results.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec23"></a>

### 6.5.5 Sensitivity Analysis

To answer RQ3, we further evaluate the impact of different numbers of broadcast neighbors and different lengths of storage modules on the performance of 2DynEthNet. Figure [6.3](#oebps-html-619883_1_en_6_chapter-xhtml-fig3) illustrates how adjusting the number of broadcast neighbors and the length of node storage modules affects the key metric Recall in the scam detection task. Specifically, we observe that under different numbers of broadcast neighbors and lengths of node storage modules, there are significant variations in Recall performance, and it does not follow the logic that the higher the number of received broadcast neighbors and the longer the node storage module, the higher the Recall metric. This indicates that to achieve optimal detection, it is necessary to carefully set the number of broadcast neighbors and the length of node storage modules.<a id="oebps-html-619883_1_en_6_chapter-xhtml-fig3"></a>

***Fig. 6.3***

Model robustness study of 2DynEthNet with different numbers of neighbors receiving the broadcast and the length of storage modules

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec24"></a>

### 6.5.6 Efficiency Performance

To address RQ4, we further evaluate the training speed performance of 2DynEthNet on new time slices with the introduction of meta-learning. Figures [6.4](#oebps-html-619883_1_en_6_chapter-xhtml-fig4) and [6.5](#oebps-html-619883_1_en_6_chapter-xhtml-fig5) respectively present the time and number of epochs required for 2DynEthNet to reach optimal solutions for six tasks w/ and w/o meta-learning. It can be seen that the design of the second dimension of 2DynEthNet significantly reduces the time required for the model to reach an optimal solution, greatly enhancing the performance of the model.<a id="oebps-html-619883_1_en_6_chapter-xhtml-fig4"></a>

***Fig. 6.4***

The time(s) required for 2DynEthNet to reach optimal solutions for six tasks w/ and w/o meta-learning

<a id="oebps-html-619883_1_en_6_chapter-xhtml-fig5"></a>

***Fig. 6.5***

The number of epochs required for 2DynEthNet to reach optimal solutions for six tasks w/ and w/o meta-learning

<a id="oebps-html-619883_1_en_6_chapter-xhtml-sec25"></a>

## 6.6 Conclusion

In this chapter, we propose a continuous dynamic and scalable two-dimensional streaming framework 2DynEthNet to enhance the performance of Ethereum phishing fraud detection. Within time slices, 2DynEthNet utilizes edge features to capture each transaction streaming and broadcasts transaction information to its neighbors through unlabeled nodes via a broadcast mechanism. Simultaneously, our model combines neighbor transaction features, current transaction features, and historical features of the current node to achieve a strong node representation capability. Between time slices, 2DynEthNet adopts a strategy of incremental information training which utilizes meta-learning to quickly update model parameters under new time slices, thus significantly improving the efficiency and scalability of the model. Additionally, we provide a new large-scale dynamic graph transaction dataset, ETGraph, which fits real Ethereum transaction scenarios without biased sampling and filtering of unlabeled accounts. Extensive experiments demonstrate that the phishing fraud detection performance and practicality of 2DynEthNet significantly outperform state-of-the-art methods.

<a id="oebps-html-619883_1_en_6_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr1"></a>EagleEye, B.: Beosin: the total cost of web3 security incidents in the first half of 2023 exceeded \$650 million. [https://bicoin8.com/321467.html](https://bicoin8.com/321467.html) (2023)
2. 2\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr2"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding Ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. II: Express Briefs **67**(11), 2737–2741 (2020)
3. 3\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr3"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
4. 4\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr4"></a>Liu, J., Zheng, J., Wu, J., Zheng, Z.: FA-GNN: filter and augment graph neural networks for account classification in ethereum. IEEE Trans. Netw. Sci. Eng. **9**(4), 2579–2588 (2022)[Crossref](https://doi.org/10.1109/TNSE.2022.3166655)
5. 5.Anita, N., Vijayalakshmi, M.: Blockchain security attack: a brief survey. In: Proceedings of the 10th International Conference on Computing, Communication and Networking Technologies (ICCCNT), pp. 1–6. IEEE (2019)
6. 6\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr6"></a>Chen, J., Xiong, H., Zhang, D., Liu, Z., Wu, J.: Tegdetector: a phishing detector that knows evolving transaction behaviors. Comput. Res. Repository. abs/2111.15446 (2021)
7. 7\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr7"></a>Li, S., Xu, F., Wang, R., Zhong, S.: Self-supervised incremental deep graph learning for ethereum phishing scam detection. arXiv preprint arXiv:2106.10176 (2021)
8. 8\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr8"></a>Li, W., Xie, J., Xin, M., Mo, J.: An overlapping network community partition algorithm based on semi-supervised matrix factorization and random walk. Expert Syst. Appl. **91**, 277–285 (2018)[Crossref](https://doi.org/10.1016/j.eswa.2017.09.007)
9. 9\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr9"></a>Scarselli, F., Gori, M., Tsoi, A.C., Hagenbuchner, M., Monfardini, G.: The graph neural network model. IEEE Trans. Neural Netw. **20**(1), 61–80 (2009)[Crossref](https://doi.org/10.1109/TNN.2008.2005605)
10. 10\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr10"></a>Chen, W., Guo, X., Chen, Z., Zheng, Z., Lu, Y.: Phishing scam detection on Ethereum: towards financial security for blockchain ecosystem. In: Proceedings of the Twenty-Ninth International Joint Conference on Artificial Intelligence, pp. 4506–4512. ijcai.org (2020)
11. 11\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr11"></a>Perozzi, B., Al-Rfou, R., Skiena, S.: Deepwalk: online learning of social representations. In: Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 701–710. Association for Computing Machinery (2014)
12. 12\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr12"></a>Cui, Z., Li, Z., Wu, S., Zhang, X., Liu, Q., Wang, L., Ai, M.: DyGCN: efficient dynamic graph embedding with graph convolutional network. IEEE Trans. Neural Netw. Learn. Syst. **35**(4), 4635–4646 (2024)[Crossref](https://doi.org/10.1109/TNNLS.2022.3185527)
13. 13\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr13"></a>Grover, A., Leskovec, J.: Node2vec: scalable feature learning for networks. In: Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 855–864. Association for Computing Machinery, San Francisco (2016)
14. 14\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr14"></a>Chen, L., Peng, J., Liu, Y., Li, J., Xie, F., Zheng, Z.: Phishing scams detection in ethereum transaction network. ACM Trans. Internet Technol. **21**(1), 1–16 (2020)[Crossref](https://doi.org/10.1145/3398071)
15. 15\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr15"></a>Li, S., Gou, G., Liu, C., Hou, C., Li, Z., Xiong, G.: Ttagn: temporal transaction aggregation graph network for ethereum phishing scams detection. In: Proceedings of the ACM Web Conference 2022, pp. 661–669. Association for Computing Machinery, New York (2022)
16. 16\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr16"></a>Hisano, R.: Semi-supervised graph embedding approach to dynamic link prediction. In: International Workshop on Complex Networks, pp. 109–121. Springer (2018)
17. 17.Ibrahim, N.M.A., Chen, L.: Link prediction in dynamic social networks by integrating different types of information. Appl. Intell. **42**(4), 738–750 (2015)[Crossref](https://doi.org/10.1007/s10489-014-0631-0)
18. 18\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr18"></a>Ahmed, N.M., Chen, L.: An efficient algorithm for link prediction in temporal uncertain social networks. Inf. Sci. **331**, 120–136 (2016)[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3425891)[Crossref](https://doi.org/10.1016/j.ins.2015.10.036)
19. 19\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr19"></a>Yao, L., Wang, L., Pan, L., Yao, K.: Link prediction based on common-neighbors for dynamic social network. Proc. 2016 Proc. Comput. Sci. **83**, 82–89 (2016)
20. 20.Zhu, J., Xie, Q., Chin, E.J.: A hybrid time-series link prediction framework for large social network. In: Proceedings of International Conference on Database and Expert Systems Applications, pp. 345–359. Springer (2012)
21. 21\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr21"></a>Seo, Y., Defferrard, M., Vandergheynst, P., Bresson, X.: Structured sequence modeling with graph convolutional recurrent networks. In: Proceedings of International Conference on Neural Information Processing, pp. 362–373. Springer (2018)
22. 22\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr22"></a>Moradabadi, B., Meybodi, M.R.: A novel time series link prediction method: learning automata approach. Phys. A: Stat. Mech. Appl. **482**, 422–432 (2017)[Crossref](https://doi.org/10.1016/j.physa.2017.04.019)
23. 23\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr23"></a>Pareja, A., Domeniconi, G., Chen, J., Ma, T., Suzumura, T., Kanezashi, H., Kaler, T., Schardl, T., Leiserson, C.: Evolvegcn: evolving graph convolutional networks for dynamic graphs. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 34, no. 04, pp. 5363–5370 (2020)
24. 24\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr24"></a>Manessi, F., Rozza, A., Manzo, M.: Dynamic graph convolutional networks. Pattern Recognit. **97**, 107000 (2020)[Crossref](https://doi.org/10.1016/j.patcog.2019.107000)
25. 25\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr25"></a>Trivedi, R., Farajtabar, M., Biswal, P., Zha, H.: Dyrep: learning representations over dynamic graphs. In: Proceedings of the 7th International Conference on Learning Representations. OpenReview.net (2019)
26. 26\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr26"></a>Van Wijk, B.C., Stam, C.J., Daffertshofer, A.: Comparing brain networks of different size and connectivity density using graph theory. Public Library Sci. **5**(10), e13701 (2010)
27. 27\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr27"></a>Rossi, E., Chamberlain, B., Frasca, F., Eynard, D., Monti, F., Bronstein, M.: Temporal graph networks for deep learning on dynamic graphs. arXiv preprint arXiv:2006.10637 (2020)
28. 28\.<a id="oebps-html-619883_1_en_6_chapter-xhtml-cr28"></a>Quinlan, J.R.: Induction of decision trees. Mach. Learn. **1**(1), 81–106 (1986)[Crossref](https://doi.org/10.1007/BF00116251)

<a id="oebps-html-619883_1_en_7_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_7](https://doi.org/10.1007/978-981-97-4430-5_7)

# 7. Account Risk Rating Based on Network Propagation Algorithm

Dan Lin[1](#oebps-html-619883_1_en_7_chapter-xhtml-aff4) , Jiajing Wu[1](#oebps-html-619883_1_en_7_chapter-xhtml-aff4) , Qishuang Fu[1](#oebps-html-619883_1_en_7_chapter-xhtml-aff4) , Zhe Chen[2](#oebps-html-619883_1_en_7_chapter-xhtml-aff5) and Zibin Zheng[1](#oebps-html-619883_1_en_7_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_7_chapter-xhtml-aff5"></a>

(2)The University of Hong Kong, Pok Fu Lam, Hong Kong

<a id="oebps-html-619883_1_en_7_chapter-xhtml-contactofauthor1"></a>

**Dan Lin (Corresponding author)Email:** [lind8@mail2.sysu.edu.cn](mailto:lind8@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-contactofauthor2"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-contactofauthor3"></a>

**Qishuang FuEmail:** [fuqsh6@mail2.sysu.edu.cn](mailto:fuqsh6@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-contactofauthor5"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

Existing risk control techniques have primarily been developed from the perspectives of de-anonymizing address clustering and illicit account classification. However, these techniques cannot be used to ascertain the potential risks for all accounts and are limited by specific heuristic strategies or insufficient label information. These constraints motivate us to seek an effective rating method for quantifying the spread of risk in a transaction network. To the best of our knowledge, we are the first to address the problem of account risk rating on Ethereum by proposing a novel model called RiskProp, which includes a de-anonymous score to measure transaction anonymity and a network propagation mechanism to formulate the relationships between accounts and transactions. We demonstrate the effectiveness of RiskProp in overcoming the limitations of existing models by conducting experiments on real-world datasets from Ethereum. Through case studies on the detected high-risk accounts, we demonstrate that the risk assessment by RiskProp can be used to provide warnings for investors and protect them from possible financial losses, and the superior performance of risk score-based account classification experiments further verifies the effectiveness of our rating method.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec1"></a>

## 7.1 Introduction

Risk control \[[1](#oebps-html-619883_1_en_7_chapter-xhtml-cr1)] not only helps wallet customers identify risky accounts and avoid losses but also plays a vital role in the anti-money laundering of virtual asset service providers, such as cryptocurrency exchanges.

Therefore, a wealth of efforts have been expended in risk control on Ethereum in recent years. In September 2020, the Financial Action Task Force (FATF) published a recommendation report on virtual assets and released information on *Red Flag Indicators* \[[2](#oebps-html-619883_1_en_7_chapter-xhtml-cr2)] related to transactions, anonymity, senders or recipients, the source of funds, and geographical risks. In addition, researchers in the academic community have proposed various techniques from the perspectives of address clustering and illicit account classification. Address clustering techniques perform entity identification of anonymous accounts. For example, Victor \[[3](#oebps-html-619883_1_en_7_chapter-xhtml-cr3)] proposes several clustering heuristics for Ethereum accounts and clusters 17.9% of all active externally owned accounts. Illicit account detection techniques focus on training classifiers based on well-designed features extracted from transactions \[[4](#oebps-html-619883_1_en_7_chapter-xhtml-cr4)–[6](#oebps-html-619883_1_en_7_chapter-xhtml-cr6)]. Moreover, some researchers have developed methods for automatic feature extraction incorporating structural information \[[7](#oebps-html-619883_1_en_7_chapter-xhtml-cr7)–[10](#oebps-html-619883_1_en_7_chapter-xhtml-cr10)].

However, there are still some limitations (L) associated with these techniques. **L1:** Account clustering techniques can only be applied to part of accounts and therefore have limited applicability, and most accounts beyond heuristic rules cannot thus be identified. **L2:** In the existing methods for illicit account detection, *binary* classifiers are usually trained via *supervised* learning. However, as only a very small percentage of risky nodes have clear labels, which are required for these methods, the vast majority of accounts that may be involved in malicious events are unlabeled. In particular, risky accounts with few transactions or unseen patterns are likely to be misidentified in practical use.

To address the limitations presented above, we explore risk control on Ethereum from a new perspective: *Account risk rating*. In traditional financial scenarios, credit scoring is usually conducted by authorized financial institutions, which perform audits on their customers to fully understand their identity, background, and financial credit standing. Similarly to credit scoring, risk rating on Ethereum can help us quantify the latent risk of a transaction or account with a quantitative score, thereby combating money laundering and identifying potential scams before new victims emerge. In terms of the abovementioned **L1**, in contrast to the traditional account clustering method, which can only de-anonymize a small number of accounts, the account risk method proposed in this chapter can obtain quantitative risk indicators for *all* accounts. Regarding **L2**, the proposed risk rating method can achieve decent performance in an unsupervised manner without feeding labels. The output of the proposed method is risk values, which are provided continuously and allow evaluation of the severity of risk.

Compared with traditional financial scenarios, several unique challenges (C) are encountered in the task of account risk rating on Ethereum. **C1: Nature of anonymity.** Transactions on Ethereum do not require real-name verification. Even worse, perpetrators of some malicious activities deliberately enhance their anonymity to counter the impact of de-anonymizing clustering techniques \[[7](#oebps-html-619883_1_en_7_chapter-xhtml-cr7)]. **C2: Complex transaction relationship.** Compared with traditional financial scenarios, a user or entity on Ethereum may control a large number of accounts at almost no cost, and the transaction relationship between accounts is also more complex. How to quantify the impact of trading behavior between accounts on account risk is a challenging core problem.

To overcome the challenges mentioned above, we propose a novel approach called Risk Propagation (*RiskProp*) for Ethereum account rating. It comprises two core designs, namely de-anonymous score and a network propagation mechanism. To resolve **C1**, de-anonymous score measures the degree to which transactions remain anonymous. For example, both the payer and the payee of an illicit transaction prefer to have a small number of transactions to ensure anonymity-preserving protection. In contrast, both sides of a licit transaction may participate in numerous interactions without evading the impact of the de-anonymized clustering algorithm. Afterward, to resolve **C2**, we model the massive transaction records as a directed bipartite graph and introduce a network propagation mechanism with three interdependent metrics, namely *Confidence* of the de-anonymous score, *Trustiness* of the payee, and *Reliability* of the payer. Intuitively, payees with higher trustiness receive transactions with higher de-anonymous scores, and payers with higher reliability will send transactions with higher confidence. Clearly, reliability, trustiness, and confidence are related to each other, so we define five items of prior knowledge that these metrics should satisfy and propose three mutually recursive equations to estimate the values of these metrics. To verify the effectiveness of the proposed risk rating method and further illustrate the significance of rating for risk control on Ethereum, we evaluate the effect of the risk rating system via experiments from two aspects, i.e., analysis of risk rating results and rating score-based illicit/licit classification.

Overall, our contributions are summarized as follows:

- **A new perspective for Ethereum risk control.** This chapter is the first to propose tackling the problem of Ethereum risk control via the perspective of account risk rating.
- **A novel risk metric for transactions.** We creatively develop a metric called *de-anonymous score* for transactions, which measures the degree of de-anonymization to quantify the risk of a transaction.
- **An effective method and interesting insights.** We implement a novel risk rating method called *RiskProp* and demonstrate its superior effectiveness and efficiency via experiments on a real-world Ethereum transaction dataset together with theoretical analysis. By analyzing the rating results and case studies on high-risk accounts, we obtain interesting insights into the Ethereum ecosystem and further show how our method could prevent financial losses ahead of blacklisting malicious accounts.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec2"></a>

## 7.2 Preliminary

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec3"></a>

### 7.2.1 Ethereum Financial Background

Ether can be paid or received in financial activities, just like currency in real life. In conventional financial scenarios, a Know Your Customer (KYC) check is the mandatory process to identify and verify a customer’s identity when opening an account and to periodically understand the legitimacy of the involved funds over time. However, unlike traditional transaction systems, where customers’ identity information is required and obtained in KYC checks, Ethereum accounts are designed as pseudonymous addresses identified by 20 bytes of public key information generated by cryptographic algorithms, for example, “0x99f154f6a393b088a7041f1f5d0a7cbfa795d301”.

Figure [7.1](#oebps-html-619883_1_en_7_chapter-xhtml-fig1) depicts the risky scenario of Ether transfer in aspects of data acquisition. It includes three layers: (1) Ethereum blockchain. The Ethereum historical data are irreversible and publicly traceable on the chain. (2) Public transactions. The transaction denotes a signed data package from an account to another account, including the sending address, receiver address, transferred Ether amount, etc. (3) Account risk rating. Usually, the identities who control the accounts are not labeled. Customers may become involved in suspicious financial crimes or be vulnerable to frauds and scams. Furthermore, the illicit funds can be laundered and cashed out via exchanges. In this procedure, our proposed *RiskProp* is implemented to measure the risk of unlabeled accounts that may have ill intentions and alert customers when engaging in suspicious, potentially illegal transactions.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig1"></a>

***Fig. 7.1***

The procedure of ETH transfer in Ethereum. “From” denotes the sender, “To” denotes the receiver, and “Txn” denotes “Transaction”

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec4"></a>

### 7.2.2 The Nature of Blockchain: Anonymity

It is known that the Ethereum account is identified as a pseudonymous address. However, if customers repeatedly use the same address as on-chain identification, the relationship between addresses becomes linkable via public transaction records. Accounts that participate in more transactions and connect with more accounts experience degrading anonymity \[[7](#oebps-html-619883_1_en_7_chapter-xhtml-cr7)]. To reduce the likelihood of exposure, criminals naturally tend to initiate transactions with fewer accounts. Here is an example on Ethereum: The two accounts of transaction [0x9a9d](https://cn.etherscan.com/tx/0x9a9df5e68a8cbb30e901024367c88dd3401b455a5916204753ebda6070bccde9) have only three transactions and became inactive thereafter. These two accounts are considered suspicious and reported as relevant [accounts of Upbit exchange hack](https://cn.etherscan.com/accounts/label/upbit-hack). On the contrary, entities who do not deliberately take anonymity-preserving measures are likely to be normal \[[7](#oebps-html-619883_1_en_7_chapter-xhtml-cr7)]. Thus, the transaction is scored based on the fact of whether the accounts are trying to hide or not, which is the *de-anonymous score*.

**Definition 1 (De-anonymous Score, Abbreviated as “Score”)**

The de-anonymous score of a transaction from account *u* to *v* where there is no intention to hide is defined as <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ1"></a>

\$$\\displaystyle \\begin{aligned} \\begin{aligned} Score(u, v) = &amp;amp; \\frac{1}{2}(\\frac{2\\log |OutTxn(u)|-\\log maxOut}{\\log maxOut} \\\\ &amp;amp;+ \\frac{2\\log |InTxn(v)|-\\log maxIn}{\\log maxIn}), \\end{aligned} {} \\end{aligned} $$

(7.1)

where \$\$OutTxn(u)\$$ represents the outgoing transactions (payments) of payer *u*, \$\$InTxn(v)\$$ represents the incoming transactions (receptions) of payee *v*, and \$\$|\\times |\$$ denotes the size of a set. The minimum value of \$\$|OutTxn(u)|\$$ and \$\$|InTxn(v)|\$$ is 1. Let *maxOut* and *maxIn* be the largest number of payments and receptions, respectively. The de-anonymous scores of a transaction \$\$(u, v)\$$ range from \$\$-1\$$ (very high anonymity, abnormal) to 1 (very low anonymity, normal). Intuitively, the score of \$\$(u, v)\$$ increases as the transaction numbers of either payer or payee grow. Note that tricky criminals may camouflage themselves by deliberately conducting low-anonymity transactions \[[11](#oebps-html-619883_1_en_7_chapter-xhtml-cr11)].

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec5"></a>

### 7.2.3 Transaction Network Construction

First, each transaction on Ethereum has one payer (i.e., sender) and one payee (i.e., receiver). Any account can be the role of payer or payee, just as a person in real life has different roles. The payee is a *passive* role and, therefore, we consider the incoming transactions to indicate the trustiness of an account. For instance, exchange accounts that receive more transactions are considered to be more trustworthy. In contrast, the payer is an *active* role and, thus, the outgoing transactions embody the intention of an account. For example, a scam account subjectively wants to transfer stolen money to its partners.

Next, the transaction records are modeled as a directed bipartite graph \$\$G=(U, V, S)\$$, where *U*, *V* , and *S* represent the set of all payers, payees, and scores, respectively. A weighted edge \$\$(u, v)\$$ denotes the transfer of Ethers from account \$\$u\\in U\$$ to account \$\$v\\in V\$$ with \$\$Score(u, v) \\in S\$$. The graph construction procedure is shown in Fig. [7.2](#oebps-html-619883_1_en_7_chapter-xhtml-fig2).<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig2"></a>

***Fig. 7.2***

The transformation from the raw transaction records to the directed bipartite graph. “Txn” denotes “Transaction”

Then, the ego network of a payer *u* is introduced. It is formed by its outgoing scores and corresponding payee neighbors, formulated as \$\$Out(u)\\cup \\{v|(u,v)\\in Out(u)\\}\$$, where \$\$Out(u)\$$ is the set of scores connected with *u*. It is similar to the ego network of a payee, formulated as \$\$In(v)\\cup \\{u|(u,v)\\in In(v)\\}\$$. Figure [7.3](#oebps-html-619883_1_en_7_chapter-xhtml-fig3) shows an example in which there are two payers, two payees, and three transactions.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig3"></a>

***Fig. 7.3***

A toy example of the directed bipartite graph established from transactions and the illustration of functions *In* and *Out*

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec6"></a>

## 7.3 Related Work

**Risk Control Studies in Cryptocurrency**

In recent years, there has been growing interest in account clustering and detecting illicit activities (e.g., financial scams, money laundering) in cryptocurrency transaction networks \[[12](#oebps-html-619883_1_en_7_chapter-xhtml-cr12)]. Victor \[[3](#oebps-html-619883_1_en_7_chapter-xhtml-cr3)] is the first to propose clustering heuristics for Ethereum’s account model, including deposit address reuse, airdrop multi-participation, and self-authorization. A recent review of the literature on cryptocurrency scams \[[13](#oebps-html-619883_1_en_7_chapter-xhtml-cr13)] showed that the existing methods (e.g., \[[4](#oebps-html-619883_1_en_7_chapter-xhtml-cr4), [14](#oebps-html-619883_1_en_7_chapter-xhtml-cr14)], and \[[15](#oebps-html-619883_1_en_7_chapter-xhtml-cr15)]) are mainly based on supervised classifiers fed with handcrafted features. Many attempts have been made \[[5](#oebps-html-619883_1_en_7_chapter-xhtml-cr5), [7](#oebps-html-619883_1_en_7_chapter-xhtml-cr7), [16](#oebps-html-619883_1_en_7_chapter-xhtml-cr16)] to incorporate structural information by learning the latent representations of accounts. Some researchers have investigated and modeled the money flow from a network perspective \[[9](#oebps-html-619883_1_en_7_chapter-xhtml-cr9), [17](#oebps-html-619883_1_en_7_chapter-xhtml-cr17)] to better identify illicit activities. After all, there is still a black area regarding the estimation of the risk value of Ethereum accounts, which is the key task in alerting about suspicious accounts and transactions on the chain.

**Rating and Ranking on Graph Data**

The aim of ratings and rankings on graph data is to provide a score or an order for each node in a graph. Currently, the main solutions are based on link analysis technique \[[18](#oebps-html-619883_1_en_7_chapter-xhtml-cr18)], Bayesian model \[[19](#oebps-html-619883_1_en_7_chapter-xhtml-cr19)], and iterative learning \[[20](#oebps-html-619883_1_en_7_chapter-xhtml-cr20)], etc. Similarly to the proposed *RiskProp* algorithm, \[[21](#oebps-html-619883_1_en_7_chapter-xhtml-cr21)] proposed axioms and iterative formulations to establish the relationship between ratings. In \[[22](#oebps-html-619883_1_en_7_chapter-xhtml-cr22)], the authors measured the bias and prestige of nodes in networks based on trust scores. In \[[23](#oebps-html-619883_1_en_7_chapter-xhtml-cr23)], the authors highlighted that graph-based approaches provide unique solution opportunities for financial crime and fraud detection. A review on this topic \[[24](#oebps-html-619883_1_en_7_chapter-xhtml-cr24)] described the problems in current studies: lack of ground truths, imbalanced class, and large-scale network. These challenges also exist in our risk rating problem on Ethereum transaction networks.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec7"></a>

## 7.4 Methodology of Account Risk Rating

In this section, we describe the prior knowledge that establishes the relationships among accounts and transactions and then propose risk propagation formulations that satisfy the prior knowledge. It is worth noticing that the proposed algorithm does not require handcraft feature engineering.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec8"></a>

### 7.4.1 Problem Definition and Model Overview

Given raw transaction records of Ethereum, we model the transaction relationships between accounts as a directed bipartite graph \$\$G=(U, V, S)\$$ with payers and payees as nodes and prepossessed de-anonymous scores as weights of edges. We believe that accounts have intrinsic metrics to quantify their reliability and trustworthiness and transactions have intrinsic metrics to measure the confidence of their calculated de-anonymous scores. Naturally, those metrics are interdependent and interplay with each other via the risk propagation mechanism:

- **Payers** vary in terms of their *Reliability*, which indicates how motivated they are. A licit payer without malicious intent usually does not hide himself or disguise its intentions during transactions. Specifically, a reliable payer has harmless intentions regardless of whether it is transferring money to an exchange or to a scammer account (being gypped). In contrast, a perpetrator (e.g., a scammer) hopes to cover up its traces \[[3](#oebps-html-619883_1_en_7_chapter-xhtml-cr3)]. The reliability metric \$\$R(u)\$$ of a payer *u* lies in \$\$\[0,1]\$$, \$\$\\forall u\\in U\$$. A value of 1 denotes a 100% reliable payer and 0 denotes a 0% reliable payer.
- **Payees** vary in their trustworthiness level, measured by a metric called *Trustiness*, which indicates how trustworthy they are. Intuitively, a cryptocurrency service provider with a better reputation will receive more licit transactions (with higher scores) from well-motivated payers. Trustiness of a payee \$\$T(v)\$$ ranges from 0 (very untrustworthy) to 1 (very trustworthy) \$\$\\forall v\\in V\$$.
- **De-anonymous scores** vary in terms of *Confidence*, which reflects the confidence in the estimated risk probability of a transaction. The confidence metric \$\$Conf(u,v)\$$ ranges from 0 (lack of confidence) to 1 (very confident).

*The connection between the reliability and risk of accounts:* We define *Reliability* to characterize the risk rating of accounts because an account’s intention can be inferred by its (active) sending behavior, rather than by its (passive) receiving behavior. A scammer transferring stolen money to its gang is a better reflection of its evil intention than the receipt of stolen money from victims. In the later section, we calculate the *risk* rating of accounts based on the *Reliability* of payer roles.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec9"></a>

### 7.4.2 Network Propagation Mechanism

Given a cryptocurrency payer-payee graph, all intrinsic metrics are unknown but are interdependent. Here, we introduce five items of prior knowledge that establish the relationships and how the network propagation mechanism is specially designed for our problem. The first two items of prior knowledge reflect the interdependency between a payee and the de-anonymous scores that they receive.

**\[Prior Knowledge 1]**

Payees with higher trustiness receive transactions with higher de-anonymous scores. Intuitively, a payee receiving transactions with high de-anonymous scores is more likely to be trustworthy. Formally, if two payees \$\$v_1\$$ and \$\$v_2\$$ have a one-to-one mapping, \$\$h:In(v_1)\\rightarrow In(v_2)\$$ and \$\$Score(u,v_1) &amp;gt; Score(h(u), v_2)\$$ \$\$\\forall (u,v_1)\\in In(v_1)\$$, then \$\$T(v_1)&amp;gt;T(v_2)\$$.

**\[Prior Knowledge 2]**

Payees with higher trustiness receive transactions with more positive confident scores. For two payees \$\$v_1\$$ and \$\$v_2\$$ with identical de-anonymous score networks, if the confidence of the in-transactions of payee \$\$v_1\$$ is higher than that of payee \$\$v_2\$$, the trustiness of payee \$\$v_1\$$ should be higher. Formally, if two payees \$\$v_1\$$ and \$\$v_2\$$ have a one-to-one mapping, \$\$h:In(v_1)\\rightarrow In(v_2)\$$ and \$\$Conf(u,v_1) &amp;gt; Conf(h(u), v_2)\$$ \$\$\\forall (u,v_1)\\in In(v_1)\$$, then \$\$T(v_1)&amp;gt;T(v_2)\$$.

According to the above prior knowledge, we develop the *Trustiness* formulation for \$\$\\forall v \\in V\$$ of our *RiskProp* algorithm: <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ2"></a>

\$$\\displaystyle \\begin{aligned} T(v) = \\frac{\\sum_{(u,v)\\in In(v)} Score(u,v)\\times Conf(u,v)}{|In(v)|}. {} \\end{aligned} $$

(7.2)

The next item of prior knowledge defines the relationship between the score of a transaction and the connected payer–payee pair using the anonymous nature of cryptocurrency.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-fpar2"></a>

**Algorithm 1** ***RiskProp*** **algorithm**

**\[Prior Knowledge 3]**

Confident de-anonymous scores of transactions are closely linked with the connected payee’s trustiness. Formally, if two scores \$\$(u_1, v_1)\$$ and \$\$(u_2, v_2)\$$ are such that \$\$Score(u_1, v_1)=Score(u_2, v_2)\$$, \$\$R(u_1)=R(u_2)\$$, and \$\$|Score(u_1,v_1)\$$ \$$- T(v_1)|\\leqslant $$ \$\$|Score(u_2,v_2)\$$ \$\$-T(v_2)|\$$, then \$\$Conf(u_1, v_1)\\geqslant Conf(u_2, v_2)\$$.

We imply that different transactions sent by the same payers can have different intentions and anonymity. Even scammers on Ethereum can have transactions that seem normal.

**\[Prior Knowledge 4]**

Transactions with higher confidence de-anonymous scores are sent by more reliable payers. Formally, if two scores \$\$(u_1, v_1)\$$ and \$\$(u_2, v_2)\$$ are such that \$\$Score(u_1, v_1)=Score(u_2, v_2)\$$, \$\$T(v_1)=T(v_2)\$$, and \$\$R(u_1)\\geqslant R(u_2)\$$, then \$\$Conf(u_1, v_1)\\geqslant Conf(u_2, v_2)\$$.

This prior knowledge incorporates the payer’s intention in measuring the confidence of transaction scores. In this way, payees may have different confidence in receiving transactions with the same anonymity. For instance, exchanges on Ethereum receive funds from payers with different motivations—some are ordinary investors and some are suspicious accounts.

Below, we propose the *Confidence* formulation that satisfies the above items of prior knowledge: <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ3"></a>

\$$\\displaystyle \\begin{aligned} Conf(u, v) = \\frac{R(u) + (1-|Score(u,v)-T(v)|)}{2}. {} \\end{aligned} $$

(7.3)

Then, we describe how to quantify the *Reliability* metric of a payer by the transactions it sends.

**\[Prior Knowledge 5]**

Payers with higher reliability send transactions with higher confidence. For two payers \$\$u_1\$$ and \$\$u_2\$$ with equal scores, if payer \$\$u_1\$$ has higher confidence for all out transaction scores than \$\$u_2\$$, then payer \$\$u_1\$$ has a higher reliability. Formally, if two payers \$\$u_1\$$ and \$\$u_2\$$ have \$\$h:Out(u_1)\\rightarrow Out(u_2)\$$ and \$\$Conf(u_1,v_1) &amp;gt; Conf(u_2, h(v))\$$ \$\$\\forall (u_1,v)\\in Out(u_1)\$$, then \$\$R(u_1)&amp;gt;R(u_2)\$$. The corresponding formulation of *Reliability* metric for \$\$\\forall u \\in U\$$ is defined as <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ4"></a>

\$$\\displaystyle \\begin{aligned} R(u) = \\frac{\\sum_{(u,v)\\in Out(u)} Conf(u,v)}{|Out(u)|}. {} \\end{aligned} $$

(7.4)

Finally, the risk rating of an account is calculated by \$\$Risk(u) = (1-R(u))\\times 10\$$. The pseudo-code of *RiskProp* network propagation is described in Algorithm [1](#oebps-html-619883_1_en_7_chapter-xhtml-fpar2). Let \$\$T^{0}\$$, \$\$Conf^{0}\$$, \$\$R^{0}\$$ be initial values and *t* be the number of interactions. In the beginning, we have initial reliability \$\$R^{0}\$$ \$\$\\forall u \\in U\$$, initial trustiness \$\$T^{0}=0.5\$$ \$\$\\forall v \\in V\$$, and initial confidence \$\$Conf^{0}=0.5\$$ for all transactions. Then, we keep updating metrics using Eqs. [7.2](#oebps-html-619883_1_en_7_chapter-xhtml-equ2)–[7.3](#oebps-html-619883_1_en_7_chapter-xhtml-equ3) until \$$\\Delta $$ is less than 0.01.

**RiskProp+**

A Semi-supervised Version

Sometimes, we have partial information about the labels of fraudulent accounts (verified, phishing scams, etc.) and licit accounts. We can take advantage of such prior information and incorporate it into our approach in a semi-supervised manner. In the semi-supervised *RiskProp+*, we initialize the *Reliability* metrics only for the training accounts. According to the risk levels of services reported by *Chainalysis* \[[25](#oebps-html-619883_1_en_7_chapter-xhtml-cr25)], we set \$\$R^0=0.9\$$ for *ICO wallet*, *Converter*, and *Mining*, \$\$R^0=0.7\$$ for *Exchange*, \$\$R^0=0.4\$$ for *Gambling*, \$\$R^0=0\$$ for *Phish/Hack*, and set \$\$R^{0}=0.7\$$ for testing accounts. The reliability values of labeled illicit accounts are unchanged during the training procedure.

**Example**

Here, we use a small real-world dataset on Ethereum to intuitively show the results of *RiskProp+* after interactions. We collect transactions of 10 accounts (6 for training and 4 for testing), including 28,598 accounts and 52,733 transactions in total. Table [7.1](#oebps-html-619883_1_en_7_chapter-xhtml-tab1) shows how the reliability of the 4 testing accounts varies over interactions (we omit trustiness and confidence for brevity). These testing accounts have the same reliability values at the beginning (\$\$R^{0}=0.7\$$). After convergence, accounts labeled as “phish/hack” get a lower value of reliability, and other licit accounts get higher reliability. Confirming our intuition, *RiskProp* learns that accounts 0xebdc and 0xfe34 are high-risk accounts that investors need to be aware of. <a id="oebps-html-619883_1_en_7_chapter-xhtml-tab1"></a>

***Table 7.1***

An example of propagation. \$\$R^{0}\$$ is initial value, \$\$R^{final}\$$ and Risk\$\${ }^{final}\$$ are the results after convergence

| Account | Label | \$\$R^{0}\$$ | \$\$R^{final}\$$ | Risk\$\${ }^{final}\$$ |
| --- | --- | --- | --- | --- |
| [0xa768](https://cn.etherscan.com/address/0xa768cc13d1ab64283882ffa74255bb0564a7592b) | Contract-deployer | 0.7 | 0.8575 | 1.425 |
| [0x8271](https://cn.etherscan.com/address/0x8271b2e8cbe29396e9563229030c89679b9470db) | Exchange | 0.7 | 0.9526 | 0.474 |
| [0xebdc](https://cn.etherscan.com/address/0xebdc8d0445e111aad61006f13e7a2d071a473779) | Phish-hack | 0.7 | 0.1195 | 8.805 |
| [0xfe34](https://cn.etherscan.com/address/0xfe34aa1b07c3c61305df1be55719f0be44a23cd9) | Phish-hack | 0.7 | 0.2330 | 7.670 |

**Workflow for Account Risk Rating**

Figure [7.4](#oebps-html-619883_1_en_7_chapter-xhtml-fig4) shows the workflow of account risk rating on Ethereum, which contains four modules: **(i) Data acquisition** collects accounts, transactions, and labels from Ethereum and [Etherscan](https://etherscan.io/). Only a few labels are provided, and these labels are not available in the unsupervised setting. **(ii) Data pre-processing** of raw transaction data described in Fig. [7.1](#oebps-html-619883_1_en_7_chapter-xhtml-fig1) is conducted in two steps: de-anonymous score calculation and directed bipartite graph construction (i.e., payer–payee network). **(iii) Account risk rating** recursively calculates the *Reliability*, *Trustiness* of accounts, and *Confidence* of transaction scores until convergence, updated by the propagation mechanism. **(iv) Results analysis** contains risk rating results analysis, comparative evaluation, and further analysis.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig4"></a>

***Fig. 7.4***

The workflow of account risk rating on Ethereum

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec10"></a>

## 7.5 Experiments of Account Risk Rating

To investigate the effectiveness of *RiskProp*, we conduct experiments on a real-world Ethereum transaction dataset. As risk rating is an issue without any ground truth, we verify the effectiveness and significance of the risk rating results of *RiskProp* via three tasks: (1) **risk rating analysis**, which includes distribution of risk rating results and case studies of transaction pattern; (2) **comparative evaluation**, which reports on the classification performance of labeled accounts compared with various baselines; and (3) **further analysis**, which contains ablation study, impact of risk threshold, and guarantees for practical use.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec11"></a>

### 7.5.1 Account Risk Rating Data Collection

We first obtain 803 ground truth account labels from an official Ethereum explorer and then include all the accounts and transactions that are within the one-hop and two-hop neighborhood of each labeled account. Next, we filter out the zero-ETH transactions and construct the records into a graph, retaining the largest weakly connected component for experiments. As a result, there are 1.19 million accounts and 4.13 million transactions in the network. In the dataset, **0.02%** (243) are labeled illicit (e.g., phishing scam), whereas **0.05%** (560) are labeled licit (e.g., exchanges). The remaining unknown accounts are not labeled with regard to licit versus illicit.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec12"></a>

### 7.5.2 Effectiveness of De-anonymous Score

We use one-way analysis of variance (ANOVA) to assess whether there is a significant difference between illicit and licit transactions in the proposed de-anonymous score in Eq. ([7.1](#oebps-html-619883_1_en_7_chapter-xhtml-equ1)). We consider a transaction as *illicit* (versus *licit*) if its payer is marked as *illicit* (versus *licit*). Table [7.2](#oebps-html-619883_1_en_7_chapter-xhtml-tab2) shows that compared with the random score, our proposed score achieves a larger mean square (MS) between groups and smaller MS within groups; in addition, our proposed score has a higher F value, and the *p*-value equals 0. These results suggest that the de-anonymous score is a useful metric for assessing the quality of transactions. <a id="oebps-html-619883_1_en_7_chapter-xhtml-tab2"></a>

***Table 7.2***

ANOVA of random scores and de-anonymous scores

|  | Random scores |  |  | De-anonymous score |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Src of var. | MS | F | *p*-Value | MS | F | *p*-Value |
| Between groups | \$\$8.8 \\times 10^{-1}\$$ | \$\$2.6 \\times 10^1\$$ | \$\$1.0 \\times 10^{-1}\$$ | \$\$7.8 \\times 10^2\$$ | \$\$7.7 \\times 10^3\$$ | 0 |
| Within groups | \$\$3.3 \\times 10^{-1}\$$ | – | – | \$\$1.0\\times 10^{-1}\$$ | – | – |

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec13"></a>

### 7.5.3 Analysis of Risk Rating Results

The principal task of *RiskProp* is to rate Ethereum accounts based on how ill-disposed they are. Given the account risk rating obtained by *RiskProp*, we first review the results and investigate the capability of *RiskProp* in discovering new risky accounts. Then, we dig deeper into the predicted high-risk accounts and obtain some insights.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec14"></a>

#### 7.5.3.1 Distribution of Risk Rating Results

The risk value of an account ranges from 0 (low risk) to 10 (high risk). The distribution of the predicted risk scores is as follows: 33.58% are located at (0,2], 63.45% are located at (2,4], 2.03% are located at (4,6], 0.78% are located at (6, 8], and 0.19% are located at (8, 10]. This is consistent with expectations: The risk value of the Ethereum transaction network meets the power distribution law, indicating that the overwhelming majority of accounts act normally, and only very few accounts have abnormal behaviors. We are interested in whether the high-risk accounts predicted by *RiskProp* are actually questionable. Thus, we first manually check the top 150 accounts with the highest risk (with both in-coming and out-going transactions). The finding is that 119 out of 150 (approximately **80%**) accounts have abnormal behaviors. Among these 119 illicit accounts, 43 accounts are already labeled as “phish/hack” by Etherscan, whereas the remaining 76 are **newly discovered** suspicious accounts that are not marked in the existing label library. This result indicates the capabilities of *RiskProp* in predicting undiscovered risky accounts and reducing financial losses.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec15"></a>

#### 7.5.3.2 Case Studies of Transaction Pattern

We then manually verified the predicted risky accounts by investigating their abnormal behaviors and found that there are many suspicious transaction patterns in the network. In order to save space, we show 6 typical patterns in Fig. [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5). These patterns are summarized from the real-world Ethereum transaction data and guided by current research and recommendation reports.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig5"></a>

***Fig. 7.5***

Visualization showing some typical transaction patterns of risky accounts (in red circles)

**(a) Hacking Scammers**

are a list of addresses related to phishing and hacks. Figure [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5)a shows a pattern of phishing accounts reported by users who suffered financial loss. A typical phishing scam on Ethereum is the [“Bee Token ICO Scam” attack](https://theripplecryptocurrency.com/bee-token-scam/), in which the phishers sent fake emails to the investors of an ICO with a fake Ethereum address to deposit their contributions into. For example, account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28) has been confirmed to be part of this “Bee Token” scam, and 243 ETH has been sent to this address by 165 victims.

**(b) Fund Source of Hacking Scammers**

are the upstream accounts of the known illicit accounts, which are collusion scam accounts to attract victims or provide money for hacking. As shown in Fig. [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5)b, the behaviors of collusion scam accounts may look similar to victims. Nevertheless, we find that the upstream collusion accounts appear to participate in fewer transactions with shorter time intervals, and there are attempts to transfer the entire ETH balance of the scammers according to the *Red Flag Indicators* of FATF \[[2](#oebps-html-619883_1_en_7_chapter-xhtml-cr2)].

**(c) Money Laundering of Scammers**

are the downstream accounts of the known illicit accounts, which are collusion scam accounts to accept and transfer the stolen money, obfuscating the true sources. As shown in Fig. [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5)c, account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28) received stolen funds from several known hacking scammers, appearing to be the account used in the “placement” stage of money laundering. Another example is [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28), which receives stolen funds from the Fake Starbase Crowdsale Contribution account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28).

**(d) Zero-Out Middle Accounts**

are the middle accounts that serve as a bridge defined by Li et al. \[[11](#oebps-html-619883_1_en_7_chapter-xhtml-cr11)]. As shown in Fig. [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5)d, most of the received funds will be transferred out in short succession (such as within 24 hours). See [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28) for an example.

**(e) Round Transfers Among Exchanges**

denote a pattern that an account withdraws ETH without additional activity to a private wallet and then deposits back to the exchange, as shown in Fig. [7.5](#oebps-html-619883_1_en_7_chapter-xhtml-fig5)e. Account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28) withdraws 0.4 ETH from Cryptopia exchange and then deposits the same amount of ETH back to Cryptopia, which is an unnecessary step and incurs transaction fees \[[2](#oebps-html-619883_1_en_7_chapter-xhtml-cr2)]. Such a phenomenon indicates that the exchange is misused as a money-laundering mixer or is conducting wash trading \[[26](#oebps-html-619883_1_en_7_chapter-xhtml-cr26)].

**(f) Creators of Illicit Contracts**

are often the manipulators behind the scenes. The Origin Protocol phishing scam contact account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28) was created by account [0xe336](https://cn.etherscan.com/address/0xe336327426b8f95a5f5eb1f74144fd9065069c28). After victims deposit money into the phishing contract, the creator transfers the stolen funds back to himself via internal transactions, which deliberately enhances anonymity.

We observe that many illicit accounts are outside the label library and are still considered risk-free. Based on the results, we infer that our *RiskProp* is able to expose unlabeled illicit accounts. This is crucial for Ethereum, which lacks authorized and effective regulation. In addition, the newly identified illicit accounts can complete the current label collection for additional analysis.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec16"></a>

### 7.5.4 Comparative Evaluation Settings

To further evaluate the performance of our method and show the potential application, we employ the rating scores to conduct classification experiments that divide Ethereum accounts into illicit and licit accounts, and we compare the results with the existing baseline methods for further verification. We wish to investigate if *RiskProp* can give a higher risk rating for the known illicit accounts and a lower rating for known licit accounts.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec17"></a>

#### 7.5.4.1 Compared Methods

As mentioned earlier, *RiskProp* is the first algorithm that explores the risk rating of blockchain accounts. We chose a variety of methods (unsupervised and supervised) as baselines, which are similar to the problem we want to solve. We compare unsupervised *RiskProp* with (i) **web page ranking**, such as PageRank \[[27](#oebps-html-619883_1_en_7_chapter-xhtml-cr27)], and (ii) **bipartite graph-based fraud detection,** such as FraudEagle \[[28](#oebps-html-619883_1_en_7_chapter-xhtml-cr28)], BIRDNEST \[[19](#oebps-html-619883_1_en_7_chapter-xhtml-cr19)], and REV2 \[[21](#oebps-html-619883_1_en_7_chapter-xhtml-cr21)], which are also unsupervised methods.

The (semi-)supervised approaches are as follows. **(i) Machine learning methods**, e.g., logistic regression (LR), naïve Bayes (NB), decision tree (DT), support vector machine (SVM), random forest (RF), extreme gradient boosting (XGBoost), and LightGBM. These methods are used by \[[6](#oebps-html-619883_1_en_7_chapter-xhtml-cr6), [10](#oebps-html-619883_1_en_7_chapter-xhtml-cr10), [29](#oebps-html-619883_1_en_7_chapter-xhtml-cr29), [30](#oebps-html-619883_1_en_7_chapter-xhtml-cr30)] for the detection of abnormal Ethereum accounts. **(ii) Traditional graph neural network**, including DeepWalk, Node2Vec, and graph convolutional network (GCN) were conducted by Chen et al. \[[31](#oebps-html-619883_1_en_7_chapter-xhtml-cr31)] for detection of Ethereum phishing scams. **(iii) Graph neural network for graphs with heterophily**, such as CPGNN \[[32](#oebps-html-619883_1_en_7_chapter-xhtml-cr32)]. The application of this type of algorithm is a recent research advancement in the task of Ethereum account classification \[[33](#oebps-html-619883_1_en_7_chapter-xhtml-cr33)].

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec18"></a>

#### 7.5.4.2 Evaluation Metrics

To evaluate the performance of the models, we calculate the following metrics: *Precision*, *Recall*, *F*1, *Accuracy*, and *AUC*. As we know, there are only 6 out of 10,000 (0.067%) accounts labeled in the entire dataset. To measure the order of the risk rating, we employ \$\$Precision@k\$$ and \$\$Recall@k\$$ to evaluate the ranking order of the algorithm (\$\$@k\$$ means the top *k* accounts). All baseline methods are tested using the original codes published by the authors. We repeat experiments 10 times and report the average results.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec19"></a>

#### 7.5.4.3 Implementation Details

We evaluate the methods with binary labeled accounts (*illicit* verse *licit*) and, thus, we assume accounts in the top 1% to be the illicit accounts (corresponding threshold: 6 for *RiskProp*). The reason for this threshold and percentage setting is discussed in Sect. [7.5.7](#oebps-html-619883_1_en_7_chapter-xhtml-sec22). The split of the dataset in the (semi-)supervised setting is \$\$training{:}test = 8{:}2\$$.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec20"></a>

### 7.5.5 Comparative Evaluation Results

We report the \$\$Precision@k\$$ and \$\$Recall@k\$$ curves of the compared algorithms, as shown in Fig. [7.6](#oebps-html-619883_1_en_7_chapter-xhtml-fig6). We observe that *RiskProp* obtains superior precision and recall than that of baseline with different *k*. Up to \$\$k=100\$$, the precision of RiskProp is almost 1 for illicit account prediction, which is surprising for an unsupervised setting. The \$\$Recall@k\$$ curve of RiskProp is significantly higher than the compared methods, and also increases steadily with *k*. Table [7.3](#oebps-html-619883_1_en_7_chapter-xhtml-tab3) shows the performance of unsupervised and supervised methods separately. We observe that *RiskProp* remarkably outperforms the unsupervised graph rating baselines in terms of accuracy and AUC, improving by 38.90% and 34.16%, respectively. Meanwhile, for the licit account prediction, we observe that RiskProp beats the best baseline (FraudEagle) with a 10.48% improvement in its F1-score. These demonstrate the effectiveness of our account risk rating method without labeling information.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig6"></a>

***Fig. 7.6***

The \$\$Precision@k\$$ and \$\$Recall@k\$$ of illicit account prediction with different rating methods. (**a**) and (**b**) Top K

<a id="oebps-html-619883_1_en_7_chapter-xhtml-tab3"></a>

***Table 7.3***

The classification results (%) of unsupervised and (semi-)supervised methods

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Illicit account |  |  | Licit account |  |  | Total |  |
| Methods | Precision | Recall | F1-score | Precision | Recall | F1 | Accuracy | AUC |
| PageRank | 29.13 | 67.49 | 40.69 | 67.08 | 28.75 | 40.25 | 40.47 | 48.12 |
| FraudEagle | 12.28 | 2.88 | 4.670 | 68.36 | **91.07** | 78.10 | 64.38 | 46.98 |
| BIRDNEST | 22.24 | 47.32 | 30.26 | 55.24 | 28.21 | 37.35 | 34.00 | 37.77 |
| REV2 | 14.10 | 4.527 | 6.854 | 68.00 | 88.04 | 76.73 | 62.76 | 46.28 |
| RiskProp | **71.48** | **71.48** | **76.15** | **91.44** | 85.89 | **88.58** | **84.56** | **83.69** |
|  | Illicit account |  |  | Licit account |  |  | Total |  |
| Methods | Precision | Recall | F1-score | Precision | Recall | F1 | Accuracy | AUC |
| LR | 65.67 | 74.58 | 69.84 | 83.87 | 77.23 | 80.41 | 76.25 | 75.90 |
| NB | 59.79 | **98.31** | 74.36 | **98.41** | 61.39 | 75.61 | 75.00 | 79.85 |
| DT | 62.66 | 54.07 | 58.04 | 75.79 | 81.19 | 78.40 | 71.75 | 68.39 |
| SVM | **90.00** | 45.76 | 60.67 | 75.38 | **97.03** | 84.85 | 78.12 | 71.40 |
| RF | 71.52 | 53.39 | 61.14 | 75.55 | 86.93 | 80.84 | 74.00 | 69.40 |
| XGBoost | 67.35 | 55.95 | 61.11 | 76.58 | 84.16 | 80.19 | 70.05 | 73.75 |
| LightGBM | 75.77 | 65.19 | 69.93 | 84.23 | 92.57 | 88.21 | 81.86 | 77.75 |
| DeepWalk | 66.85 | 66.30 | 66.54 | 86.48 | 86.75 | 86.61 | 83.13 | 81.03 |
| Node2Vec | 62.36 | 63.26 | 62.76 | 85.10 | 84.56 | 84.82 | 78.13 | 72.78 |
| GCN | 20.83 | 27.78 | 23.81 | 79.46 | 68.99 | 73.86 | 60.63 | 47.40 |
| CPGNN | 52.17 | 61.54 | 56.47 | 86.84 | 81.82 | 84.26 | 76.88 | 71.68 |
| RiskProp+ | 70.91 | 84.78 | **77.23** | 93.33 | 85.96 | **89.49** | **85.63** | **85.37** |

The best results are marked in bold

Next, we turn our attention to the results of the semi-supervised *RiskProp+* compared with the existing (semi-)supervised classification in Table [7.3](#oebps-html-619883_1_en_7_chapter-xhtml-tab3), from which we derive the following conclusions: (1) *RiskProp+* outperforms all baseline methods by 12.32% in terms of F1-score, 13.62% in terms of AUC, and 10.56% in terms of accuracy. (2) The precision of licit accounts prediction is improved from 82.52% (i.e., the average precision in baselines) to 93.33%, which means more licit accounts can be correctly identified. (3) The superior performance of *RiskProp* is more significant in the prediction of illicit accounts. The recall of illicit accounts prediction is improved from 60.56% (i.e., the average recall of illicit accounts prediction in baselines) to 84.78%. This shows the effectiveness of our framework in the prediction of both illicit and licit accounts.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec21"></a>

### 7.5.6 Ablation Study

To further validate the contribution of each component of the proposed *RiskProp+*, we conduct an ablation study as follows.

- **RiskProp+ (Full model):** All components of the model and label data are included.
- **w/o label:** Labels are unavailable in the learning procedure, and the model is trained in an unsupervised manner.
- **w/o network propagation (NP):** Remove the NP procedure and calculate the average de-anonymous scores (*ADS*) for each account’s outgoing transactions (payer role). An account is predicted as abnormal if its \$\$ADS\\leqslant 0\$$.
- **w/o de-anonymous score (DS):** Replace DS with random scores, ranging from \$\$-\$$1 to 1.

We derive the following findings from Table [7.4](#oebps-html-619883_1_en_7_chapter-xhtml-tab4): (1) Without the labels, the F1-score drops only slightly, indicating that our *RiskProp* does not rely on label data and can obtain good results in an unsupervised manner. To our surprise, the full model outperforms the RiskProp (w/o label), with a 3.3% increase in recall and 0.51% decrease in precision. This may be possibly explained by the reliability values of labeled illicit accounts remaining unchanged during training in the supervised setting. (2) RiskProp (w/o NP) has a only lower precision but a greatly improved recall, revealing that most of the illicit accounts are correctly predicted as illicit but that some licit accounts are misjudged to be illicit. This result demonstrates that de-anonymous score is an effective indicator of illicit transactions but their confidence varies among transactions. This result also confirms why we need to consider the confidence of the score in the propagation mechanism. (3) RiskProp (w/o DS) yields low precision (47.37%) and severely low recall (19.57%). This result demonstrates that, even if the network propagation model is retained, the wrong scores of transactions will be spread throughout the entire Ethereum transaction network, resulting in poor prediction results. <a id="oebps-html-619883_1_en_7_chapter-xhtml-tab4"></a>

***Table 7.4***

Illicit account prediction of ablation studies

| Methods | Precision | Recall | F1-score |
| --- | --- | --- | --- |
| RiskProp+ | 0.7091 | 0.8478 | **0.7723** |
| RiskProp+ (w/o label) | **0.7148** | 0.8148 | 0.7615 |
| RiskProp+ (w/o NP) | 0.3811 | **0.9959** | 0.5513 |
| RiskProp+ (w/o DS) | 0.4737 | 0.1957 | 0.2769 |

The best results are marked in bold

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec22"></a>

### 7.5.7 Risk Threshold Analysis

Given accounts in the reversed order of their risk ratings, a natural question is *how to classify licit or illicit accounts according to their risk ratings for the classification task?* One possible option is to determine the percentage of known illicit labels in the dataset and set the risk value of this percentage as a demarcation line for account classification. However, the percentage is imprecise because some of the illicit accounts remain unrevealed according to the experimental results in Sect. [7.5.3.2](#oebps-html-619883_1_en_7_chapter-xhtml-sec15). Therefore, we try to establish a suitable risk threshold (*RTH*) of RiskProp by conducting classification experiments. Figure [7.7](#oebps-html-619883_1_en_7_chapter-xhtml-fig7)a demonstrates the results of illicit account prediction with different risk thresholds, ranging from 1 to 10. As expected, the precision increases while the recall decreases with increasing *RTH*. In addition, F1, accuracy, and AUC first increase and then decrease with the increase in *RTH*. The best performance for F1 and AUC is when \$\$RTH=6\$$. Thus, we set the risk threshold \$\$RTH=6\$$ for *RiskProp*.<a id="oebps-html-619883_1_en_7_chapter-xhtml-fig7"></a>

***Fig. 7.7***

Further analysis of *RiskProp*. (**a**) Impact of different *RTH*. (**b**) Scalability of *RiskProp*

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec23"></a>

### 7.5.8 Guarantees for Practical Use

Here, we present guarantees for *RiskProp* in practical use regarding the following aspects: (1) guarantee of convergence; (2) time complexity; and (3) linear scalability.

**Convergence and Uniqueness**

We present the theoretical properties of *RiskProp*, including the proofs of prior knowledge, convergence, and uniqueness of the proposed metrics, i.e., *reliability*, *trustiness*, and *confidence*. Proofs are shown in the Appendix due to lack of space.

**Time Complexity**

In each interaction, the *RiskProp* updates the *reliability*, *Trustiness* metrics of accounts and *Confidence* metric of transactions. Therefore, the complexity of each iteration is \$\$\\mathcal {O}(|U|+|S|)=\\mathcal {O}(|S|)\$$, \$\$|S|\$$ is the total edges in the payer–payee network. Thus, for *k* iterations, the total running time is \$\$\\mathcal {O}(k|S|)\$$.

**Linear Scalability**

We have shown that *RiskProp* is linear in running time in the number of nodes. To show this experimentally as well, we create random networks of an increasing number of nodes and edges and compute the running time of the algorithm until convergence. Figure [7.7](#oebps-html-619883_1_en_7_chapter-xhtml-fig7)b shows that the running time increases linearly with the number of nodes in the network. Therefore, we can conclude that *RiskProp* is a scalable rating method that is suitable for applications on large-scale transaction networks.

**Analysis of Incorrect Predictions**

Furthermore, the results of the *RiskProp+* experiment showed that 39 out of 46 (85%) phishing accounts were correctly predicted as illicit accounts. To understand why the remaining accounts failed to be detected as illicit by our model, we manually checked their transactions and neighbors and obtained the following results: (i) For one of the accounts, we have a risk score of 5.72, and in practice, the system will also warn about such accounts that are close to the risk threshold (\$\$RTH=6\$$). (ii) One account is set as the default risk value because the phishing account has no outgoing transactions for the time being, and in practice, we can make correct predictions as soon as the phishing account starts laundering money. (iii) Among the remaining five accounts, one account has a high transaction volume of 154. The remaining four accounts have a high volume of transactions along with withdrawals of ETH from exchanges, which directly contributed to the high de-anonymity score of transactions. However, there are two sides to the story: regulation and fraud are a game of confrontation. For hackers, reusing accounts reduces the probability of being identified as high risk, and at the same time, reusing accounts and withdrawing money from exchanges increase the risk of exposure and fund freezing.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec24"></a>

## 7.6 Conclusion

In this chapter, we present the first systematic study to assess the account risk via a rating system named *RiskProp*. In *RiskProp*, we modeled transaction records of Ethereum as a bipartite graph, proposed a novel metric called de-anonymous score to quantify the transaction risk, and designed a network propagation mechanism based on transaction semantics. By analyzing the rating results and manually checking the accounts with high risk, we evaluated the performance of *RiskProp* and obtained new insights about transaction risks on Ethereum. In addition, we employed the obtained risk scores to conduct illicit/licit account classification experiments on labeled data, and the superiority of this method over baseline methods further verified the effectiveness of *RiskProp* in risk estimation.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-sec25"></a>

## Appendix

### Proof for Prior Knowledge

In this part, we provide proof that the proposed metrics, i.e., *Reliability*, *Trustiness*, and *Confidence* satisfy Prior knowledge 1–5. Prior knowledge 1 in the main chapter is the following:

**\[Prior Knowledge 1]**

Payees with higher trustiness receive transactions with higher de-anonymous scores. Formally, if two payees \$\$v_1\$$ and \$\$v_2\$$ have a one-to-one mapping, \$\$h:In(v_1)\\rightarrow In(v_2)\$$ and \$\$Score(u,v_1) &amp;gt; Score(h(u), v_2)\$$ \$\$\\forall (u,v_1)\\in In(v_1)\$$, then \$\$T(v_1)&amp;gt;T(v_2)\$$.

The formulation to be used to show that the prior knowledge is satisfied is Eqs. ([7.2](#oebps-html-619883_1_en_7_chapter-xhtml-equ2)), ([7.3](#oebps-html-619883_1_en_7_chapter-xhtml-equ3)), and ([7.4](#oebps-html-619883_1_en_7_chapter-xhtml-equ4)) in the main chapter.

\$\$\\displaystyle \\begin{aligned} T(v) = \\frac{\\sum_{(u,v)\\in In(v)} Score(u,v)\\times Conf(u,v)}{|In(v)|}  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} R(u) = \\frac{\\sum_{(u,v)\\in Out(u)} Conf(u,v)}{|Out(u)|}  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} Conf(u, v) = \\frac{R(u) + (1-|Score(u,v)-T(v)|)}{2}  \\end{aligned}\$$

**Proof**

To prove the Prior Knowledge 1, let us take two payees \$\$v_1\$$ and \$\$v_2\$$ that have identically ego networks and a one-to-one mapping *h*, such that \$\$|In(v_1)|=|In(v_2)|\$$, \$\$Conf(u, v_1)=Conf(h(u), v_2)\$$, and \$\$Score(u,v_1) &amp;gt; Score(h(u), v_2)\$$ \$\$\\forall (u,v_1)\\in In(v_1)\$$.

According to Eq. ([7.2](#oebps-html-619883_1_en_7_chapter-xhtml-equ2)), we have

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} T(v_1)-T(v_2)&amp;amp;= \\frac{\\sum\_{(u,v_1)\\in In(v_1)} Score(u,v_1)\\times Conf(u,v_1)}{|In(v_1)|}-\\\\ &amp;amp;\\frac{\\sum\_{(u,v_2)\\in In(v_2)} Score(h(u),v_2)\\times Conf(h(u),v_2)}{|In(v_2)|}\\\\ &amp;amp;=\\frac{\\sum_{(u,v_1)\\in In(v_1)}(Score(u,v_1)-Score(h(u),v_2))\\times Conf(u,v_1)}{|In(v_1)|} \\end{aligned}  \\end{aligned}\$$

As \$\$Score(u,v_1) &amp;gt; Score(h(u), v_2)\$$, so

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} T(v_1)-T(v_2) &amp;gt; \\frac{\\sum_{(u,v_1)\\in In(v_1)}Conf(u,v_1)}{|In(v_1)|} \\end{aligned}  \\end{aligned}\$$

As \$\$Conf(u,v_1)\$$ \$$\\ge $$ 0 because *Confidence* are non-negative,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} T(v_1)-T(v_2) &amp;gt; 0 \\Rightarrow T(v_1) &amp;gt; T(v_2) \\end{aligned}  \\end{aligned}\$$

The other items of prior knowledge have very similar and straightforward proof. □

### Proof for Convergence

Before the proof of convergence, we first discuss the boundary of proposed metrics. At the end of iteration *t* of Algorithm [1](#oebps-html-619883_1_en_7_chapter-xhtml-fpar2), and by Eqs. ([7.2](#oebps-html-619883_1_en_7_chapter-xhtml-equ2)), ([7.3](#oebps-html-619883_1_en_7_chapter-xhtml-equ3)), and ([7.4](#oebps-html-619883_1_en_7_chapter-xhtml-equ4)), we get,

\$\$\\displaystyle \\begin{aligned} T^t(v)=\\frac{\\sum_{(u,v)\\in In(v)}Score(u,v)\\times Conf^{t-1}(u,v)}{|In(v)|}  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} R^t(u)=\\frac{\\sum_{(u,v)\\in Out(u)}Conf^{t-1}(u,v)}{|Out(u)|}  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} Conf^t(u,v) = \\frac{R^t(u)+(1-|Score(u,v)-T^t(v)|}{2})  \\end{aligned}\$$

\$\$T^{\\infty (v)}, R^{(\\infty )}(u), Conf^{(\\infty )}(u,v)\$$ are their final values after convergence.

<a id="oebps-html-619883_1_en_7_chapter-xhtml-fpar3"></a>

**Lemma 7.1 (Boundary Discussion)**

*Set the maximum score in the transaction network as M, namely:*

\$\$\\displaystyle \\begin{aligned} M = \\operatorname*{\\max}_{(u,v)} Score(u,v)  \\end{aligned}\$$

*then* \$\$|M| &amp;lt; 1\$$.

*The difference between a payee v’s final Trustiness and its Trustiness after the first iteration is*

\$\$\\displaystyle \\begin{aligned} |T^{\\infty}(u)-T^1(u)|\\le |M|  \\end{aligned}\$$

*Similarly,*

\$\$\\displaystyle \\begin{aligned} |R^{\\infty}(u)-R^1(u)|\\le 1  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} |Conf^{\\infty}(u,v)-Conf^1(u,v)|\\le \\frac{1+|M|}{2} = \\alpha~(\\alpha \\le 1)  \\end{aligned}\$$

**Proof**

First, we state that \$\$|M|\$$ is strictly less than 1 in practice. According to the formulation of *Score* of the main chapter, we can see that \$\$Score(u,v) = 1\$$ when \$\$OutTxn(u)=maxOut\$$ and \$\$InTxn(v)=maxIn\$$, it is an extreme situation where the largest number of payments and receptions of the entire network appears in one transaction. The other case is \$\$Score(u,v) = -1\$$ when that \$\$OutTxn(u)=1\$$ and \$\$InTxn(v)=1\$$ at the same time. This situation presents some isolated transactions, however, they do not propagate risk and thus do not influence convergence. These situations are out of our consideration. So we get \$\$|M|\$$ is strictly smaller than 1.

Then, we prove that \$\$T(v)\$$ is bounded during the iterations:

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |T^{\\infty}(v)-T^1(v)| &amp;amp; = | \\frac{\\sum\_{(u,v)\\in In(v)}Score(u,v)\\times Conf^{\\infty}(u,v)}{|In(v)|}-\\\\ &amp;amp;\\frac{\\sum_{(u,v)\\in In(v)}Score(u,v)\\times Conf^{0}(u,v)}{|In(v)|}| \\end{aligned}  \\end{aligned}\$$

Since \$\$|x+y|\\le |x|+|y|\$$, we get,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |T^{\\infty}(v)-T^1(v)| &amp;amp;\\le \\frac{\\sum_{(u,v)\\in In(v)}|Score(u,v)\\times (Conf^{\\infty}(u,v) - Conf^{0}(u,v))|}{|In(v)|} \\end{aligned}  \\end{aligned}\$$

Since \$\$|x\\times y| = |x|\\times |y|\$$, we have, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ5"></a>

\$$\\displaystyle \\begin{aligned} \\begin{aligned} |T^{\\infty}(v)-T^1(v)| &amp;amp;\\le \\frac{\\sum_{(u,v)\\in In(v)}|Score(u,v)|\\times (Conf^{\\infty}(u,v) - Conf^{0}(u,v))|}{|In(v)|} \\end{aligned} {} \\end{aligned} $$

(7.5)

Since \$$|Score(u, v)| \\le |M| \\le 1 $$, and \$\$|(Conf^{\\infty }(u,v) - Conf^{0}(u,v))| \\le 1\$$, we get,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |T^{\\infty}(v)-T^1(v)| \\le |M| \\times \\frac{|In(v)|}{|In(v)|} = |M| \\end{aligned}  \\end{aligned}\$$

Next, we conduct the proof on \$\$R(u)\$$:

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |R^{\\infty}(u)-R^1(u)| &amp;amp; = \\frac{|\\sum\_{(u,v)\\in Out(u)} Conf^{\\infty}(u,v) -\\sum_{(u,v)\\in Out(u)}Conf^{0}(u,v)|}{|Out(u)|} \\end{aligned}  \\end{aligned}\$$

Again, since \$\$|x\\times y| = |x|\\times |y|\$$, we get, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ6"></a>

\$$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|R^{\\infty}(u)-R^1(u)| \\le \\frac{\\sum_{(u,v)\\in Out(u)}| Conf^{\\infty}(u,v) - Conf^{0}(u,v)|}{|Out(u)|} \\end{aligned} {} \\end{aligned} $$

(7.6)

Similarly, since \$\$|(Conf^{\\infty }(u,v) - Conf^{0}(u,v))| \\le 1\$$, we have,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |R^{\\infty}(u)-R^1(u)| \\le \\frac{|Out(u)|}{|Out(u)|} = 1 \\end{aligned}  \\end{aligned}\$$

Finally, we calculate the bound of \$$Conf(u,v) $$:

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|Conf^{\\infty}(u,v)-Conf^1(u,v)| =\\\\ &amp;amp;\\frac{|R^{\\infty}(u)-R^1(u)+|Score(u,v)-T^1(v)|-|Score(u,v)-T^{\\infty}(v)||}{2} \\end{aligned}  \\end{aligned}\$$

Since \$\$|x+y|\\le |x|+|y|\$$, we have

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|Conf^{\\infty}(u,v)-Conf^1(u,v)| \\le\\\\ &amp;amp;\\frac{|R^{\\infty}(u)-R^1(u)|+ (||Score(u,v)-T^1(v)|-|Score(u,v)-T^{\\infty}(v)||)}{2} \\end{aligned}  \\end{aligned}\$$

Since \$\$||x|-|y|| \\le |x-y|\$$, it follows that, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ7"></a>

\$$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|Conf^{\\infty}(u,v)-Conf^1(u,v)| \\le \\frac{|R^{\\infty}(u)-R^1(u)|+ |T^{\\infty}(v)-T^1(v)|}{2} \\end{aligned} {} \\end{aligned} $$

(7.7)

Since \$\$|R^{\\infty }(u) - R^{1}(u)| \\le 1\$$, and\$\$|T^{\\infty }(v)-T^1(v)| \\le |M|\$$, we get,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |Conf^{\\infty}(u,v)-Conf^1(u,v)| \\le \\frac{1+|M|}{2} \\end{aligned}  \\end{aligned}\$$

For convenience, we let \$$\\frac {1+|M|}{2}=\\alpha $$. Since \$\$|M|&amp;lt;1\$$, then \$\$\\alpha &amp;lt;1\$$. □

**Theorem 7.1**

*Convergence of Propagation: The difference during iterations is bounded as as* \$\$|Conf^{\\infty }(u,v)-Conf^t(u,v)| \\le \\alpha ^{t}\$$ *(*\$\$\\alpha =\\frac {1+|M|}{2} &amp;lt; 1\$$*),* \$\$\\forall (u, v)\\in S\$$*. As t increases, the difference decreases and* \$\$Conf^t(u,v)\$$ *converges to* \$\$|Conf^{\\infty }(u,v)\$$*. Similarly,* \$\$|T^{\\infty }(v)-T^t(v)| \\le \\alpha ^{t-1},\\forall v \\in V\$$, \$\$|R^{\\infty }(u)-R^t(u)| \\le \\alpha ^{t-1},\\forall u \\in U\$$.

**Proof**

Similar to Eqs. ([7.5](#oebps-html-619883_1_en_7_chapter-xhtml-equ5)), ([7.6](#oebps-html-619883_1_en_7_chapter-xhtml-equ6)), and ([7.7](#oebps-html-619883_1_en_7_chapter-xhtml-equ7)), we have, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ8"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} &amp;amp;|Conf^{\\infty}(u,v)-Conf^t(u,v)| \\le \\frac{|R^{\\infty}(u)-R^t(u)|+ |T^{\\infty}(v)-T^t(v)|}{2} \\end{aligned} \\end{aligned} $$

(7.8)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-equ9"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} &amp;amp;|R^{\\infty}(u)-R^t(u)|\\le \\frac{\\sum_{(u,v,)\\in Out(u)}| Conf^{\\infty}(u,v) - Conf^{t-1}(u,v)|}{|Out(u)|} \\end{aligned} \\end{aligned} $$

(7.9)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-equ10"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} &amp;amp;|T^{\\infty}(v)-T^t(v)| \\\\ &amp;amp;\\le \\frac{\\sum_{(u,v)\\in In(v)}|Score(u,v)|\\times |(Conf^{\\infty}(u,v)- Conf^{t-1}(u,v))|}{|In(v)|} \\end{aligned} \\end{aligned} $$

(7.10)

First, we will prove the convergence of *Confidence* using mathematical induction.

*Base Case of Induction*

When \$\$t=1\$$, as we proved in Lemma [7.1](#oebps-html-619883_1_en_7_chapter-xhtml-fpar3), we get:

\$\$\\displaystyle \\begin{aligned} |Conf^{\\infty}(u,v)-Conf^1(u,v)|\\le \\alpha^{1}  \\end{aligned}\$$

**Induction Step**

We assume by the hypothesis that

\$\$\\displaystyle \\begin{aligned} |Conf^{\\infty}(u,v)-Conf^{t-1}(u,v)|\\le \\alpha^{t-1},  \\end{aligned}\$$

which is consistent with the base case already.

Then, by substituting Eqs. ([7.9](#oebps-html-619883_1_en_7_chapter-xhtml-equ9)) and ([7.10](#oebps-html-619883_1_en_7_chapter-xhtml-equ10)) into Eq. ([7.8](#oebps-html-619883_1_en_7_chapter-xhtml-equ8)), for the case in the next iteration where time is *t*, we have,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|Conf^{\\infty}(u,v)-Conf^t(u,v)| \\\\ &amp;amp;\\le \\frac{\\sum\_{(u,v)\\in Out(u)}| Conf^{\\infty}(u,v) - Conf^{t-1}(u,v)|}{2\\times|Out(u)|})\\\\ &amp;amp;+\\frac{\\sum\_{(u,v)\\in In(v)}|Score(u,v)|\\times |(Conf^{\\infty}(u,v) - Conf^{t-1}(u,v)|}{2\\times|In(v)|}\\\\ &amp;amp;\\le \\frac{1}{2}\\times \\left((\\frac{1+|M|}{2})^{t-1} + \\frac{|M|\\times \\sum_{(u,v)\\in In(v)} |Conf^{\\infty}(u,v) - Conf^{t-1}(u,v)|}{|In(v)|}\\right)\\\\ &amp;amp;\\le \\frac{1}{2}\\times \\left((\\frac{1+|M|}{2})^{t-1} +|M| \\times (\\frac{1+|M|}{2})^{t-1}\\right) \\\\ &amp;amp;\\le (\\frac{1+|M|}{2})^{t} = \\alpha^{t} \\\\ \\end{aligned}  \\end{aligned}\$$

Therefore, \$\$|Conf^{\\infty }(u,v)-Conf^t(u,v)|\\le \\alpha ^{t}\$$.

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} |R^{\\infty}(u)-R^t(u)| &amp;amp; \\le \\frac{\\sum\_{(u,v)\\in Out(u)}| Conf^{\\infty}(u,v) - Conf^{t-1}(u,v)|}{|Out(u)|} \\\\ &amp;amp;\\le \\frac{\\sum_{(u,v)\\in Out(u)} (\\frac{1+|M|}{2})^{t-1}}{|Out(u)|}\\\\ &amp;amp;\\le (\\frac{1+|M|}{2})^{t-1} = \\alpha^{t-1} \\end{aligned}  \\end{aligned}\$$

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;|T^{\\infty}(v)-T(v)^t| \\\\ &amp;amp;\\le \\frac{\\sum\_{(u,v)\\in In(v)}|Score(u,v)|\\times |(Conf^{\\infty}(u,v) - Conf^{t-1}(u,v))|}{|In(v)|} \\\\ &amp;amp;\\le \\frac{\\sum\_{(u,v)\\in In(v)}|(Conf^{\\infty}(u,v) - Conf^{t-1}(u,v))|}{|In(v)|}\\\\ &amp;amp;\\le \\frac{\\sum_{(u,v)\\in In(v)}(\\frac{1+|M|}{2})^{t-1}}{|In(v)|} \\\\ &amp;amp;\\le (\\frac{1+|M|}{2})^{t-1} = \\alpha^{t-1} \\end{aligned}  \\end{aligned}\$$

As discussed in the Lemma [7.1](#oebps-html-619883_1_en_7_chapter-xhtml-fpar3). we know that \$\$|M|\$$ is strictly smaller than 1, then we have \$\$\\alpha &amp;lt;1\$$. As *t* increases, \$\$\\alpha ^{t-1} \\rightarrow 0\$$ and \$\$\\alpha ^{t} \\rightarrow 0\$$, so after *t* iterations, \$\$Conf(u,v)^t\\rightarrow Conf^{\\infty }(u,v)\$$, \$\$R(u)^t\\rightarrow R^{\\infty }(u)\$$, and \$\$T(v)^t\\rightarrow T^{\\infty }(v)\$$, the algorithm converges. □

### Proof for Uniqueness

In this part, we provide proofs that *Reliability*, *Trustiness*, and *Confidence* are unique.

**Theorem 7.2**

*Confidence, Reliability, and Trustiness converge to the unique value.*

**Proof**

First, we consider the uniqueness of *Confidence* using mathematical contradiction.

Let the \$\$Conf(u,v)\$$ converges to different values. So, let \$\$(u,v)\$$ be the transaction with maximum *Confidence* difference, *D* (with \$\$D \\ge 0\$$), between its two possible \$\$Conf_1(u,v)\$$ and \$\$Conf_2(u,v)\$$.

According to Eq. ([7.8](#oebps-html-619883_1_en_7_chapter-xhtml-equ8)), we get, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ11"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} D&amp;amp;=|Conf_1^{\\infty}(u,v)-Conf_2^{\\infty}(u,v)| \\\\ &amp;amp;\\le\\frac{|R_1^{\\infty}(u)-R_2^{\\infty}(u)|+|T_1^{\\infty}(v)-T_2^{\\infty}(v)|}{2} \\end{aligned} \\end{aligned} $$

(7.11)

Then, according to Eqs. ([7.9](#oebps-html-619883_1_en_7_chapter-xhtml-equ9)) and ([7.10](#oebps-html-619883_1_en_7_chapter-xhtml-equ10)), we have, <a id="oebps-html-619883_1_en_7_chapter-xhtml-equ12"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} |R_1^{\\infty}(u)-R_2^{\\infty}(u)| &amp;amp; \\le \\frac{\\sum_{(u,v)\\in Out(u)}| Conf_1^{\\infty}(u,v) - Conf_2^{\\infty}(u,v)|}{|Out(u)|} \\\\ &amp;amp; \\le D \\end{aligned} \\end{aligned} $$

(7.12)

<a id="oebps-html-619883_1_en_7_chapter-xhtml-equ13"></a>

\$$\\displaystyle \\begin{aligned} {} \\begin{aligned} &amp;amp;|T_1^{\\infty}(v)-T_2^{\\infty}(v)| \\\\ &amp;amp;\\qquad \\le \\frac{\\sum_{(u,v)\\in In(v)}|Score(u,v)|\\times |Conf_1^{\\infty}(u,v)- Conf_2^{\\infty}(u,v)|}{|In(v)|} \\\\ &amp;amp;\\qquad  \\le |M|\\times D \\end{aligned} \\end{aligned} $$

(7.13)

We substitute Eqs. ([7.12](#oebps-html-619883_1_en_7_chapter-xhtml-equ12)) and ([7.13](#oebps-html-619883_1_en_7_chapter-xhtml-equ13)) into Eq. ([7.11](#oebps-html-619883_1_en_7_chapter-xhtml-equ11)), and get,

\$\$\\displaystyle \\begin{aligned} \\begin{aligned} &amp;amp;D=|Conf_1^{\\infty}(u,v)-Conf_2^{\\infty}(u,v)| \\\\ &amp;amp;\\le \\frac{1}{2}\\times (\\frac{\\sum\_{(u,v)\\in Out(u)}| Conf_1^{\\infty}(u,v) - Conf_2^{\\infty}(u,v)|}{|Out(u)|} \\\\ &amp;amp;+\\frac{\\sum\_{(u,v)\\in In(v)}|Score(u,v)|\\times |Conf_1^{\\infty}(u,v) - Conf_2^{\\infty}(u,v)|}{|In(v)|} \\\\ &amp;amp;\\le \\frac{1}{2}\\times \\left( D +\\frac{|M|\\times\\sum_{(u,v)\\in In(v)} |Conf^{\\infty}(u,v) - Conf^{\\infty}(u,v)|}{|In(v)|} \\right)\\\\ &amp;amp;\\le \\frac{1}{2}\\times ( D +|M| \\times D ) \\\\ &amp;amp;\\le (\\frac{1+|M|}{2}) \\times D \\\\ &amp;amp; = \\alpha \\times D \\\\ \\end{aligned}  \\end{aligned}\$$

Thus, by solving \$\$D \\le \\alpha \\times D (\\alpha \\ne 0)\$$ and with the condition that \$\$D\\ge 0\$$, we obtain \$\$D=0\$$. Then, \$\$|Conf_1^{\\infty }(u,v)-Conf_2^{\\infty }(u,v)|=0\$$ and converge value of *Confidence* is unique. The uniqueness of *Trustiness* and *Reliability* have similar proof. □

<a id="oebps-html-619883_1_en_7_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr1"></a>Möser, M., Böhme, R., Breuker, D.: Towards risk scoring of bitcoin transactions. In: FC, pp. 16–32. Springer, Berlin (2014)
2. 2\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr2"></a>FATF: Money laundering and terrorist financing red flag indicators associated with virtual assets. [http://www.fatf-gafi.org/publications/fatfrecommendations/documents/Virtual-Assets-Red-Flag-Indicators.html](http://www.fatf-gafi.org/publications/fatfrecommendations/documents/Virtual-Assets-Red-Flag-Indicators.html) (2022)
3. 3\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr3"></a>Victor, F.: Address clustering heuristics for ethereum. In: FC, pp. 617–633. Springer, Berlin (2020)
4. 4\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr4"></a>Farrugia, S., Ellul, J., Azzopardi, G.: Detection of illicit accounts over the Ethereum blockchain. Expert Syst. Appl. **150**, 113318 (2020)[Crossref](https://doi.org/10.1016/j.eswa.2020.113318)
5. 5\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr5"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
6. 6\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr6"></a>Chen, W., Guo, X., Chen, Z., Zheng, Z., Lu, Y.: Phishing scam detection on ethereum: towards financial security for blockchain ecosystem. In: IJCAI, pp. 4506–4512 (Jul. 2020)
7. 7\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr7"></a>Weber, M., Domeniconi, G., Chen, J., Weidele, D.K.I., Bellei, C., Robinson, T., Leiserson, C.E.: Anti-money laundering in bitcoin: experimenting with graph convolutional networks for financial forensics. arXiv preprint arXiv:1908.02591 (2019)
8. 8.Yuan, Z., Yuan, Q., Wu, J.: Phishing detection on Ethereum via learning representation of transaction subgraphs. In: Blocksys, pp. 178–191. Springer, Berlin (2020)
9. 9\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr9"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding Ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. II: Express Briefs **67**(11), 2737–2741 (2020)
10. 10\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr10"></a>Li, S., Gou, G., Liu, C., Hou, C., Li, Z., Xiong, G.: TTAGN: temporal transaction aggregation graph network for ethereum phishing scams detection. In: Proceedings of the ACM Web Conference, pp. 661–669. ACM, New York (2022)
11. 11\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr11"></a>Li, X., Liu, S., Li, Z., Han, X., Shi, C., Hooi, B., Huang, H., Cheng, X.: Flowscope: spotting money laundering based on graphs. In: AAAI, vol. 34, no. 04, pp. 4731–4738 (2020)
12. 12\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr12"></a>Wu, J., Liu, J., Zhao, Y., Zheng, Z.: Analysis of cryptocurrency transactions from a network perspective: an overview. J. Netw. Comput. Appl. **190**, 103139 (2021)[Crossref](https://doi.org/10.1016/j.jnca.2021.103139)
13. 13\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr13"></a>Bartoletti, M., Lande, S., Loddo, A., Pompianu, L., Serusi, S.: Cryptocurrency scams: analysis and perspectives. IEEE Access **9**, 148353–148373 (2021)[Crossref](https://doi.org/10.1109/ACCESS.2021.3123894)
14. 14\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr14"></a>Chen, W., Zheng, Z., Cui, J., Ngai, E., Zheng, P., Zhou, Y.: Detecting Ponzi schemes on ethereum: towards healthier blockchain technology. In: WWW, pp. 1409–1418. ACM, New York (2018)
15. 15\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr15"></a>Ibrahim, R.F., Mohammad Elian, A., Ababneh, M.: Illicit account detection in the ethereum blockchain using machine learning. In: ICIT, pp. 488–493. IEEE, New York (2021)
16. 16\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr16"></a>Tam, D.S.H., Lau, W.C., Hu, B., Ying, Q.F., Chiu, D.M., Liu, H.: Identifying illicit accounts in large scale e-payment networks – a graph representation learning approach. arXiv preprint arXiv:1906.05546 (2019)
17. 17\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr17"></a>Lal, B., Agarwal, R., Shukla, S.K.: Understanding money trails of suspicious activities in a cryptocurrency-based blockchain. arXiv preprint arXiv:2108.11818 (2021)
18. 18\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr18"></a>Sangers, A., van Heesch, M., Attema, T., Veugen, T., Wiggerman, M., Veldsink, J., Bloemen, O., Worm, D.: Secure multiparty pagerank algorithm for collaborative fraud detection. In: FC, pp. 605–623. Springer, Berlin (2019)
19. 19\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr19"></a>Hooi, B., Shah, N., Beutel, A., Günnemann, S., Akoglu, L., Kumar, M., Makhija, D., Faloutsos, C.: Birdnest: Bayesian inference for ratings-fraud detection. In: ICDM, pp. 495–503. SIAM, Philadelphia (2016)
20. 20\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr20"></a>Hooi, B., Song, H.A., Beutel, A., Shah, N., Shin, K., Faloutsos, C.: Fraudar: bounding graph fraud in the face of camouflage. In: SIGKDD, pp. 895–904. ACM, New York (2016)
21. 21\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr21"></a>Kumar, S., Hooi, B., Makhija, D., Kumar, M., Faloutsos, C., Subrahmanian, V.: REV2: fraudulent user prediction in rating platforms. In: WSDM, pp. 333–341. ACM, New York (2018)
22. 22\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr22"></a>Mishra, A., Bhattacharya, A.: Finding the bias and prestige of nodes in networks based on trust scores. In: WWW, pp. 567–576. ACM, New York (2011)
23. 23\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr23"></a>Kurshan, E., Shen, H.: Graph computing for financial crime and fraud detection: trends, challenges and outlook. Int. J. Semant. Comput. **14**(4), 565–589 (2020)[Crossref](https://doi.org/10.1142/S1793351X20300022)
24. 24\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr24"></a>Akoglu, L., Tong, H., Koutra, D.: Graph based anomaly detection and description: a survey. Data Min. Knowl. Discov. **29**(3), 626–688 (2015)[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3334317)[Crossref](https://doi.org/10.1007/s10618-014-0365-y)
25. 25\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr25"></a>Team, C.: Report: Key players of the cryptocurrency ecosystem (2021, Jun.). \[Online]. Available: [https://go.chainalysis.com/rs/503-FAP-074/images/Key-players-in-crypto-report.pdf](https://go.chainalysis.com/rs/503-FAP-074/images/Key-players-in-crypto-report.pdf)
26. 26\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr26"></a>Victor, F., Weintraud, A.M.: Detecting and quantifying wash trading on decentralized cryptocurrency exchanges. In: WWW, pp. 23–32. ACM, New York (2021)
27. 27\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr27"></a>Brin, S., Page, L.: The anatomy of a large-scale hypertextual web search engine. Comput. Netw. ISDN Syst. **30**(1), 107–117 (1998)[Crossref](<https://doi.org/10.1016/S0169-7552(98)00110-X>)
28. 28\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr28"></a>Akoglu, L., Chandy, R., Faloutsos, C.: Opinion fraud detection in online reviews by network effects. In: Proceedings of the International AAAI Conference on Web and Social Media, vol. 7, no. 1, pp. 2–11 (Aug. 2013)
29. 29\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr29"></a>Al-E’mari, S., Anbar, M., Sanjalawe, Y., Manickam, S.: A labeled transactions-based dataset on the ethereum network. Commun. Comput. Inf. Sci. **1347**, 61–79 (2021)
30. 30\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr30"></a>Agarwal, R., Barve, S., Shukla, S.K.: Detecting malicious accounts in permissionless blockchains using temporal graph properties. Appl. Netw. Sci. **6**(1), 9 (2021)[Crossref](https://doi.org/10.1007/s41109-020-00338-3)
31. 31\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr31"></a>Chen, L., Peng, J., Liu, Y., Li, J., Xie, F., Zheng, Z.: Phishing scams detection in ethereum transaction network. ACM Trans. Internet Technol. **21**(1), 1–16 (2021)[Crossref](https://doi.org/10.1145/3398071)
32. 32\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr32"></a>Zhu, J., Rossi, R.A., Rao, A., Mai, T., Lipka, N., Ahmed, N.K., Koutra, D.: Graph neural networks with heterophily. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 12, pp. 11168–11176 (2021)
33. 33\.<a id="oebps-html-619883_1_en_7_chapter-xhtml-cr33"></a>Huang, T., Lin, D., Wu, J.: Ethereum account classification based on graph convolutional network. IEEE Trans. Circuits Syst. II: Express Briefs **69**(5), 2528–2532 (2022)

<a id="oebps-html-619883_1_en_8_chapter-xhtml"></a>

© The Author(s), under exclusive license to Springer Nature Singapore Pte Ltd. 2025J. Wu et al. (eds.)Blockchain Transaction Data AnalyticsBig Data Management[https://doi.org/10.1007/978-981-97-4430-5_8](https://doi.org/10.1007/978-981-97-4430-5_8)

# 8. Transaction Tracking Based on Personalized PageRank Algorithm

Zhiying Wu[1](#oebps-html-619883_1_en_8_chapter-xhtml-aff4) , Jieli Liu[1](#oebps-html-619883_1_en_8_chapter-xhtml-aff4) , Jiajing Wu[1](#oebps-html-619883_1_en_8_chapter-xhtml-aff4) and Zibin Zheng[1](#oebps-html-619883_1_en_8_chapter-xhtml-aff4)

<a id="oebps-html-619883_1_en_8_chapter-xhtml-aff4"></a>

(1)Sun Yat-sen University, Guangzhou, China

<a id="oebps-html-619883_1_en_8_chapter-xhtml-contactofauthor1"></a>

**Zhiying Wu (Corresponding author)Email:** [wuzhy95@mail2.sysu.edu.cn](mailto:wuzhy95@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_8_chapter-xhtml-contactofauthor2"></a>

**Jieli LiuEmail:** [liujli7@mail2.sysu.edu.cn](mailto:liujli7@mail2.sysu.edu.cn)

<a id="oebps-html-619883_1_en_8_chapter-xhtml-contactofauthor3"></a>

**Jiajing Wu (Corresponding author)Email:** [wujiajing@mail.sysu.edu.cn](mailto:wujiajing@mail.sysu.edu.cn)

<a id="oebps-html-619883_1_en_8_chapter-xhtml-contactofauthor4"></a>

**Zibin ZhengEmail:** [zhzibin@mail.sysu.edu.cn](mailto:zhzibin@mail.sysu.edu.cn)

## Abstract

Recently, both the academic and industrial communities have devoted significant efforts to unveil the true entities behind pseudo-anonymous accounts on the blockchain and to recover stolen funds from vast transaction data. We model blockchain transaction records as transaction graphs and view blockchain transaction tracking as a graph search task. To achieve efficient and effective tracking of fund transfers in transaction graphs, we propose an scalable transaction tracking tool, TRacer. To the best of our knowledge, this is the first tool designed for multiple account-based blockchain platforms and capable of handling complex transaction behaviors in decentralized finance (DeFi). Specifically, we address the transaction tracking task using a subgraph search approach, which employs a novel ranking method to infer the correlation between accounts during the graph search process in multi-relational blockchain transaction graphs. Theoretical analysis and experimental results on datasets from multiple blockchain platforms demonstrate that TRacer can perform transaction tracking tasks more efficiently at lower costs and achieve better tracking results compared to existing methods or even expert manual audits.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec1"></a>

## 8.1 Introduction

According to a report by the well-known blockchain security firm Chainalysis \[[1](#oebps-html-619883_1_en_8_chapter-xhtml-cr1)], illicit transactions,such as financial fraud and hacking attacks and money laundering, in the cryptocurrency-related business have caused losses exceeding \$14 billion in 2021. In particular, with the rise of DeFi, most of these illicit activities and malicious attacks occur in account-based blockchain transaction systems, such as Ethereum and Binance Smart Chain (BSC) \[[2](#oebps-html-619883_1_en_8_chapter-xhtml-cr2)].

Various technologies have been developed to combat financial crimes in blockchain transaction systems based on publicly accessible blockchain transaction data \[[3](#oebps-html-619883_1_en_8_chapter-xhtml-cr3)–[8](#oebps-html-619883_1_en_8_chapter-xhtml-cr8)]. These technologies can be divided into two categories: **proactive (pre-transaction) risk alerting** and **remedial (post-transaction) fund tracing**. Proactive risk alerting typically assesses the risk of new transactions by evaluating the behavior of historically related accounts and existing label information. Data-driven detection techniques can identify anomalies or illegal activities, such as phishing scams \[[9](#oebps-html-619883_1_en_8_chapter-xhtml-cr9), [10](#oebps-html-619883_1_en_8_chapter-xhtml-cr10)], price manipulation \[[11](#oebps-html-619883_1_en_8_chapter-xhtml-cr11)], and money laundering \[[12](#oebps-html-619883_1_en_8_chapter-xhtml-cr12)], which fall within this scope. However, as shown in Fig. [8.1](#oebps-html-619883_1_en_8_chapter-xhtml-fig1)a, although proactive early warning can alert high-risk transactions before they occur, it cannot prevent criminals who have already laundered funds and cashed out illegal gains through transactions due to the pseudonymity and distributed nature of blockchain systems. Therefore, significant efforts have been made to trace the proceeds of crime \[[13](#oebps-html-619883_1_en_8_chapter-xhtml-cr13)–[15](#oebps-html-619883_1_en_8_chapter-xhtml-cr15)], aiming to de-anonymize the related fund flows and assist victims in recovering losses.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig1"></a>

***Fig. 8.1***

(**a**) Proactive risk warning in blockchain raises warnings for risky transactions. (**b**) Remedial money tracing in blockchain traces the money flow among the source and the targets possessing the laundered funds, also providing evidence to catch the criminals off-chain

Figure [8.1](#oebps-html-619883_1_en_8_chapter-xhtml-fig1)b illustrates an example of emergency fund tracking. Typically, the process of tracking transactions starts from a source and traces the flow of funds to a target. Here, the ***source*** represents a subject of tracking, such as a blockchain account belonging to a fraudster fleeing with a large amount of illicit proceeds, while the ***target*** indicates an account used to aggregate ”clean” funds awaiting withdrawal. Although the identity information of accounts in the blockchain system is unknown, once we identify the target deposit address on exchanges, these exchanges usually perform Know Your Customer (KYC) procedures, enabling the relevant criminals to be identified and apprehended off-chain based on the KYC information provided by the exchanges \[[16](#oebps-html-619883_1_en_8_chapter-xhtml-cr16)].

Currently, the methods used for blockchain transaction tracing \[[17](#oebps-html-619883_1_en_8_chapter-xhtml-cr17)–[20](#oebps-html-619883_1_en_8_chapter-xhtml-cr20)] are mainly based on rule-based heuristics and taint analysis \[[21](#oebps-html-619883_1_en_8_chapter-xhtml-cr21)]. However, as an emerging research topic, existing transaction tracing methods have limitations in terms of effectiveness, universality, and efficiency.

In this chapter, we propose the *first* intelligent transaction Tracing tool for account-based blockchain transaction systems, named **TRacer**. This tool integrates a scalable Ranking algorithm for estimating the correlation between accounts and is capable of handling complex DeFi operations and massive transaction records at a lower cost. As depicted in Fig. [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-fig2), TRacer models complex DeFi operations in blockchain transaction systems as a directed, weighted, temporal, and multi-relational graph. Subsequently, we devise a ranking-guided graph expansion method to identify subgraphs around the sources of risk, revealing the flow of funds between the source and other accounts, with a novel ranking method that offers scalability and effectiveness advantages. Finally, we conduct local community detection on the subgraphs obtained through graph expansion around the risk seeds, which are concise enough to assist future expert audits. Experimental results demonstrate the performance of TRacer in account-based blockchain transaction tracing. Our tool code and data are available online.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn1_source"></a>[1](#oebps-html-619883_1_en_8_chapter-xhtml-fn1) The main contributions of our work can be summarized as follows:

- To the best of our knowledge, we are the first research team to investigate intelligent transaction tracing specifically targeting account-based blockchain trading systems like Ethereum. This is an urgent issue given the increasing number of security incidents in blockchain systems.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig2"></a>

  ***Fig. 8.2***

  The framework of TRacer. TRacer first models DeFi actions into a graph. Then, given a risk source, TRacer searches a subgraph surrounding the source via graph expansion and extracts the key money flows for expert auditing via local community detection

- We have designed and implemented a generic blockchain transaction tracing tool called TRacer, which incorporates the complex semantics of DeFi operations into the transaction network and employs an effective and scalable ranking method to estimate the relevance of accounts.

- We have thoroughly evaluated the performance of TRacer through theoretical analysis and experimental assessments, demonstrating its effectiveness and scalability. Additionally, we have contributed a benchmark dataset consisting of 20 real transaction tracing cases initiated by illicit activities, which have been reported and manually verified by experts from blockchain security companies.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec2"></a>

## 8.2 Preliminaries

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec3"></a>

### 8.2.1 Problem Definition

The transaction tracing task in account-based blockchain trading systems aims to track the flow of funds from a given source account to a target account where funds are aggregated and await cashing out, prioritizing fund flows for further manual verification by auditors. By modeling blockchain transaction relationships as a graph, where nodes represent accounts and edges represent fund flow relationships, we formalize the transaction tracing problem as a subgraph search problem, described as follows.

- **Source:** A given tracing object such as an account of a blockchain fraudsters.
- **Target:** The pseudonymous accounts where the funds from the source finally stay. Once a target deposit account of an exchange that enforce KYC processes is located, the real identity of the target and its corresponding source can be revealed.
- **Problem formulation:** Given a source node *s* in a transaction graph *G*, the objective is to search for a connected fund transfer subgraph \$\$G_{s}\$$ from *s* to its fund flow targets around the neighborhood of *s*. \$\$G_{s}\$$ should ideally encompass as many target nodes as possible within the smallest possible subgraph size, facilitating easier further manual verification.

Please note that transaction tracing methods may apply to blockchain fraud cases that have been disclosed but not fully investigated, i.e., only a small portion of accounts or transactions related to the cases have been identified. Therefore, to ensure the applicability of our method to most cases, in this chapter, we assume a worst-case scenario for transaction tracing, where only one associated account is known.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec4"></a>

### 8.2.2 Discussion of Method Design

As stated in the problem definition, the transaction tracing task is modeled as a subgraph search problem in the transaction graph, and addressed through a biased graph search approach. Specifically, in the biased search process, we employ a personalized ranking method that takes into account the characteristics of fund flows (such as amount, DeFi operation types) to guide the search direction. Next, we elaborate on the observations and findings that inspired us to adopt the aforementioned methodology in our design. Our motivations for the design are as follows:

**(1) Local Searching Surpasses Clustering**

Two kinds of methods, i.e., clustering and local searching, can be used to tackle the subgraph searching problem. Clustering methods aim to cluster the relevant nodes, based on their similarity in terms of features or topological structure. However, the accounts related to the risky source are not necessarily similar. For example, hackers and token swap intermediaries are closely connected and both have large transaction volumes, but they do not intuitively belong to the same cluster. On the contrary, the local searching methods, which start from given accounts, can adjust the search direction while exploring the money flow and bypass the accounts with different roles, thus relieving the aforementioned problems.

**(2) Practicality Favors a Biased Search**

Local searching from a given source can be conducted in either blind or biased manners. Typical blind searching methods include Breadth First Search (BFS) and Depth First Search (DFS). In the transaction tracing process, blind searching methods probably collect a large number of unrelated transactions and suffer from the search explosion problem. For the transaction tracing task considered here, it is preferable to use biased search methods to guide the search in the proper direction due to the following two reasons. On the one hand, the transaction information (e.g., amount and timestamp) can be leveraged to evaluate the search bias, which is conducive to the recovery of real money flow and ensuring the effectiveness of transaction tracing. On the other hand, searching bias guides transaction tracing to avoid unrelated transactions, thus reducing transaction data access and improving execution efficiency. In Fig. [8.3](#oebps-html-619883_1_en_8_chapter-xhtml-fig3)a and b, we compare the tracing results of two searching methods, i.e., BFS (blind searching) and Poison \[[21](#oebps-html-619883_1_en_8_chapter-xhtml-cr21)] (a heuristic biased search), on a real case, the Bitfinex incident \[[22](#oebps-html-619883_1_en_8_chapter-xhtml-cr22)]. After querying the same quantity of accounts, the biased search method Poison can successfully recover the money flow between the source and target, but BFS fails.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig3"></a>

***Fig. 8.3***

The tracing results of (**a**) BFS (a typical blind search) and (**b**) Poison (a typical biased search) on the Bitfinex incident with the same number of accessed accounts, where orange nodes represent the accessed accounts, and gray nodes represent the un-accessed accounts. We observe Poison successfully reaches the target while BFS fails

**(3) Personalized Ranking Boosts Search Quality**

Biased searching requires iterative querying of the neighbor nodes with the highest relevance, and therefore a ranking technique is needed to rank the relevance of different nodes. Node relevance ranking techniques can be divided into two categories, namely global ranking and personalized ranking. Figure [8.4](#oebps-html-619883_1_en_8_chapter-xhtml-fig4) gives a comparison between the ranking results of two kinds of ranking methods, namely PageRank (global ranking) and personalized PageRank (personalized ranking), on the accounts related to the Bitfinex incident. We can observe that global ranking has limits in two aspects: (i) The ranking is calculated with the global transaction information, making it difficult to focus on particular money flows related to risky accounts and thus may mislead the search direction. (ii) Global ranking requires acquiring and processing the entire transaction graph, making it challenging to ensure execution efficiency. On the contrary, personalized ranking only ranks the neighbors of a source, which leads searching methods to concentrate more on the accounts and transactions closely related to the risk source. Thus, personalized ranking is more intuitive and efficient than global ranking for transaction tracing tasks.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig4"></a>

***Fig. 8.4***

Two kinds of ranking methods, i.e., (**a**) PageRank (global ranking) and (**b**) personalized PageRank (personalized ranking), run on the Bitfinex incident. The darker the node color, the higher the account ranking and the more relevant the account is to the money flow

In summary, based on experimental observations on real cases and the above insights, this chapter proposes a *personalized ranking approach* to rank accounts in the neighborhood of the risk source and use it as a basis for a *biased graph search* to *trace the money flow* from the source to the targets.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec5"></a>

## 8.3 Methodology of Transaction Tracing

This section introduces the architecture and implementation of TRacer.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec6"></a>

### 8.3.1 Architecture Overview

TRacer consists of three main modules, including graph construction, graph expansion, and local community detection. To model DeFi actions between accounts, we designed the graph construction module to formalize transactions into a graph. Additionally, to pinpoint potential fund flows, the graph expansion module starts from a given risky account and finds a subgraph. Lastly, the local community discovery module extracts a critical small-scale local community from the expanded subgraph for further validation. Descriptions of each module are as follows:

- **Graph construction**: The module models the DeFi actions between accounts into directed, weighted, temporal, and multi-relationship graphs.
- **Graph expansion**: Since the blockchain data contains billions of transactions which is too large for common graph algorithms, this module aims to find a relevant subgraph from a risky source. The module contains four operations: ***Expand*** collects all edges related to a given node, ***Push*** merges the collected edges to the subgraph, ***Rank*** computes the relevance of nodes in the subgraph to the source, and ***Pop*** selects a node for expanding. The graph expansion process terminates when the end condition is met.
- **Local community detection**: This module ***Extract***s a local community of the source node from the expended subgraph, in which nodes have higher relevance to the source than nodes out of the community.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec7"></a>

### 8.3.2 Graph Construction

Since there are multiple types of tokens in account-based blockchain trading systems, we formulate the money transfer relationships among accounts into a directed, weighted, temporal, and multi-relationship graph \$\$G=(V, E)\$$, where *V* is the node set representing accounts, *E* is the edge set representing the token transfer relationships. An edge \$\$e=(u,v,w,t,b,h)\$$ denotes that account *u* transfer *w* units token *b* to account *v* at timestamp *t* with a transaction hash *h*. We define mapping functions \$\$f_{src}\$$, \$\$f_{tgt}\$$, \$\$f_{amt}\$$, \$\$f_{ts}\$$, and \$\$f_{sym}\$$ to map each edge to its source, target, amount, timestamp, and token type respectively. There are multiple types of edges indicating the transfer relationships of different tokens.

According to recent blockchain security reports \[[1](#oebps-html-619883_1_en_8_chapter-xhtml-cr1), [11](#oebps-html-619883_1_en_8_chapter-xhtml-cr11), [23](#oebps-html-619883_1_en_8_chapter-xhtml-cr23), [24](#oebps-html-619883_1_en_8_chapter-xhtml-cr24)], DeFi actions are widely exploited to confuse the source of money flow in account-based blockchains. In contrast to current approaches \[[17](#oebps-html-619883_1_en_8_chapter-xhtml-cr17)–[21](#oebps-html-619883_1_en_8_chapter-xhtml-cr21)], we model DeFi actions in the transaction graph for the first time, which is critical for transaction tracing tasks in account-based blockchains. As shown in Fig. [8.5](#oebps-html-619883_1_en_8_chapter-xhtml-fig5)a and b, we categorize DeFi actions into two typical patterns: **Xfer** and **Swap**. Xfer means sending or receiving tokens through a transaction, while Swap refers to exchanging tokens for another token through a transaction. If the Swap pattern fails to be modeled in the transaction graph, the transaction tracing method will be unable to determine whether the traced token has been converted to another token, resulting in tracing failure. Specifically, in the graph construction, the Xfer pattern includes: (1) ***transfer***: An account sends an amount of token to another account, (2) ***minting***: A token contract mints an amount of token to an account, and (3) ***burning***: An account burns an amount of token. And the Swap pattern includes: (1) ***add liquidity***: An account deposits an amount of token to a DeFi app, and receives a certain amount of Liquidity Provider (LP) token back, (2) ***remove liquidity***: An account sends an amount of LP token to a DeFi app for destroying and gets a certain amount of other tokens back, and (3) ***trade***: An account sells an amount of token A in a DeFi app for a certain amount of token B. We identify the transfer relationships having the same transaction hash and involving both sending and receiving tokens as Swap, otherwise as Xfer.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig5"></a>

***Fig. 8.5***

(**a**) Xfer: Sending or receiving tokens. (**b**) Swap: Exchanging tokens for other kinds of tokens

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec8"></a>

### 8.3.3 Graph Expansion

The graph expansion module aims to obtain a relevant subgraph expanded from a given source via iterating the four operations shown in Fig. [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-fig2). In what follows, we introduce the detailed design of these four operations.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec9"></a>

#### 8.3.3.1 *Push* and *Rank*

The *Push* operation merges the expanded edges to the subgraph in each iteration. While *Rank* operation evaluates the relevance of nodes in the subgraph to the source. In order to evaluate the relevance, we propose a novel personalized ranking method, i.e., **Transaction Tracing Rank (TTR)**. Compared with the current approaches (e.g., personalized PageRank), our ranking method is distinguished by: (i) evaluating the ranking while gradually exploring the money flow without accessing the whole transaction graph; (ii) incorporate transaction information (direction, amount, time, and DeFi actions) to evaluate the ranking of accounts. Specifically, in order to rank while exploring the money flow, we decompose the ranking calculation into *Rank* operation and *Pop* operation, where *Rank* operation incrementally updates the ranking via a local push procedure \[[25](#oebps-html-619883_1_en_8_chapter-xhtml-cr25)] and *Pop* operation determines the next expanding node. We give a detailed introduction to the local push procedure of two existing personalized ranking methods, i.e., personalized PageRank and approximated personalized PageRank, in Appendices and discuss the *Pop* operation in the following subsection. Moreover, by incorporating the transaction information, we design four strategies: tracing tendency, weighted pollution, temporal reasoning, and token redirection. We use \$\$r_s(u,t,b)\$$ to denote the residual of node *u* brought from token \$\$b \\in B\$$ at timestamp \$$t \\in \\Gamma $$, where \$$\\Gamma $$ is the timestamp set and *B* is the token symbol set in the subgraph. In this way, the local push procedure in TTR is described as Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1). During initialization, a part of the residual of node *u* is transformed into the relevance (line 1). Other parts of the residual are pushed to the neighbors according to the following strategies:

<a id="oebps-html-619883_1_en_8_chapter-xhtml-fpar1"></a>

**Algorithm 2 TTR local push**

**Tracing Tendency**

Since a money transfer relationship between accounts is directed, the attention to in-degree neighbors and out-degree neighbors during the local push procedure can be different. In most cases, tracing for the destinations of money flows oriented from a particular source needs to pay more attention to the out-degree neighbors. Therefore, we define an attention coefficient \$\$0 \\leq \\beta \\leq 1\$$. During the residual propagation, the out-degree neighbors in a transaction relationship can get a higher residual when \$\$\\beta &amp;gt; 0.5\$$, and the in-degree neighbors can receive a higher residual when \$\$\\beta &amp;lt; 0.5\$$. As Fig. [8.6](#oebps-html-619883_1_en_8_chapter-xhtml-fig6)a shows, the in-degree neighbors and the out-degree neighbors obtain a different weight in this strategy. Line 6–17 in Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1) describe the residual propagation procedure of different directions with the attention coefficient assigned at line 7.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig6"></a>

***Fig. 8.6***

(**a**) Tracing tendency. Different attention is assigned to the out-degree neighbors and in-degree neighbors. (**b**) Weighted pollution. The higher the edge weight, the closer the relationship. (**c**) Temporal reasoning. Tracing money flow in chronological order, and \$\$t1&amp;lt;t2&amp;lt;t3&amp;lt;t4\$$ in this example. (**d**) Token redirection. Uncovering the token flows even though there exist complex DeFi actions in the Swap pattern

**Weighted Pollution**

In the blockchain transaction graph, the strength of money transfer relationships is weighted by the transaction amount. For each node, a neighbor trading a larger amount of money with the target node is considered to be more relevant to the node. Therefore, in the weighted pollution strategy, we take the weight of the money transfer relationships into account. Figure [8.6](#oebps-html-619883_1_en_8_chapter-xhtml-fig6)b shows an example of this strategy that neighbors of *u* associated by edges with a greater weight can obtain more residual during the propagation procedure. In this way, the residual of a node is distributed to each neighbor associated by edge \$\$e \\in E'\$$ according to the ratio of edge weight \$\$f\_{amt}(e) / \\sum \_{e'' \\in E'}f_{amt}(e'')\$$ as given in line 11 of Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1), where \$\$E'\$$ is the set of edges.

**Temporal Reasoning**

Transactions on blockchains are recorded in blocks chronologically, and each block is assigned with a specific timestamp. With the timestamp information, tracing for the targets of money flows usually follows the paths with increasing timestamps, while tracing back to the source of money flows follows the paths with decreasing timestamps. Therefore, in this strategy we take the temporal information into consideration. Referring to Fig. [8.6](#oebps-html-619883_1_en_8_chapter-xhtml-fig6)c, the residual from the input transaction at *t*2 is pushed out through the outgoing edges after *t*2 and the incoming edge before *t*2. Lines 4–5 in Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1) define the edge set for residual propagation that satisfies this strategy. Moreover, the residual is pushed to the node itself if the edge set is empty (see line 16 in Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1)), indicating that the funds have not been transferred from the node.

**Token Redirection**

This strategy makes the effort to uncover the flow of interesting tokens based on the transaction patterns of Xfer and Swap. As given in Fig. [8.6](#oebps-html-619883_1_en_8_chapter-xhtml-fig6)d, the residual of node *u* from the USDC token in an Xfer edge with hash1 should be pushed through the edges with hash3 and hash4, rather than the USDC outgoing edge with hash2. Since the edges with hash2 are in a Swap pattern and swapped the USDC token into ETH. To achieve the redirection of token flows in complex transaction actions, we define a recursive function \$\$\\rho (\\cdot ,\\cdot )\$$ which can find the initial state of a set of incoming edges before the Swap operations and the final state of a set of outgoing edges after the Swap operations within a node. For example, the initial state before Swap of the incoming edge with hash2 in Fig. [8.6](#oebps-html-619883_1_en_8_chapter-xhtml-fig6)d is the incoming edge with hash1, and the final state after Swap of the outgoing edge with hash2 is the outgoing edges with hash3 and hash4. Specifically, as given in Algorithm [2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar1) line 8–14, the residual of a specific token should be pushed through the redirected edges. Therefore, \$\$\\rho (\\cdot ,\\cdot )\$$ satisfies the following recursive equation:

\$$\\displaystyle \\begin{aligned} {} \\rho(\\mathcal{E}, E(u))=\\mathcal{E}\_{xfer} \\cup \\rho(\\bigcup\\limits\_{e \\in \\mathcal{E}_{swap}} redirect(e), E(u)), \\end{aligned} $$

(8.1)

where \$\$\\mathcal {E}\$$ is a set of edges for redirection, \$\$\\mathcal {E}_{xfer} \\subset \\mathcal {E}\$$ is a set of Xfer edges, \$\$\\mathcal {E}_{swap} \\subset \\mathcal {E}\$$ is a set of Swap edges, and \$\$redirect(\\cdot )\$$ selects the edges in the token types before/after Swap for incoming/outgoing edges \$\$e \\in \\mathcal {E}_{swap}\$$ from edges \$\$E(u)\$$ related to *u*. Especially, \$$\\rho (\\emptyset , E(u)) = \\emptyset $$.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec10"></a>

#### 8.3.3.2 *Pop* and *Expand*

The *Pop* operation selects a node from the subgraph for the next round expansion iteration, and the *Expand* operation expands from a node by collecting all the related edges of this node. Note that the graph expansion in TRacer terminates when the residual of all nodes in the subgraph is below a threshold \$\$\\epsilon \\in (0,1)\$$, i.e., <a id="oebps-html-619883_1_en_8_chapter-xhtml-equ2"></a>

\$$\\displaystyle \\begin{aligned} \\max\\limits\_{u \\in V}(\\sum\_{t \\in \\Gamma}\\sum_{b \\in B}r_s(u,t,b)) &amp;lt; \\epsilon. {} \\end{aligned} $$

(8.2)

Here we employ greedy selection for the *Pop* operation to achieve the condition in Eq. [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-equ2), i.e., the *Pop* operation selects the node in the subgraph with the highest residual.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec11"></a>

### 8.3.4 Local Community Detection

<a id="oebps-html-619883_1_en_8_chapter-xhtml-fpar2"></a>

**Algorithm 3 TTR-based local community detection**

Referring to Fig. [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-fig2), the *Extract* operation utilizes local community detection to construct a small-scale local community from the expanded graph. For a specific risk source node, the importance ranking of nodes within the local community is significantly higher than that of external nodes, making further expert auditing easier.

*Conductance* is a widely considered measure of local community detection \[[25](#oebps-html-619883_1_en_8_chapter-xhtml-cr25)], which is defined as:

\$$\\displaystyle \\begin{aligned} \\Phi(S)=\\frac{\\boldsymbol{p}_s(\\partial(S))}{\\boldsymbol{p}_s(S)}, \\end{aligned} $$

(8.3)

where *S* denotes the nodes of the local community, the boundary \$\$\\partial (S)=\\{ v| (u,v) \\in E \\land u \\in S \\land v \\in \\bar {S} \\}\$$, \$\$\\bar {S}\$$ is the complement of *S* and \$\$\\boldsymbol {p}_s(S)=\\sum _{u \\in S}\\boldsymbol {p}_s(u)\$$ denotes the sum of rank over each node in the local community. A smaller value of conductance is assumed to indicate a denser local community. Given a specific threshold \$\$\\varphi &amp;gt; 0\$$ for conductance, the local community detection aims to find the local community satisfying: <a id="oebps-html-619883_1_en_8_chapter-xhtml-equ4"></a>

\$$\\displaystyle \\begin{aligned} \\Phi(S) &amp;lt; \\varphi. {} \\end{aligned} $$

(8.4)

With \$\$S=\\{s\\}\$$ as the initialization, Algorithm [3](#oebps-html-619883_1_en_8_chapter-xhtml-fpar2) describes how to find the local community satisfying Eq. [8.4](#oebps-html-619883_1_en_8_chapter-xhtml-equ4).

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec12"></a>

## 8.4 Experiments of Transaction Tracing

In this section, we conducted theoretical analysis and experiments to evaluate the effectiveness of TRacer on large-scale real-world datasets. Additionally, we conducted case studies using network visualization techniques.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec13"></a>

### 8.4.1 Theoretical Analysis

In this section, we conduct theoretical analysis to demonstrate that TRacer can accomplish transaction tracing tasks on large-scale transaction graphs at a low cost. Additionally, we discuss the upper limit of tracing depth in TRacer.

In Proposition [8.1](#oebps-html-619883_1_en_8_chapter-xhtml-fpar3), we demonstrate that the cost of TRacer is independent of the size of the graph. Therefore, TRacer can scale to transaction graphs of arbitrary size.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-fpar3"></a>

**Proposition 8.1**

*TRacer runs on a graph size independent cost.*

**Proof**

Following the proof of Lemma 2 in Andersen et al. \[[25](#oebps-html-619883_1_en_8_chapter-xhtml-cr25)], the iteration of graph expansion runs \$\$O(\\frac {1}{\\epsilon \\alpha })\$$ times. As a result, the graph expansion module accesses transactions \$\$O(\\frac {1}{\\epsilon \\alpha })\$$ times. Moreover, the number of nodes with non-zero values in the output TTR score is at most \$\$O(\\frac {1}{\\epsilon \\alpha })\$$, which guarantees the cost of local community detection is \$\$O(\\frac {1}{\\epsilon \\alpha })\$$. Therefore, the cost of all modules in TRacer is independent of the graph size. □

In addition, what depth TRacer can trace in a transaction graph from the source node is described in Proposition [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar4).

<a id="oebps-html-619883_1_en_8_chapter-xhtml-fpar4"></a>

**Proposition 8.2**

*An n-hop neighbor of the source node can be found in the graph obtained by graph expansion, in which n satisfies*

\$$\\displaystyle \\begin{aligned} n \\leq \\frac{log(\\epsilon)}{log(1-\\alpha)} + 1. \\end{aligned} $$

(8.5)

**Proof**

In order to maximize the rank of the neighbors far away from the source node, \$$\\alpha $$ needs to be as small as possible, and \$$\\beta $$ needs to be as close as possible to 0 or 1, which ensures that the residual can be pushed to a specific direction. Let the sum of residual pushed from the source node *s* to the *n*-hop neighbors be \$\$r^{(n)}\$$. Considering \$\$\\beta =1\$$ here, \$\$r^{(n)}\$$ can be obtained by what follows:

\$$\\displaystyle \\begin{aligned} \\begin{cases} &amp;amp; r^{(1)}=(1-\\alpha), \\\\ &amp;amp; r^{(2)} \\geq (1-\\alpha)(r^{(1)}-k_1 \\epsilon)=(1-\\alpha)^2-(1-\\alpha)k_1 \\epsilon, \\\\ &amp;amp; ...... \\\\ &amp;amp; r^{(n)} \\geq (1-\\alpha)(r^{(n-1)}-k\_{n-1} \\epsilon) \\\\ &amp;amp; \\ \\ \\ \\ \\ \\ \\ \\ =(1-\\alpha)^n-\\sum\_{i=1}^{n-1}(1-\\alpha)^{n-i}k_{n-i} \\epsilon, \\\\ \\end{cases} \\end{aligned} $$

(8.6)

where \$\$k_i\$$ represents the number of nodes with residual less than \$$\\epsilon $$ in the *i*-order neighbors of the source node. Therefore, \$\$r^{(n)}\$$ obtains the maximum value when

\$$\\displaystyle \\begin{aligned} \\sum\_{i=1}^{n-1}(1-\\alpha)^{n-i}k_{n-i} \\epsilon = 0, \\end{aligned} $$

(8.7)

which means the residual of each *i*-order node is greater than or equal to \$$\\epsilon $$. This situation exists when the source node is in a path-like graph, whose adjacency matrix *A* satisfies \$\$A(i,i+1)=1\$$ and other elements are 0. Considering the end condition of the local push procedure, the residual of *n*-hop neighbors is

\$$\\displaystyle \\begin{aligned} \\begin{cases} &amp;amp; (1-\\alpha)^n &amp;lt; \\epsilon\\\\ &amp;amp; (1-\\alpha)^{n-1} \\geq \\epsilon \\\\ \\end{cases} \\Rightarrow \\frac{log(\\epsilon)}{log(1-\\alpha)} &amp;lt; n \\leq \\frac{log(\\epsilon)}{log(1-\\alpha)} + 1. \\end{aligned} $$

(8.8)

□

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec14"></a>

### 8.4.2 Experimental Setups

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec15"></a>

#### 8.4.2.1 Transaction Tracing Dataset

We contribute a new benchmark dataset including 20 realistic transaction tracing cases in the recent 5 years across three account-based blockchains, i.e., Ethereum, BNB Chain, and Polygon \[[26](#oebps-html-619883_1_en_8_chapter-xhtml-cr26)]. These cases are initialized by various illegal activities, including hacker attacks, Rug-pull, and scams, which have caused billions of dollars in losses. All these cases are reported and manually verified by experts of blockchain security companies, e.g., Certik,<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn2_source"></a>[2](#oebps-html-619883_1_en_8_chapter-xhtml-fn2) Peckshield,<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn3_source"></a>[3](#oebps-html-619883_1_en_8_chapter-xhtml-fn3) and Chainalysis.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn4_source"></a>[4](#oebps-html-619883_1_en_8_chapter-xhtml-fn4) Some statistics of this dataset are shown in Table [8.1](#oebps-html-619883_1_en_8_chapter-xhtml-tab1). Note that the transaction data in the dataset are obtained from open APIs.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn5_source"></a>[5](#oebps-html-619883_1_en_8_chapter-xhtml-fn5) The activities of these cases have crossed millions of blocks, and we have to trace the money flows of the sources among more than 4 billion money transfers. <a id="oebps-html-619883_1_en_8_chapter-xhtml-tab1"></a>

***Table 8.1***

Statistics of the transaction record data related to the cases

| Field | Description | Number |
| --- | --- | --- |
| Source nodes | The source node related to this case, such as the hacker account and the scam contract. | 20 |
| Target nodes | A set of target nodes related to this case, such as exchange wallets and mixing services. | 0.87K |
| Blocks | The blocks related to these cases. | 23.5M |
| Money transfers | The money transfers contained in the blocks related to these cases. | 4.83B |

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec16"></a>

#### 8.4.2.2 Compared Methods

Our method is compared with current methods based on community detection, graph representation learning, and tainted analysis techniques. Specifically, the benchmark methods for comparison include:

- **LPA** \[[27](#oebps-html-619883_1_en_8_chapter-xhtml-cr27)] and **Louvain** \[[28](#oebps-html-619883_1_en_8_chapter-xhtml-cr28)]: These two community discovery methods can find a close connected subgraph (i.e. community) containing the source node.
- **Ethprivacy** \[[29](#oebps-html-619883_1_en_8_chapter-xhtml-cr29)]: This method identifies Ethereum accounts belonging to the same entity by graph representation learning (i.e. Ethprivacy-1) or manual transaction features such as gas price distribution (i.e. Ethprivacy-2).
- **Metapath2Vec** \[[30](#oebps-html-619883_1_en_8_chapter-xhtml-cr30)]: This graph representation learning method is employed to achieve Ethereum account clustering \[[31](#oebps-html-619883_1_en_8_chapter-xhtml-cr31)], which can find the nodes with similar structural features.
- **BFS** \[[17](#oebps-html-619883_1_en_8_chapter-xhtml-cr17)]: Breadth-first search, which is a widely used method in transaction tracing tasks.
- **Poison** \[[21](#oebps-html-619883_1_en_8_chapter-xhtml-cr21)]: A heuristics biased search method based on taint analysis technology, where each output of a transaction with a dirty input is considered to be tainted.
- **Haircut** \[[21](#oebps-html-619883_1_en_8_chapter-xhtml-cr21)]: A heuristics biased search method based on taint analysis technology, where each output of a transaction with a dirty input is considered to be tainted partially according to the amount value.
- **APPR** \[[25](#oebps-html-619883_1_en_8_chapter-xhtml-cr25)]: The approximate personalized PageRank (APPR) algorithm ranks the relevance of nodes to a given source node based on topology information. This algorithm can be leveraged for ranking-guided, biased searching.

In practice, local search methods such as TRacer, BFS, Poison, Haircut, and APPR can be directly applied to real-time blockchain transaction systems through open APIs without accessing the entire transaction graph. In contrast, methods based on community discovery and graph representation learning (e.g., LPA, Louvain, Ethprivacy, and Metapath2Vec) theoretically require the entire transaction graph as input. Therefore, we pre-collect all transactions from all blocks relevant to the cases to simulate the performance of these methods.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec17"></a>

#### 8.4.2.3 Experimental Settings

In the comparison experiments, all methods based on community discovery and graph representation learning use the parameter settings selected in the previous work. The increase in depth causes the output graph size of BFS and Poison to grow exponentially, making it very difficult to audit transactions. Thus, we set the upper limit of the tracing depth for these two methods as 2. In addition, we use the Haircut method to trace the “dirty money” from the source node until the amount proportion of “dirty money” of all nodes is less than 0.1% of that from the source node. Moreover, we set \$\$\\alpha =0.15\$$, \$\$\\epsilon =10^{-3}\$$ for APPR and TTR, and \$\$\\varphi =10^{-3}\$$, \$\$\\beta =0.7\$$ for TTR to ensure that our method is able to find the paths among the source node and the target nodes with 42-hop at most, according to Proposition [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-fpar4).

All the experiments are conducted on a Linux OS machine equipped with an Intel i9-9940X CPU and 128 GB memory.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec18"></a>

#### 8.4.2.4 Metrics

To evaluate the effectiveness and efficiency of transaction tracing methods, we report the average value of the following metrics in all cases:

- **Recall**: Recall evaluates the ratio of target nodes that can be traced by a method, which is defined as: \$\$Recall = |\\mathcal {V}_t| / |V_t|\$$, where \$\$|\\mathcal {V}_t|\$$ is the number of traced target nodes and \$\$|V_t|\$$ is the number of all target nodes in a case.
- **Number of nodes**: This metric measures the size of the output graph in a case. A smaller output graph is easier to be audited by experts while ensuring recall.
- **Tracing depth**: This metric measures the depth at which the transaction tracking method tracks the transaction graph from the source node, while the tracing depth *K* indicates that the algorithm can detect at most *K* hop neighbors of the source node.
- **Runtime**: We calculate the runtime of the algorithms to measure their efficiency.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec19"></a>

### 8.4.3 Experimental Results

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec20"></a>

#### 8.4.3.1 Scalability vs. Performance

The approximation parameter \$$\\epsilon $$ is an important hyper-parameter for modulating scalability. To examine the effect of \$$\\epsilon $$ on the performance, we repeat experiments with different values of \$$\\epsilon $$ and report the recall as well as the number of traced nodes. As given in Fig. [8.7](#oebps-html-619883_1_en_8_chapter-xhtml-fig7), the value of recall has reached 70% when \$\$\\epsilon = 10^{-1}\$$. When \$$\\epsilon $$ is smaller than \$\$10^{-3}\$$, the increment of recall becomes slow, and the number of nodes rapidly increases. Referring to Proposition [8.1](#oebps-html-619883_1_en_8_chapter-xhtml-fpar3), a smaller value of \$$\\epsilon $$ leads to a larger iteration time. Therefore, taking into account recall, time cost, and the size of the output network, we set \$\$\\epsilon = 10^{-3}\$$ for TRacer in the experiments.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig7"></a>

***Fig. 8.7***

The relationship among Epsilon, Recall, and Node number. Note that the recall has reached 70% with \$\$\\epsilon = 10^{-1}\$$ merely, and the increment of recall becomes slow when \$$\\epsilon $$ is less than \$\$10^{-3}\$$

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec21"></a>

#### 8.4.3.2 Comparative Experiments

Table [8.2](#oebps-html-619883_1_en_8_chapter-xhtml-tab2) shows the performance of different methods, from which we can obtain the following observations. <a id="oebps-html-619883_1_en_8_chapter-xhtml-tab2"></a>

***Table 8.2***

Performance comparison between baselines and TRacer The top 3 best results are in bold

| Methods | Recall (%) | #Nodes (K) | Depth | Runtime (h) |
| --- | --- | --- | --- | --- |
| LPA | 67.76 | 682.30 | **10.35** | 1.76 |
| Louvain | 51.27 | 111.84 | **9.75** | 1.69 |
| Metapath2Vec | – | – | – | \$\$&amp;gt;\$$24 |
| Ethprivacy-1 | – | – | – | \$\$&amp;gt;\$$24 |
| Ethprivacy-2 | 0.01 | **1.89** | 1.10 | 1.78 |
| BFS | **77.02** | 52.50 | 2.00 | **0.05** |
| Poison | 70.06 | 41.45 | 2.00 | **0.03** |
| Haircut | 58.85 | 10.35 | 4.15 | **0.01** |
| APPR | **71.92** | **0.66** | 3.60 | 0.51 |
| **TRacer** | **92.31** | **0.87** | **5.05** | 0.65 |

***Firstly***, the output graphs of community discovery methods, i.e., LPA and Louvain, contain an extremely large number of nodes, which is not conducive to transaction audit. ***Secondly***, for the methods based on graph representation learning (i.e. Metapath2Vec and Ethprivacy-1), we terminate the algorithms in advance since the runtime in a case exceeds 24 hours, making it impossible to respond swiftly to illegal activities. Additionally, the very low recall value (0.01) of Ethprivacy-2, which is based on manual transaction features, indicates that this method hardly traces any target nodes. ***Thirdly***, BFS, Poison, and Haircut can complete transaction tracing tasks quickly, but the size of their output graphs is still enormous, thus making transaction auditing, which normally relies on experts to do it manually, exceptionally challenging. **Fourthly**, effectiveness and efficiency can be balanced by both the APPR and TRacer, and the output graph size are suitable. Especially, TRacer attains the best recall and comparatively high tracing depth.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec22"></a>

#### 8.4.3.3 Ablation Experiments

TRacer consists of three main modules including graph construction, graph expansion, and local community detection. In order to discuss the function of different modules, we conduct an ablation study and report the performance of TRacer in Table [8.3](#oebps-html-619883_1_en_8_chapter-xhtml-tab3) after removing the DeFi pattern recognition in graph construction and the local community detection. When the DeFi pattern recognition is removed in the graph construction module, the recall decreases significantly, which shows that the understanding of DeFi patterns in TRacer can help trace the money flows effectively. Moreover, if the local community detection module is removed, the number of nodes increases significantly with the weakly improvement of recall, which suggests that the local community detection module can find the nodes strongly associated with the source node at the cost of a slight recall loss. <a id="oebps-html-619883_1_en_8_chapter-xhtml-tab3"></a>

***Table 8.3***

Ablation experiments

| Graph construction |  | Local community |  | Number of |
| --- | --- | --- | --- | --- |
| with DeFi patterns | Graph expansion | detection | Recall (%) | nodes (K) |
| \$$\\surd $$ | \$$\\surd $$ | \$$\\surd $$ | 92.3 | 0.87 |
|  | \$$\\surd $$ | \$$\\surd $$ | 80.3 | 0.55 |
| \$$\\surd $$ | \$$\\surd $$ |  | 95.9 | 57.5 |

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec23"></a>

#### 8.4.3.4 Top*N* Recall

Since the rank of a node represents the relevance relationship between this node and the source node, we can audit the nodes according to the descending order of rank. To compare the rank-based methods including Haircut, APPR, and TRacer, we take out the top *N* most relevant nodes to the source and calculate the recall for different *N*. The result is displayed in Fig. [8.8](#oebps-html-619883_1_en_8_chapter-xhtml-fig8), where the curve of TRacer shows a better performance in terms of recall than other methods. In addition, TRacer achieves a 25% recall gain over APPR when \$\$N&amp;gt;50\$$.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig8"></a>

***Fig. 8.8***

Top *N* most relevant nodes and the recall

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec24"></a>

#### 8.4.3.5 Responsible Disclosure

We believe that responsible disclosure is part of our obligation, and we are willing to provide the key fund flows identified by TRacer to the whistleblowers of fraud cases to help them understand the entire process of the case and recover their losses. For example, in the Cryptopia hack case (discussed in the next section), TRacer detected illegal funds flowing into the cryptocurrency exchange OKEx. We subsequently sent this discovery to the whistleblower of the case, who had not previously identified this fund flow through manual tracking. We are currently developing the method introduced in this chapter into an online tool, which has the potential to assist victims or organizations of blockchain fraud in recovering their losses.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec25"></a>

### 8.4.4 Case Studies

In this part, we visualize the traced money flow of two cases with Gephi 0.9.2 \[[32](#oebps-html-619883_1_en_8_chapter-xhtml-cr32)], in order to evaluate the feasibility of TRacer.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec26"></a>

#### 8.4.4.1 Cryptopia

Cryptopia exchange was hacked in May 2019. According to the tracking results released by CoinHolmes,<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn6_source"></a>[6](#oebps-html-619883_1_en_8_chapter-xhtml-fn6) the source node with the prefix 0xd4e79<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn7_source"></a>[7](#oebps-html-619883_1_en_8_chapter-xhtml-fn7) possessed 30.8K stolen ETH from Cryptopia and transferred approximately 10K ETH to four target nodes labeled as EtherDelta.

Figure [8.9](#oebps-html-619883_1_en_8_chapter-xhtml-fig9) displays the transaction tracing results of our method, with source and target nodes labeled. Additionally, the size of nodes is proportional to their ranking in importance to the source node. Larger nodes indicate higher relevance to the source node. Based on the tracing results, we can easily locate four target nodes labeled as EtherDelta within the 2-hop neighborhood of the source node, consistent with CoinHolmes’ findings.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig9"></a>

***Fig. 8.9***

Tracing visualization for Cryptopia. Besides the EtherDelta exchange marked by experts, our method also finds the other exchanges including Yobit.net and OKEx

Furthermore, the graph also reveals four-hop neighbors of the source node labeled as Yobit.net<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn8_source"></a>[8](#oebps-html-619883_1_en_8_chapter-xhtml-fn8) and two labeled as OKEx, which were not mentioned in CoinHolmes’ report. In fact, Yobit.net and OKEx are exchanges where the hacker could cash out the stolen ETH. According to the traced fund flows in the graph, approximately 1420 stolen ETH were transferred to Yobit.net, while 18.47K stolen ETH were transferred to OKEx. Therefore, in this case, our method traced over 97% of the stolen ETH from Cryptopia.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec27"></a>

#### 8.4.4.2 Kucoin

Kucoin exchange was hacked in September 2020, and a large amount of stolen funds remains untraceable to this day. As shown in Fig. [8.10](#oebps-html-619883_1_en_8_chapter-xhtml-fig10), the hacker’s source node<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn9_source"></a>[9](#oebps-html-619883_1_en_8_chapter-xhtml-fn9) obtained ETH from a node labeled as Kucoin and then transferred most of the stolen ETH to a well-known privacy protection protocol called Tornado Cash \[[29](#oebps-html-619883_1_en_8_chapter-xhtml-cr29)].<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig10"></a>

***Fig. 8.10***

Tracing visualization for Kucoin. A large number of ETH was transferred to Tornado Cash

According to the tracing results obtained by our method, a total of 13.8K ETH was transferred to the 100 ETH fund pool of Tornado Cash, which is consistent with the conclusions of experts from SlowMist.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn10_source"></a>[10](#oebps-html-619883_1_en_8_chapter-xhtml-fn10) Since Tornado Cash is a decentralized mixing service, we cannot obtain valuable KYC information from the project to identify the hacker. Additionally, due to the design of Tornado Cash based on zero-knowledge proofs, liquidity mining, and smart contracts, it is difficult to trace downstream fund flows when funds are transferred to Tornado Cash. Therefore, in recent years, some researchers have analyzed Tornado Cash \[[29](#oebps-html-619883_1_en_8_chapter-xhtml-cr29)].

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec28"></a>

#### 8.4.4.3 Axie Infinity

Axie Infinity, a famous gaming project on the Ronin chain,<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn11_source"></a>[11](#oebps-html-619883_1_en_8_chapter-xhtml-fn11) suffered an attack in March 2022, resulting in a loss of over $600 million. According to Certik<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn12_source"></a>[12](#oebps-html-619883_1_en_8_chapter-xhtml-fn12)’s tracking report, the attacker’s source node transferred the stolen funds to Tornado Cash and two exchanges, namely FTX and Huobi.

Figure [8.11](#oebps-html-619883_1_en_8_chapter-xhtml-fig11) displays the transaction tracing results of TRacer for this case. Compared to the tracking results provided by Certik, TRacer identified two additional exchanges, Binance and Kucoin, which provided initial funding to the source. Additionally, TRacer also discovered another target exchange, Hotbit, which was not reported by Certik’s experts. These results indicate that TRacer’s tracing capability sometimes surpasses that of manual audits by experts.<a id="oebps-html-619883_1_en_8_chapter-xhtml-fig11"></a>

***Fig. 8.11***

Tracing visualization for Ronin. The money of the source node comes from the green node, while the purple and blue nodes are the targets

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec29"></a>

## 8.5 Conclusion

In this chapter, we investigated the transaction tracing problem in account-based blockchain trading systems and proposed TRacer, the first intelligent transaction tracing tool. In contrast to existing heuristic and taint analysis-based methods, which often require expert knowledge and manual intervention, TRacer demonstrates significant advantages in terms of universality, effectiveness, and time cost. In TRacer, we first model DeFi operations in account transactions as a directed, weighted, temporal, and multi-relational graph. Unlike prior work that models blockchain transactions as simple edges, we categorize transactions into two types of edges, namely Xfer and Swap, based on the DeFi operations in transactions, thereby better representing the transaction semantics in the transaction graph. Subsequently, we propose a ranking-based graph searching method on the transaction graph to trace fund flows. Specifically, we introduce a novel personalized ranking method, namely TTR, for effective and low-cost transaction tracing, which can also handle complex DeFi transaction operations in account-based blockchains. Theoretical analysis and experimental results validate the effectiveness of TRacer.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-sec30"></a>

## Appendix

**Personalized PageRank**

The personalized PageRank vector \$\$\\boldsymbol {p}_s\$$ of a source node *s* in a graph \$\$G=(V,E)\$$ is defined as the unique solution of Eq. [8.9](#oebps-html-619883_1_en_8_chapter-xhtml-equ9), i.e., <a id="oebps-html-619883_1_en_8_chapter-xhtml-equ9"></a>

\$$\\displaystyle \\begin{aligned} \\boldsymbol{p}_s = \\alpha \\boldsymbol{e}_s + (1-\\alpha) \\boldsymbol{p}_s M, {} \\end{aligned} $$

(8.9)

where \$$\\alpha $$ is a teleport constant between 0 and 1, \$\$\\boldsymbol {e}_s\$$ is the indicator vector with a single nonzero element of 1 at *s*, *M* is a transition matrix and \$\$M=D^{-1}A\$$ where *D* and *A* are degree matrix and adjacency matrix. The definition of personalized PageRank is equivalent to simulating a random walk starting from *s*, and \$\$\\boldsymbol {p}_s\$$ is a probability vector where \$\$\\boldsymbol {p}_s(u)\$$ is the probability that a certain random walk beginning at *s* terminates at *u*.

**Approximate Personalized PageRank (APPR)**

The first algorithm proposed to calculate personalized PageRank is power iteration \[[33](#oebps-html-619883_1_en_8_chapter-xhtml-cr33)], which requires high time complexity and not effective in large-scale networks. Therefore, various efficient approximate solutions of personalized PageRank have been proposed, and the most widely used one is called the “local push” algorithm \[[25](#oebps-html-619883_1_en_8_chapter-xhtml-cr25)]. This algorithm starts with all probability residual on the source node of the graph, and pushes the residual to the neighbors iteratively. During the iterations, the residual of each node can be transformed into the relevance to the source node. Finally an estimate of \$\$\\boldsymbol {p}_s\$$ can be obtained. In the algorithm, a residual vector \$\$\\boldsymbol {r}_s\$$ is used to maintain the residual, where \$\$\\boldsymbol {r}_s(u)\$$ denotes the residual of node *u*. By setting \$\$\\boldsymbol {p}_s=\\mathbf {0}\$$ and \$\$\\boldsymbol {r}_s=\\boldsymbol {e}_s\$$ for initialization, the local push procedure updates the value of \$\$\\boldsymbol {p}_s(u)\$$ as follows:

\$$\\displaystyle \\begin{aligned} \\begin{cases} &amp;amp; \\boldsymbol{p}_s(u)=\\boldsymbol{p}_s(u)+\\alpha \\boldsymbol{r}_s(u) \\\\ &amp;amp; \\boldsymbol{r}_s(v)=\\boldsymbol{r}_s(v)+(1-\\alpha)\\boldsymbol{r}_s(u) / d(u) \\\\ \\end{cases}, {} \\end{aligned} $$

(8.10)

where \$\$v \\in N(u)\$$ is the neighbor of *u*, and \$\$d(u)\$$ is the degree of *u*. The local push procedure stops when the residual of each node in *G* is within \$$\\epsilon $$.

<a id="oebps-html-619883_1_en_8_chapter-xhtml-bib1"></a>

**References**

1. 1\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr1"></a>Chainalysis: Crypto crime trends for 2022: Illicit transaction activity reaches all-time high in value, all-time low in share of all cryptocurrency activity. [https://blog.chainalysis.com/reports/2022-crypto-crime-report-introduction/](https://blog.chainalysis.com/reports/2022-crypto-crime-report-introduction/) (2022)
2. 2\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr2"></a>Binance: Binance chain documentation. [https://docs.binance.org/](https://docs.binance.org/) (2020)
3. 3\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr3"></a>Li, X., Jiang, P., Chen, T., Luo, X., Wen, Q.: A survey on the security of blockchain systems. Future Gener. Comput. Syst. **107**, 841–853 (2020)[Crossref](https://doi.org/10.1016/j.future.2017.08.020)
4. 4.Huang, Y., Wang, H., Wu, L., Tyson, G., Luo, X., Zhang, R., Liu, X., Huang, G., Jiang, X.: Understanding (mis)behavior on the EOSIO blockchain. In: Proc. ACM Meas. Anal. Comput. Syst., vol. 4, no. 2, Boston, pp. 1–28 (2020)
5. 5.Xia, P., Wang, H., Zhang, B., Ji, R., Gao, B., Wu, L., Luo, X., Xu, G.: Characterizing cryptocurrency exchange scams. Comput. Secur. **98**, 101993 (2020)[Crossref](https://doi.org/10.1016/j.cose.2020.101993)
6. 6.Wu, J., Liu, J., Zhao, Y., Zheng, Z.: Analysis of cryptocurrency transactions from a network perspective: an overview. J. Netw. Comput. Appl. **190**, 103139 (2021)[Crossref](https://doi.org/10.1016/j.jnca.2021.103139)
7. 7.Lin, D., Chen, J., Wu, J., Zheng, Z.: Evolution of ethereum transaction relationships: toward understanding global driving factors from microscopic patterns. IEEE Trans. Comput. Soc. Syst. **9**, 559–570 (2022)[Crossref](https://doi.org/10.1109/TCSS.2021.3093384)
8. 8\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr8"></a>Lin, D., Wu, J., Yuan, Q., Zheng, Z.: Modeling and understanding ethereum transaction records via a complex network approach. IEEE Trans. Circuits Syst. **67-II**, 2737–2741 (2020)
9. 9\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr9"></a>Wu, J., Yuan, Q., Lin, D., You, W., Chen, W., Chen, C., Zheng, Z.: Who are the phishers? Phishing scam detection on Ethereum via network embedding. IEEE Trans. Syst. Man Cybern. Syst. **52**(2), 1156–1166 (2022)[Crossref](https://doi.org/10.1109/TSMC.2020.3016821)
10. 10\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr10"></a>Zhou, J., Hu, C., Chi, J., Wu, J., Shen, M., Xuan, Q.: Behavior-aware account de-anonymization on Ethereum interaction graph. IEEE Trans. Inf. Forensics Secur. **17**, 3433–3448 (2022)[Crossref](https://doi.org/10.1109/TIFS.2022.3208471)
11. 11\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr11"></a>Wu, S., Wang, D., He, J., Zhou, Y., Wu, L., Yuan, X., He, Q., Ren, K.: DeFiRanger: detecting price manipulation attacks on DeFi applications. CoRR, abs/2104.15068 (2021)
12. 12\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr12"></a>Weber, M., Domeniconi, G., Chen, J., Weidele, D.K.I., Bellei, C., Robinson, T., Leiserson, C.E.: Anti-money laundering in Bitcoin: experimenting with graph convolutional networks for financial forensics. CoRR, abs/1908.02591 (2019)
13. 13\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr13"></a>Yousaf, H., Kappos, G., Meiklejohn, S.: Tracing transactions across cryptocurrency ledgers. In: Proc. 2019 USENIX Secur. Symp., Santa Clara, pp. 837–850 (2019)
14. 14.Wu, L., Hu, Y., Zhou, Y., Wang, H., Luo, X., Wang, Z., Zhang, F., Ren, K.: Towards understanding and demystifying Bitcoin mixing services. In: Proc. Web Conf. (WWW), New York, pp. 33–44 (2021)
15. 15\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr15"></a>Di Battista, G., Di Donato, V., Patrignani, M., Pizzonia, M., Roselli, V., Tamassia, R.: Bitconeview: visualization of flows in the Bitcoin transaction graph. In: Proc. 2015 IEEE Symp. Vis. Cyber Secur., Chicago, pp. 1–8 (2015)
16. 16\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr16"></a>Wu, J., Liu, J., Chen, W., Huang, H., Zheng, Z., Zhang, Y.: Detecting mixing services via mining Bitcoin transaction network with hybrid motifs. IEEE Trans. Syst. Man Cybern. Syst. **52**(4), 2237–2249 (2022)[Crossref](https://doi.org/10.1109/TSMC.2021.3049278)
17. 17\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr17"></a>Zhao, C., Guan, Y.: A graph-based investigation of Bitcoin transactions. In: Proc. Adv. Digit. Forensics XI - 11th IFIP WG 11.9 Int. Conf., Orlando, pp. 79–95 (2015)
18. 18.Phetsouvanh, S., Oggier, F., Datta, A.: Egret: extortion graph exploration techniques in the Bitcoin network. In: Proc. IEEE Int. Conf. Data Min. Work. (ICDM) Work., Singapore, pp. 244–251 (2018)
19. 19.Oggier, F., Datta, A., Phetsouvanh, S.: An ego network analysis of sextortionists. Soc. Netw. Anal. Min. **10**(1), 44 (2020)[Crossref](https://doi.org/10.1007/s13278-020-00650-x)
20. 20\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr20"></a>Tironsakkul, T., Maarek, M., Eross, A., Just, M.: Probing the mystery of cryptocurrency theft: an investigation into methods for cryptocurrency tainting analysis. CoRR, abs/1906.05754 (2019)
21. 21\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr21"></a>Möser, M., Böhme, R., Breuker, D.: Towards risk scoring of Bitcoin transactions. In: Proc. Financ. Cryptogr. Data Secur. - FC 2014 Work., Barbados, pp. 16–32 (2014)
22. 22\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr22"></a>SlowMist: Crypto compliance series what is peel chain. [https://slowmist.medium.com/crypto-compliance-series-what-is-peel-chain-7b5be0bb7214](https://slowmist.medium.com/crypto-compliance-series-what-is-peel-chain-7b5be0bb7214) (2022)
23. 23\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr23"></a>Elliptic: Money laundering through dexs and mixers. [https://www.elliptic.co/blog/money-laundering-through-dexs-and-mixers](https://www.elliptic.co/blog/money-laundering-through-dexs-and-mixers) (2022)
24. 24\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr24"></a>Wu, Z., Liu, J., Wu, J., Zheng, Z., Luo, X., Chen, T.: Know your transactions: real-time and generic transaction semantic representation on blockchain & web3 ecosystem. In: Proc. Web Conf. (WWW), Austin (2023)
25. 25\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr25"></a>Andersen, R., Chung, F., Lang, K.: Local graph partitioning using pagerank vectors. In: Proc. 47th Annu. IEEE Symp. Found. Comput. Sci. (FOCS), Berkeley, pp. 475–486 (2006)
26. 26\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr26"></a>Team, P.: Bring the world to Ethereum, polygon (2019, Dec.). \[Online]. Available: [https://polygon.technology/](https://polygon.technology/)
27. 27\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr27"></a>Raghavan, U.N., Albert, R., Kumara, S.: Near linear time algorithm to detect community structures in large-scale networks. Phys. Rev. E **76**(3), 036106 (2007)[Crossref](https://doi.org/10.1103/PhysRevE.76.036106)
28. 28\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr28"></a>Blondel, V.D., Guillaume, J.-L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. J. Stat. Mech. Theory Exp. **2008**(10), P10008 (2008)[Crossref](https://doi.org/10.1088/1742-5468/2008/10/P10008)
29. 29\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr29"></a>Béres, F., Seres, I.A., Benczúr, A.A., Quintyne-Collins, M.: Blockchain is watching you: profiling and deanonymizing Ethereum users. In: Proc. IEEE Int. Conf. Decentralized Appl. Infrastructures (DAPPS), Online Event, pp. 69–78 (2021)
30. 30\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr30"></a>Dong, Y., Chawla, N.V., Swami, A.: Metapath2vec: scalable representation learning for heterogeneous networks. In: Proc. 23rd ACM SIGKDD Int. Conf. Knowl. Discov. data Min., Halifax, pp. 135–144 (2017)
31. 31\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr31"></a>Sun, H., Ruan, N., Liu, H.: Ethereum analysis via node clustering. In: Proc. 13th Int. Conf. Netw. Syst. Secur., Sapporo, pp. 114–129 (2019)
32. 32\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr32"></a>Bastian, M., Heymann, S., Jacomy, M.: Gephi: an open source software for exploring and manipulating networks. In: Proc. Third Int. Conf. Weblogs Soc. Media, San Jose, pp. 361–362 (2009)
33. 33\.<a id="oebps-html-619883_1_en_8_chapter-xhtml-cr33"></a>Page, L., Brin, S., Motwani, R., Winograd, T.: The pagerank citation ranking: bringing order to the web. Stanford InfoLab, Tech. Rep. (1999)

**Footnotes**

[1](#oebps-html-619883_1_en_8_chapter-xhtml-fn1_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn1"></a>

[https://github.com/wuzhy1ng/BlockchainSpider](https://github.com/wuzhy1ng/BlockchainSpider).

[2](#oebps-html-619883_1_en_8_chapter-xhtml-fn2_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn2"></a>

[https://www.certik.com/](https://www.certik.com/).

[3](#oebps-html-619883_1_en_8_chapter-xhtml-fn3_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn3"></a>

[https://peckshield.com/](https://peckshield.com/).

[4](#oebps-html-619883_1_en_8_chapter-xhtml-fn4_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn4"></a>

[https://www.chainalysis.com/](https://www.chainalysis.com/).

[5](#oebps-html-619883_1_en_8_chapter-xhtml-fn5_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn5"></a>

[https://blockscan.com](https://blockscan.com).

[6](#oebps-html-619883_1_en_8_chapter-xhtml-fn6_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn6"></a>

[https://trace.coinholmes.com](https://trace.coinholmes.com).

[7](#oebps-html-619883_1_en_8_chapter-xhtml-fn7_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn7"></a>

[https://etherscan.io/address/0xd4e79226f1e5a7a28abb58f4704e53cd364e8d11](https://etherscan.io/address/0xd4e79226f1e5a7a28abb58f4704e53cd364e8d11).

[8](#oebps-html-619883_1_en_8_chapter-xhtml-fn8_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn8"></a>

[https://etherscan.io/address/0xf5bec430576ff1b82e44ddb5a1c93f6f9d0884f3](https://etherscan.io/address/0xf5bec430576ff1b82e44ddb5a1c93f6f9d0884f3).

[9](#oebps-html-619883_1_en_8_chapter-xhtml-fn9_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn9"></a>

[https://etherscan.io/address/0xeb31973e0febf3e3d7058234a5ebbae1ab4b8c23](https://etherscan.io/address/0xeb31973e0febf3e3d7058234a5ebbae1ab4b8c23).

[10](#oebps-html-619883_1_en_8_chapter-xhtml-fn10_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn10"></a>

[https://coinyuppie.com/uncovering-tornado-cashs-anonymity/](https://coinyuppie.com/uncovering-tornado-cashs-anonymity/).

[11](#oebps-html-619883_1_en_8_chapter-xhtml-fn11_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn11"></a>

[https://bridge.roninchain.com/](https://bridge.roninchain.com/).

[12](#oebps-html-619883_1_en_8_chapter-xhtml-fn12_source)<a id="oebps-html-619883_1_en_8_chapter-xhtml-fn12"></a>

[https://cryptoshrypto.com/certik-explains-the-strategy-of-ronin-hacker/](https://cryptoshrypto.com/certik-explains-the-strategy-of-ronin-hacker/).
