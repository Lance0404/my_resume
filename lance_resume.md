# Lance Chang 

- [virtuouslycan@gmail.com](virtuouslycan@gmail.com) 
- Github: [Lance0404](https://github.com/Lance0404)
- +886 963257206 
- Line ID: lycanlance 

---
### Profile 
#### Abstract 
Career started as a Bioinformatic technician, un-puzzling genome level sequencing projects. As my programming skill accumulates and interest broadens, I switched my career path to the software industry. I mainly develop backend applications with Python, but also have experience in Kotlin, Java, Node.js and Rust. I am a backend developer, data engineer and devops engineer. 

#### Summary 
- Experience in web application back-end development, either monolith or microservice, with multiple different languages and databases, and deployed to multiple different cloud environments. 
- Experience in microservice development with AWS Lambda Functions written in Python or Node.js.
- Experience in CI/CD coordinated by Jenkins (or AWS Codebuild), under containerized environments and deployed to AWS with Cloudformation template.
- By carrying out the Agile/Scrum practice, I can work cooperatively within a self-organized team under a foreign environment and delivery done increments on a sprintly basis. 
- Without an academic CS background, I became a competent software developer with the attitude of constantly chasing new tech. 
Experience 
---
### Experience
Cameo Inc.
: *Senior Software Developer (contractor)*
__Nov 2021 - Now__

- Joined a team that maintains an IoT data center that collects air, water and noise data from nation-wide devices. Continuously refactored the code base and developed new features on top.
- Developed public-facing RESTful APIs with Python FastAPI framework and Celery asynchronous framework, and deployed as Nginx-Gunicorn-FastAPI form with docker-compose.
- Configured multiple Nginx web servers for redirection and load balancing, along with certificate auto renewal.
- Developed continuous delivery workflow for deploying services on premise machines. 
- Developed Kafka consumer-producer process with Python aiokafka package that does ETL on messages between topics on the fly, and capable of consuming on specific time range which is useful for recovering data from the past. 


FST Network
: *Senior Software Developer*
__June 2021 - August 2021__
- Joined a team that develops a data mesh software with Rust which was orchestrated with kubernetes.
- Developed a FTP client feature with async_ftp crate .
- Developed RESTful APIs that get data from Postgresql with sqlx crate.
- Developed gRPC APIs that communicate between microservices with the tonic crate.


Wistron ITS
: *Senior DevOps Engineer (Contractor of Bioclinica, a US company provides clinical imaging solution)*
__Nov 2020 - May 2021__
- Continuously optimizing the CICD process of two Npm-managed Javascript web applications. 
- Maintained CICD processes that mainly covers build, test, publish, git tagging and deployment to AWS. 
- By using AWS Codebuild with docker images as concurrent Jenkins slaves, Jenkins jobs are scalable. 
- Refactored Jenkins jobs by moving the tedious web-based configuration into Jenkinsfile, so-called pipeline as code, eventually leads to reduced maintenance cost. 
- Chained up multiple Jenkins jobs into one single job so as to have the process fully automated without human intervention. 
Parameterized all the options for that multitasked Jenkins job so the user can easily operate certain desired stages through toggles from the web UI. 
- Made use of parallel stages in Jenkinsfile so stages without dependency can run in parallel to reduce the overall CI execution time. 
- Resolved issues related to deploying AWS cloudformation stacks in different regions. 

Ampos Solution Inc. 
: *Backend developer*
__May 2019 - Aug 2020__
- Work as a developer within a Project Team of the company, which takes on customized requirements from the customer, but also rotates to Product Teams if they fall short of resources.
- Develop the backend part of an ERM (Employee Resource Management) system, which contains both monolithic and microservice parts and deployed on AWS cloud as ECS. 
- Develop monolithic server with Spring Boot, Java and Kotlin, with unit tests and integration tests covered. 
- Develop microservice with AWS Lambda, usually written in Python or Node.js, or ECS written in Kotlin with Spring Boot framework. 
- Integrate the functionality of an external server, Matter Most, to implement a chat channel function for our mobile app. 
- Provide performant backend APIs with cache design for both mobile and web client use. 
- Deploy a CodeBuild project for every new service, which webhooks to its VCS and operates CI and optionally deploys to the environment of desire. 
- For every deployable project, write AWS CloudFormation template.yml for both its CodeBuild and its own stack to achieve IaC (Infrastructure as Code). 
- Use AWS CodeBuild or Jenkins to implement CI/CD for every deployable project. 
- Build on top of several AWS services like S3, Glue, AthenaQuery, Elastic Beanstalk, ECS, ECR, Lambda, ElasticSearch, RDS, DynamoDB, CodeBuild, CloudFormation, CloudWatch, SNS and SQS. 

Breaktime Inc.
: *Backend developer/Data engineer*
__Mar 2018 - May 2019__
- Enhanced the collection, reformatting and storage of user behavior data by replacing the message queue Redis (in RAM) with Kafka (in Disk), so spikely lower the cost and maintenance effort. 
- Optimized the dataflow from Redis to Kafka and from Kafka to Hbase (Hadoop). 
- Use Spark to consume streaming data from Kafka and output the aggregated data as parquet file format. 
- Fine-tuned Hbase rowkey design for bettering the data analyst’s daily usage. 
- Refactored a web crawler REST api, covering more than 1000 domains. With spec given, it crawls through >100,000 web pages per hour. 
- Automate the crawling process with the domain-specific xpath settings and regex so it can be fine parsed and stored into PostgreSQL . 
- Customize the crawl on JS-generated pages with the use of Selenium. 
- Developed an event-driven and scalable web application with the use of Nginx, uWSGI/Gunicorn, Flask, Celery*, Docker and Supervisor. 
- Familiar with the deployment of docker images with GCE on GCP (Google Cloud Platform) and monitoring them with StackDriver. 
- Familiar with deploying microservices as pods with GKE (kubernetes) on GCP by customizing the YAML file. 
- Automating the sales’ requirements by searching through a list of keywords against Elasticsearch DB and generating a csv format file with python script.

Hgiga Inc.
: *Full-stack developer*
__Nov 2016 - Feb 2018__
- Maintenance of an MTA (Mail Transfer Agent) software including debugging, function enhancement and customized requirements. 
- Assisting the customer service team for instant case solving during office hours. 
- Version control with CVS. 
- Pack the software into rpm according to the customized spec file. 
- Deliver the updated install package through rpm server. 
- Front-end maintenance with JavaScript, JQuery, Bootstrap et al. 
- Backend maintenance with Perl, PHP, MySQL. 
- Developed a full text search function through all the emails with the incorporation of Elasticsearch. 
- Developed all kinds of customized HR data importing functions, since each customer may have different HR db schema. 
- Developed a PDF signature function for those emails having PDF as attachment. 


Genomics
: *Bioinformatic technician*
__Jun 2014 - Oct 2016__
- _de novo_ transcriptome (w/ or w/o reference) 
- RNS-reseq (w/ reference) 
- genome de novo assembly, gene prediction, annotation (illumina data) - genome de novo assembly, gene prediction, annotation (pacbio data) 
- amplicon variant call, variant annotation 
- WES (whole exome sequencing)/WGS (whole genome sequencing) 

Academia Sinica
: *Research assistant*
__Oct 2012 - Dec 2013__

- Publication
    - Chang TH, Lo WS, Ku C, Chen LL, Kuo CH. Molecular evolution of the substrate utilization strategies and putative virulence factors in mosquito-associated Spiroplasma species. Genome Biol Evol. 2014 Mar;6(3):500-9. doi: 10.1093/gbe/evu033. 
    - Lo WS, Ku C, Chen LL, Chang TH, Kuo CH. Comparison of metabolic capacities and inference of gene content evolution in mosquito-associated Spiroplasma diminutum and S. taiwanense. Genome Biol Evol. 2013;5(8):1512-23. doi: 10.1093/gbe/evt108.

---
### Education 
- National Taiwan University, Taiwan, Taipei, Jul 2010 - Oct 2012 
Master’s degree - Plant Pathology and Microbiology 
- Publication
    - Liu LY, Tseng HI, Lin CP, Lin YY, Huang YH, Huang CK, Chang TH, Lin SS. High-Throughput Transcriptome Analysis of the Leafy Flower Transition of Catharanthus roseus Induced by Peanut Witches'-Broom Phytoplasma Infection. Plant Cell Physiol. 2014 May;55(5):942-57. doi: 10.1093/pcp/pcu029. Epub 2014 Feb 2. 

- National Chung Hsing University, Taiwan, Taichung, Sep 2003 - Jun 2007 Bachelor's degree - Entomology 

---
### Skills 

- Languages 
    - Python, Rust, Java/Kotlin, Node.js, Javascript, Go 
    - Bash, Perl5, PHP, R, HTML 
- Web frameworks and related tools 
    - Python 
        - FastAPI(starlette), Flask(uWSGI, Gunicorn), Django, Celery(async design), Sqlalchemy(SQL ORM)
    - Java/Kotlin 
        - Tomcat, Spring-boot, Hystrix, Liquibase, Security, JPA, Swagger, Junit, Mockito, Gradle, Maven 
- Web server: Nginx 
- Database 
    - (sql) PostgreSQL, MySQL, AWS RDS 
    - (nosql) AWS DynamoDB, MongoDB 
    - ElasticSearch 
    - Hbase 
    - Kafka 
    - Redis, Memcached 
- Big Data 
    - Spark, Duckdb, Pandas, AWS Glue/Athena 
- Cloud Services 
    - AWS 
        - S3, SNS, SQS, ECR, ECS, CloudFormation, CodeBuild, CloudWatch, API Gateway, IAM, VPC, Route53 
- GCP 
    - GCE, GKE, StackDriver 
- Version Control System 
    - Git, Github, Bitbucket, Gitlab
- IDE: 
    - VSCode, IntelliJ, PyCharm 
- Container
    - Docker, Docker-compose, Kubernetes	
- DevOps 
    - CodeBuild, Jenkins, AWS cli
- OS 
    -  Window (WSL2), Linux, MacOS
- Protocol 
    - REST, GraphQL, gRPC, HTTP(S), SMTP, FTP(S) 
- Others 
    - Postman 
    - Jira, Confluence, Trello 
- Programming certificate: 
    - Kafka certificate (hand out by TDEA, Taiwan Data Engineering Association) 
- English certificate: 
    - GRE (1330), TOEFL iBT (103), TOEIC (885), TOEFL ITP (613), GEPT mid-high level passed.
