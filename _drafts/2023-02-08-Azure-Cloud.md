---
layout: page
title: "Azure Cloud Concepts"
date: 2023-08-02
tags: Azure
key: "AZ0208" 
comment: true
mathjax: true
---  


## Cloud Fundamentals

* Cloud : Connect to computing services over internet
* Computing services: Common IT infrastructure such as virtual machines, storage, databases, and networking
* Types:
    * <b> Private </b> : You own and maintain your datacenter and make it available to your organization. People in your organization or whoever you granted access are able to acess or avail services. It is costly to setup the required infrastructure like hardware, electricity, cooling, physical space, physical security...
    * <b> Public </b> : A public cloud is built, controlled, and maintained by a third-party cloud provider. With a public cloud, anyone that wants to purchase cloud services can access and use resources. The general public availability is a key difference between public and private clouds. <b> Pay for what you use </b>. <b> Scale up or scale down resources easily based the traffic </b>
    * <b> Hybrid </b>:  A hybrid cloud environment can be used to allow a private cloud to surge for increased, temporary demand by deploying public cloud resources. Hybrid cloud can be used to provide an extra layer of security. For example, users can flexibly choose which services to keep in public cloud and which to deploy to their private cloud infrastructure
    * <b> Multi-cloud </b>: Use multiple public cloud providers. Use different features from different cloud providers.

* Shared Responsibility: 
    * We have various resources to maintain like hardwares, uninterupted electricity, cooling, updating patches, data of various kind, acessing security (who have access to what) and so on
    * If we opt for a cloud service who will responsible for what?
    * One should be clear about that before opting for the serivce 
    * If you’re using a cloud SQL database, the cloud provider would be responsible for maintaining the actual database.    However, you’re still responsible for the data that gets ingested into the database.
    * If you **deployed a virtual machine and installed an SQL database** on it, you’d be responsible for database patches and updates, as well as maintaining the data and information stored in the database.
    * With an **on-premises datacenter**, you’re responsible for everything.
* Type of Services:
    * IaaS (Infrastructure as a Service)
    * PaaS (Platform as a Service)
    * SaaS (Software as a Service)

<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1C5SoDmMFDOQWQiNeES679FEWC4Sq8qUJ" width="500px" height="500px">
</p>

* You’ll always be responsible for:

    * The information and data stored in the cloud
    * Devices that are allowed to connect to your cloud (cell phones, computers, and so on)
    * The accounts and identities of the people, services, and devices within your organization
* The cloud provider is always responsible for:

    * The physical datacenter
    * The physical network
    * The physical hosts
* Your service model will determine responsibility for things like:

    * Operating systems
    * Network controls
    * Applications
    * Identity and infrastructure
* Azure Arc: Set of technologies that helps manage your cloud environment (be it public or private)
* Azure VMware: Solution lets you run your VMware workloads in Azure with seamless integration and scalability.
* Consumption Model: All cloud services will come under **Operational Expenditure** of a company not on a capital expenditure.
*  "pay as you go" model help you **plan operational costs, run infrastrcture more efficiently, scale the business if the need changes**.
## Benefits of Cloud
* **Uptime** (or availability), ideal:24 by 7. 100% uptime is not feasible (reange: 99%, 99.5% 99.9% and 99.99% ). Reasons: Maintanance, make duplicates of entity for security reasons. A service with 99% implies that the service will not be available for 1.6 hrs a week or 7 hrs a month. Whereas A service with 99.99% implies that the service will not available just for 10 minutes a week.
* **Scale** the resourse to meet the demands as business grows. Two type: **Vertical Scaling** and **Horizontal Scaling**. Vertical scaling increases the **existing resources (More CPU or More RAM)** whereas horizontal scaling adds new resources (**addtional VMs, containers**)
* Refer to Service Level Agreements (SLAs), typicall measured in percent(%). For example, uptime 99.9%
* Each service has its own SLAs
* **Reliability**: ability of a system to recover from failures and continue to function. Decentralized design is resilient to failures
* **Predictability** : Lets you move forward with confidence. performance predictability or cost predictability
    * Performance: Predicting the resources needed to deliver a positive experience. Examples, Autoscaling, load balancing, and high availability
    * Cost : predicting or forecasting the cost of the cloud spend
* **Governance**:  Deployed resources meet corporate standards and government regulatory requirement
* **Security** : Physical, handle things like distributed denial of service (DDoS) attack
* **Management of the cloud**:  managing your cloud resources
   
    * Automatically scale resource deployment based on need.
    * Deploy resources based on a preconfigured template, removing the need for manual configuration.
    * Monitor the health of resources and automatically replace failing resources.
    * Receive automatic alerts based on configured metrics, so you’re aware of performance in real time.

* **Management in the cloud**: how you’re able to manage your cloud environment and resources

    * Through a web portal, CLI, APIs, Powershell
## Cloud Service Types

* **IaaS**:
    * most flexible category, maximum amount of control for your cloud resources
    * Cloud provider is responsible for maintaining the hardware, network connectivity (to the internet), and physical security
    * Consumer is responsible for everythin else
    * What you do with that hardware is up to you
    * **Scenarios**: **Lift-and-shift migration** (standing up cloud resources similar to your on-prem datacenter, then simply moving the things running on-prem to running on the IaaS infrastructure). **Testing and development:** Assume that you have worked out testing and development protocols, you want to test it out before establishing your own datacenter.you can stand up or shut down the different environments rapidly with an IaaS structure, while maintaining complete control.

* **PaaS**:
    * Middle ground between renting space in a datacenter (infrastructure as a service) and paying for a complete and deployed solution (software as a service)
    * Cloud provider maintains the physical infrastructure, physical security, and connection to the internet, operating systems, middleware, development tools, and business intelligence services that make up a cloud solution, licensing or patching for operating systems and databases.
    * Suited to provide a **complete development environment**
    * Use cases: Development framework (build upon to develop or customize cloud-based applications). Analytics or business intelligence.

* **SaaS**:
    * Complete cloud service model from a product perspective
    * You’re essentially renting or using a fully developed application
    * Email, financial software, messaging applications, and connectivity software are all common examples of a SaaS implementation.
    * **least** amount of technical knowledge or expertise to fully employ.
    * Use cases: Email and messaging, Business productivity applications.

## Azure Architecture and Services
* Services: 100+
* Create an Account (free) to avail services (subscriptions) with fee.
<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1AiAUdNNLIpTyDaSr1RJh2UYGNXSMeLrx" width="500px" height="500px">
</p>

* We can manage subscriptions
* We can use "Learn sandbox" for learning purpose. Always activate it while learning
* We can interact in three ways via CLI : Power Shell (default), BASH, Interactive mode.
### Azure Physical Infrastructure
* These are datacenters with hardwares, power, cooling system distributed across glob.
* We can't access indiviudal datacenters
* Grouped into Azure regions or availability zone (focusing **resilient and reliability**)
* **Region**: A geographical location with at leaset one or more datacenters (networked together with low-latency network)
* **Availability zones** : A physically separated (one more) datacenters within the Azure region. **Not all regions support Availability Zone**
* Why is it called "availability"? Because failure of one datacenter in the AZ zone does not stop the service (because the software and data are made reduntant). Therefore, these zones are prefered for mission critical applications.
* There could be a cost to duplicating your services and transferring data between availability zones.
* **Resources** that need AZ: VMs, SQL database, managed disks, load balancers
* Categories :
    * Zonal: pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
    * Zone-Redundant: platform replicates automatically across zone
    * Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.
* Region pairs:
    * Most Azure regions are paired with another region within the same geography (such as US, Europe, or Asia) at least **300 miles** away.
    * This approach allows for the **replication of resources** across a geography that helps reduce the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect an entire region

    <p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1REQv5qH7OhHzrrHL1SXTCRoF5OBTlptL" width="500px" height="500px">
    </p> 

    * Pair could be unidirectional in some cases (it affects the backup)
* Sovereign Regions:
    * Sovereign regions are instances of Azure that are isolated from the main instance of Azure. You may need to use a sovereign region for compliance or legal purposes.
    * US, China have sovereign regions where Azure do not directly maintain datacenters but through a partnership.
### Management Infrastrcture.
* Resources and Resource Groups:
    * Resource is a basic building block
    * Anything you create, provision, deploy, etc. is a resource
    * Virtual Machines (VMs), virtual networks, databases, cognitive services, etc. are all considered resources within Azure.
    * **Resource groups** are simply groupings of resources.
    * A single resource can **only be in one resource group** at a time
    * Resource group can not be nested.
    * When you apply an action to a resource group, that action will apply to all the resources within the resource group
    *  If you’re setting up a **temporary dev environment**, grouping all the resources together means you can deprovision all of the associated resources at once by deleting the resource group.
    * set up your resource groups **to maximize** their usefulness for you.
* Azure subscriptions:
    * A unit of management, billing, and scale
    * Logically organize your resource groups and facilitate billing
    * Subscription provides you with authenticated and authorized access to Azure products and services.
    * All provisions are maintained in Azure Active Directory (AD)
    * Two types of boundary one can set on the services availed via subscriptions: Billing boundary, Access Control boundary
* Management Group
    * Resources are gathered into resource groups, and resource groups are gathered into subscriptions
    * Useful, if you’re dealing with multiple applications, multiple development teams, in multiple geographies.
    * If you have many subscriptions, you might need a way to efficiently manage access, policies, and compliance for those subscriptions. Azure management groups provide a level of scope above subscriptions. You organize subscriptions into containers called management groups and apply governance conditions to the management groups. All subscriptions within a management group automatically inherit the conditions applied to the management group, the same way that resource groups inherit settings from subscriptions and resources inherit from resource groups. Management groups give you enterprise-grade management at a large scale, no matter what type of subscriptions you might have. Management groups can be nested.
    
    <p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=1XxnAvyfnOmSjKBDsQDQO5uHUxY3EdsUy" width="500px" height="300px">
    </p> 

    * **10,000 management groups** can be supported in a single directory.
    * A management group tree can support up to six levels of depth.
    * Each management group and subscription can support only one parent.

### Compute and Networking Services
* Compute options: Virtual Machines, Containers, Functions.
* Networking : Virtual Networks, DNS, Express route
* Virtual Machines (VMs):
    * Its a IaaS
    * Have total control on OS
    * Run Custome softwares, custom hosting
    * Need to update patches, softwares regularly on owr own (this might affect services)
    * use an **already created image** to rapidly provision VM
    * What is an image then? An image is a **template** used to create a VM and may already include an OS and other software, like development tools or web hosting environments
    * We can run a single VM (for development and test) or group of VM for scalability
    * **Scale sets**: create and manage a group of identical, load-balanced VMs
    * With Virtual machine scale sets, you can build large-scale services for areas such as compute, big data, and container workloads.
    * **Availability sets**: for more resilient, highly available environment. Uses two approaches to connect with datacenters within available zone: **Update domain** and **fault domain**
    * **Update domain**: Groups VMs that can be rebooted at the same time
    * **Fault domain** : Groups VMs common power source and network switch
    * no additional cost for configuring an availability set. You only pay for the VM instances you create
    * **Use Cases**: Dev and test on different OS, running application in the cloud, extending the datacenter to cloud,during disaster recovery.
    * **VM Resources**: Size (purpose, number of cores, amount of RAM), Storage Disks (hard disk, ssd..), Networking (virtual network, public IP address, and port configuration)
    * How to move the existing on-premises VM to cloud? Make an image of the on-premises datacenter and move it to cloud VM.
    * To create a VM, use *az vm create --specs* as follows
    * To create extension set use *az vm extension set --specs*. For example, we can configure Nginx ("engine-x) web server using this command.
    * Azure **Virtual Desktop** is another option
    * Azure Virtual Desktop also provides a more consistent experience with broader application support compared to Windows Server-based operating systems.

### Containers
* VMs are limited to a single operating system per virtual machine
* To run **multiple instances of an application** on a single host machine, containers are an excellent choice.
* What are containers?
    * Containers are a virtualization environment. Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host. Unlike virtual machines, **you don't manage the operating system** for a container. Virtual machines appear to be an instance of an operating system that you can connect to and manage. Containers are **lightweight and designed to be created, scaled out, and stopped dynamically**. It's possible to create and deploy virtual machines as application demand increases, but containers are a **lighter weight, more agile method**. Containers are designed to allow you to respond to changes on demand. With containers, you can quickly restart if there's a crash or hardware interruption. One of the most popular container engines is **Docker**, which is supported by Azure.
* VMs virtualize hardware, the containers virtualize the OS
* Containers are offered as **PaaS** in Azure
* **Use cases:** Containers are often used to create solutions by using a microservice architecture. This architecture is where you break solutions into smaller, independent pieces. For example, you might split a website into a container hosting your front end, another hosting your back end, and a third for storage. This split allows you to separate portions of your app into logical sections that can be maintained, scaled, or updated independently.

Imagine your website back-end has reached capacity but the front end and storage aren't being stressed. With containers, you could scale the back end separately to improve performance. If something necessitated such a change, you could also choose to change the storage service or modify the front end without impacting any of the other components.

### Azure Functions:
* Event-driven, **serverless compute** (though the name is misleading) option that **doesn’t require** maintaining virtual machines or containers
* With Azure Functions, an event wakes the function, alleviating the need to keep resources provisioned when there are no events.
* Azure Functions is ideal when you're only concerned **about the code running your service** and not about the underlying platform or infrastructure
* Functions are commonly used when you need to perform work in response to an event (often via a REST request), timer
* Azure Functions runs your code when it's triggered and automatically deallocates resources when the function is finished.
* Two types: Stateless (default), stateful

### Application Hosting

 * We can use VMs or Containers for hosting an application in Azure.
 * **Azure App**: build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructur
 * Supports continuous deployment model.
 * Type of apps: Web apps, mobile apps, API apps,WebJobs

 ### Virtual Networking
 * virtual subnets enable Azure resources, such as VMs, web apps, and databases, to communicate with each other, with users on the internet, and with your on-premises client computers
 * Azure virtual networks provide the following key networking capabilities:

    * Isolation and segmentation
    * Internet communications
    * Communicate between Azure resources
    * Communicate with on-premises resources
    * Route network traffic
    * Filter network traffic
    * Connect virtual networks
* Peering: Allows connection two virtual networks directly connect to each other
* **Important**: Network traffic between peered networks is private, and travels on the Microsoft backbone network, never entering the public internet

### Virtual Private Networks (VPNs)
* VPNs are typically deployed to connect two or more trusted private networks to one another over an untrusted network (typically the public internet)
* Azure VPN Gateway instances are deployed in a dedicated subnet of the virtual network

### Azure ExpressRoute
* Azure ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection, with the help of a connectivity provider
* ExpressRoute connections **don't go over the public Internet**.
* ExpressRoute enables direct access to the following services in all regions:

    * Microsoft Office 365
    * Microsoft Dynamics 365
    * Azure compute services, such as Azure Virtual Machines
    * Azure cloud services, such as Azure Cosmos DB and Azure Storage

### Azure DNS
* A hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure
* You can't use Azure DNS to buy a domain name

## Azure Storage Accounts
* Types: Blob storage (like Data lake storage), Queue storage, table,Azure Files..
* Storage accounts provide a unique namespace
* Store data and access it from anywhere using HTTP or HTTPS 
* Data is secure, highly available, durable, scalable
* There are different types of storage accounts: Locally redundant Storage (LRS), Geo Redundant Storage (GRS),..
* You can choose the one based on the use cases, [Read more](!https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/2-accounts) 
* Having a unique namespace in Azure for your data
* storage account in Azure **must have** a unique-in-Azure account name
* The combination of the account name and the Azure Storage service endpoint forms the endpoints for your storage account.

### Redundancy
* Data in an Azure Storage account is always **replicated three times** in the primary region.
* You can either choose Locally Redundant Storage (LRS)  or Zone-Redundant Storage (ZRS)
* LRS replicates the data in the storage account of the primary regions, Provides 11 nines of durability (99.9999999%).     LRS protects your data against server rack and drive failures. However, if a disaster such as fire or flooding occurs within the data center, all replicas of a storage account using LRS may be lost or unrecoverable
* ZRS replicates data in three different zones and provides 12 nines of durability. 
* ZRS in the primary region is recommended for scenarios that require high availability
* The durability increases to 16 nines if we opt for GRS (of course, with increased cost)

### Storage Services
* **Azure Blobs:** A massively scalable object store for text and binary data. Also includes support for big data analytics through Data Lake Storage Gen2. 
    * Azure Blob Storage is unstructured, meaning that there are no restrictions on the kinds of data it can hold. 
    * Blob Storage can manage thousands of simultaneous uploads, massive amounts of video data, constantly growing log files, and can be reached from anywhere with an internet connection.
    * A blob could contain gigabytes of binary data streamed from a scientific instrument, an encrypted message for another application, or data in a custom format for an app you're developing
    * **Blob storage is ideal for:**
        * Serving images or documents directly to a browser.
        * Storing files for distributed access.
        * Streaming video and audio.
        * Storing data for backup and restore, disaster recovery, and archiving.
        * Storing data for analysis by an on-premises or Azure-hosted service.
* **Access tiers:**
    * Hot access tier: Optimized for storing data that is accessed frequently (for example, images for your website).
    * Cool access tier: Optimized for data that is infrequently accessed and stored for at least 30 days (for example, invoices for your customers).
    * Archive access tier: Appropriate for data that is rarely accessed and stored for at least 180 days, with flexible latency requirements (for example, long-term backups).
* **Azure Files:** Managed file shares for cloud or on-premises deployments.
* **Azure Queues:** A messaging store for reliable messaging between application components. Queue storage can be combined with compute functions like Azure Functions to take an action when a message is received.
* **Azure Disks:** Block-level storage volumes for Azure VMs.
* What does it mean by "managed"? Azure handles hardware maintenance, updates, and critical issues for you.

### Azure Data Migration
* Migration of **infrastructure**, applications, and data using Azure Migrate as well as asynchronous migration of data using Azure Data Box
* Azure Migrate: helps you migrate from an on-premises environment to the cloud
* Azure migrate and Data box are suitable for moving a large data size (say > 40 TB)
* AzCopy : For small files. Move data between storage accounts.
* Azure File Sync: Allow shared files in both on-premises and cloud

## Identity, Access and Security (IAS)
* A set of Authorization and authentication methods 
### Azure Active Directory (AD)
* Directory service that enables you to sign in and access both Microsoft cloud applications and cloud applications that you develop
* **Who use it?**: IT administrators, App developers, Users (say, for password reset), Microsoft 365, Microsoft Office 365, Azure, and Microsoft Dynamics CRM Online subscribers are already using Azure AD to authenticate into their account.
* **FUnctions**: Authentication,Single sign-on,Application management,Device management
* **Authentication Methods**: standard passwords, single sign-on (SSO), multifactor authentication (MFA), and passwordless. Microsfot authenticator App is one such example for MFA
* **Azure external identities**: For, B2B colloboration, B2C (Business to Customer), B2B direct connect.
* **Azure Conditional Acess**: Provides a more granular multifactor authentication experience for users. For example, a user might not be challenged for second authentication factor if they're at a known location. However, they might be challenged for a second authentication factor if their sign-in signals are unusual or they're at an unexpected location. 
* **Role Based Access Control (RBAC)**: provides built-in roles that describe common access rules for cloud resources. You can also define your own roles. Each role has an associated set of access permissions that relate to that role. When you assign individuals or groups to one or more roles, they receive all the associated access permissions.
* So, if you hire a new engineer and add them to the Azure RBAC group for engineers, they automatically get the same access as the other engineers in the same Azure RBAC group. Similarly, if you add additional resources and point Azure RBAC at them, everyone in that Azure RBAC group will now have those permissions on the new resources as well as the existing resources.
* Azure RBAC is **hierarchical**, in that when you grant access at a parent scope, those permissions are inherited by all child scopes.
* Azure RBAC doesn't enforce access permissions at the application or data level.
* **Zero Trust Model** : Zero Trust is a security model that assumes the worst case scenario and protects resources with that expectation.
* **Defence-in-Depth**: The objective of defense-in-depth is to protect information and prevent it from being stolen by those who aren't authorized to access it.
<p align="center">
 <img align="center" src="https://drive.google.com/uc?export=view&id=135WNs4g9EaY9rCLWFFGsmO7loGiuRlkJ" width="500px" height="300px">
    </p> 