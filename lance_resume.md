# Lance Chang
## Senior Software Engineer

- <virtuouslycan@gmail.com>
- Github: [Lance0404](https://github.com/Lance0404)
- +886 963257206
- Line ID: lycanlance

---

## Profile
Started as a _Bioinformatics Technician_ analyzing genome-scale sequencing data, then moved into software engineering. Builds web applications and middleware in both compiled (Java/Kotlin/Scala/Rust/C++) and interpreted (Python/Node.js) languages, across SQL and NoSQL databases. Primarily a _backend developer_, with additional experience as a _data engineer_ and _DevOps engineer_.

---

## Highlights
- Backend development across monolithic and microservice architectures, multiple languages/databases, deployed on AWS and GCP.
- Serverless microservice development with AWS Lambda.
- CI/CD pipelines built with Jenkins and AWS CodeBuild, containerized and deployed to AWS via CloudFormation.
- Delivers sprint increments in Agile/Scrum teams, comfortable working in cross-border, cross-functional environments.

---

## Experience

### Foxconn Software R&D Center (SRDC)
* **Senior Software Engineer** _Jan. 2025 - Now_
    - Delivering AUTOSAR Adaptive Platform (AP) middleware in C++ for IVI (In-Vehicle Infotainment) and T-BOX ECUs, covering the full AP development cycle: requirement analysis, architecture design, implementation, integration, and validation.
    - Delivered core AP functional clusters, each split per VLAN for isolation:
        - **TSync** - time synchronization across ECUs, including Sync/FUp/pDelay message monitoring
        - **SOME/IP** - service-oriented middleware communication (service discovery, pub/sub, RPC), with packet-level monitoring during development to verify protocol behavior
        - **IdsM** - Intrusion Detection System Manager for security event reporting
        - **Diag** - UDS-based diagnostic services
        - **SOVD** - Service-Oriented Vehicle Diagnostics, the HTTP/REST-based next-gen diagnostic interface
        - **LogD** - logging service supporting both streaming DLT output and DLT file output
    - Coordinated heavily across departments since hardware and firmware are supplied by other business units, working closely with those teams to align interface specs, resolve integration issues, and validate middleware against externally provided hardware and firmware.
    - Also contributing to an AI agent (STT & TTS) initiative for internal corporate use cases.

### Constant Contact
* **Senior Software Engineer** _Apr. 2022 - Dec. 2024_
    - Maintained and extended systems inherited from Retention Science (acquired 2020) - backend applications storing customer data and running business logic at scale.
    - Refactored legacy code and built new features on top of it.
    - Carried on-call rotation for systems under the team's ownership.
    - Led database upgrades, e.g. MySQL 5.6 to 5.7, Elasticsearch 6 to 1.3.
    - Frequently used: Scala, SBT, Cadence, Python, serverless, AWS ECS/Lambda/OpenSearch/Aurora MySQL/S3/SQS/SNS/Kinesis/Athena.

### Cameo Inc.
* **Senior Software Developer (contractor)** _Nov. 2021 - Apr. 2022_
    - Maintained and extended an IoT data center collecting air, water, and noise data from nationwide devices.
    - Built public-facing RESTful APIs with FastAPI and Celery, deployed as Nginx-Gunicorn-FastAPI via docker-compose.
    - Configured Nginx servers for redirection, load balancing, and automated certificate renewal.
    - Built continuous delivery workflows for on-premise deployment.
    - Built a Kafka consumer-producer pipeline (aiokafka) doing on-the-fly ETL between topics, with time-range-based consumption for historical data recovery.

### FST Network
* **Senior Software Developer** _June 2021 - August 2021_
    - Joined a team building a Kubernetes-orchestrated data mesh in Rust.
    - Built an FTP client feature with the `async_ftp` crate.
    - Built RESTful APIs against PostgreSQL with the `sqlx` crate.
    - Built gRPC APIs for inter-service communication with the `tonic` crate.

### Wistron ITS
* **Senior DevOps Engineer** (Contractor of Bioclinica, a US clinical imaging solutions company) _Nov 2020 - May 2021_
    - Continuously optimized CI/CD for two npm-managed JavaScript web applications.
    - Maintained pipelines covering build, test, publish, git tagging, and deployment to AWS.
    - Scaled Jenkins with AWS CodeBuild-backed docker images as concurrent build slaves.
    - Migrated Jenkins jobs from web-based configuration to Jenkinsfile (pipeline as code), cutting maintenance cost.
    - Chained multiple Jenkins jobs into a single, fully automated pipeline with no manual intervention, exposing toggles for each stage through parameterized web UI options.
    - Parallelized independent Jenkinsfile stages to reduce overall CI runtime.
    - Resolved issues deploying AWS CloudFormation stacks across regions.

### Ampos Solution Inc.
* **Backend Developer** _May 2019 - Aug 2020_
    - Worked within a project team handling customized customer requirements, rotating into product teams as needed.
    - Built the backend of an ERM (Employee Resource Management) system - both monolithic and microservice components, deployed on AWS ECS.
    - Built a monolithic server in Spring Boot (Java/Kotlin) with unit and integration test coverage.
    - Built microservices on AWS Lambda (Python/Node.js) and ECS (Kotlin/Spring Boot).
    - Integrated Mattermost to add a chat channel feature to the mobile app.
    - Delivered performant backend APIs with caching for mobile and web clients.
    - Set up a CodeBuild project per service, webhooked to VCS, running CI and optional deployment.
    - Wrote CloudFormation templates per deployable project for both CodeBuild and its stack (IaC).
    - Implemented CI/CD with AWS CodeBuild and Jenkins across deployable projects.
    - Worked across AWS S3, Glue, Athena, Elastic Beanstalk, ECS, ECR, Lambda, Elasticsearch, RDS, DynamoDB, CodeBuild, CloudFormation, CloudWatch, SNS, and SQS.

### Breaktime Inc.
* **Backend Developer/Data Engineer** _Mar 2018 - May 2019_
    - Replaced Redis (in-RAM) with Kafka (on-disk) for user behavior data collection, cutting cost and maintenance effort.
    - Optimized the data flow from Redis to Kafka and from Kafka to HBase (Hadoop).
    - Used Spark to consume Kafka streams and output aggregated Parquet files.
    - Tuned HBase rowkey design to improve data analysts' daily workflow.
    - Refactored a web crawler REST API covering 1,000+ domains, crawling 100,000+ pages/hour per spec.
    - Automated crawling with domain-specific XPath and regex rules, parsing results into PostgreSQL.
    - Handled JS-rendered pages with Selenium.
    - Built an event-driven, scalable web app with Nginx, uWSGI/Gunicorn, Flask, Celery, Docker, and Supervisor.
    - Deployed and monitored Docker images on GCE (GCP) with StackDriver.
    - Deployed microservices as pods on GKE via custom YAML manifests.
    - Automated sales' keyword-search requirements against Elasticsearch, generating CSV output via Python scripts.

### Hgiga Inc.
* **Full-stack Developer** _Nov 2016 - Feb 2018_
    - Maintained an MTA (Mail Transfer Agent) software: debugging, feature enhancement, and customized requirements.
    - Supported customer service with instant case resolution during office hours.
    - Managed version control with CVS.
    - Packaged software into RPMs per customized spec files and delivered updates via RPM server.
    - Maintained the frontend with JavaScript, jQuery, and Bootstrap.
    - Maintained the backend with Perl, PHP, and MySQL.
    - Built full-text search across emails using Elasticsearch.
    - Built customized HR data import functions to handle varying customer HR schemas.
    - Built a PDF signature function for emails with PDF attachments.

### Genomics
* **Bioinformatic Technician** _Jun 2014 - Oct 2016_
    - _De novo_ transcriptome assembly, with and without reference.
    - RNA-seq analysis with reference.
    - _De novo_ genome assembly, gene prediction, and annotation (Illumina and PacBio data).
    - Amplicon variant calling and annotation.
    - WES (whole exome sequencing) / WGS (whole genome sequencing).

### Academia Sinica
* **Research Assistant** _Oct 2012 - Dec 2013_
    - Publications:
        - Chang TH, Lo WS, Ku C, Chen LL, Kuo CH. Molecular evolution of the substrate utilization strategies and putative virulence factors in mosquito-associated Spiroplasma species. Genome Biol Evol. 2014 Mar;6(3):500-9. doi: 10.1093/gbe/evu033.
        - Lo WS, Ku C, Chen LL, Chang TH, Kuo CH. Comparison of metabolic capacities and inference of gene content evolution in mosquito-associated Spiroplasma diminutum and S. taiwanense. Genome Biol Evol. 2013;5(8):1512-23. doi: 10.1093/gbe/evt108.

---

## Education
### National Taiwan University, Taiwan, Taipei
- Master's degree - Plant Pathology and Microbiology _Jul 2010 - Oct 2012_
- Publication:
    - Liu LY, Tseng HI, Lin CP, Lin YY, Huang YH, Huang CK, Chang TH, Lin SS. High-Throughput Transcriptome Analysis of the Leafy Flower Transition of Catharanthus roseus Induced by Peanut Witches'-Broom Phytoplasma Infection. Plant Cell Physiol. 2014 May;55(5):942-57. doi: 10.1093/pcp/pcu029. Epub 2014 Feb 2.

### National Chung Hsing University, Taiwan, Taichung
- Bachelor's degree - Entomology _Sep 2003 - Jun 2007_

---

## Skills

- Languages
    - Python, Scala, Java/Kotlin, Rust, Node.js, JavaScript, Go
    - Bash, Perl5, PHP, R, HTML
- Web frameworks and related tools
    - Python
        - FastAPI (Starlette), Flask (uWSGI, Gunicorn), Django, Celery (async design), SQLAlchemy (SQL ORM)
    - Scala
        - Play, Cadence
    - Java/Kotlin
        - Tomcat, Spring Boot, Hystrix, Liquibase, Security, JPA, Swagger, JUnit, Mockito, Gradle, Maven
- Web server: Nginx
- Database
    - PostgreSQL, MySQL, AWS RDS
    - AWS DynamoDB, MongoDB
    - Redis, Memcached
    - Kafka
    - Elasticsearch/OpenSearch
    - HBase
- Big Data
    - Spark, DuckDB, Pandas, AWS Glue/Athena
- Cloud Services
    - AWS
        - S3, SNS, SQS, ECR, ECS, CloudFormation, CodeBuild, CloudWatch, API Gateway, IAM, VPC, Route53
    - GCP
        - GCE, GKE, StackDriver
- Version Control System
    - Git, GitHub, Bitbucket, GitLab
- IDE
    - VSCode, IntelliJ, PyCharm
- Container
    - Docker, Docker Compose, Kubernetes
- DevOps
    - CodeBuild, Jenkins, AWS CLI
- OS
    - Windows (WSL2), Linux, macOS
- Protocol
    - REST, GraphQL, gRPC, HTTP(S), SMTP, FTP(S)
- Others
    - Postman, Jira, Confluence, Trello
- Programming certificate
    - Kafka certificate (issued by TDEA, Taiwan Data Engineering Association)
- English certificate
    - GRE (1330), TOEFL iBT (103), TOEIC (885), TOEFL ITP (613), GEPT mid-high level passed
