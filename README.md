FastApps
========



**Proof of concept** of an hypermedia-driven mobile application platform.


Main Components
---------------

### Scraper ###

Responsibilities

 - Take outside-world sources of information, either structured (like data feeds or web services) or unstructured (HTML websites), turn them into normalized aggregated structured data based on pre-established ontologies.
 - Periodically traverse data source(s) for new data discovery and updating/syncing.

Artifacts

 - Spiders
  - Namely "Scrapy spiders": https://doc.scrapy.org/en/latest/topics/spiders.html


Technologies

 - scrapy (Python)
 - ArangoDB


### App Generator ###

Responsibilities:

 - For each supported platform (Android, iOS, web):.
   - Take a declarative description of end-user applications and for each of them:
     - Create and maintain base application code and assets.
     - Manage build and deploy lifecycle
     - Manage and store application secrets (code signig keys, passwords, API Keys)

Artifacts:
 
 - App descriptors
  - YAML data structures that define individual Mobile Applications
 - CLI
  - Command line interface to manage  

Technologies

 - Swift and Cocoa Touch (iOS)
 - Java and Android SDK (Android)
 - HTML/Javascript (Hybrid)
 - Cordova-lib (app automation and assets generation)
 - YAML (configuration and descriptors)


### API ###

Responsibilities

 - Take declarative descriptions of configuration and content data and its potential interactions, turn them into live API endpoints and client libraries.
 - Provide runtime access to content and configuration data to end-user application instances clients through a truly HATEOAS RESTFull interface.
 - Webhooks registration and invocation (i.e. for push notifications)
 
Artifacts:
 
 - Views
  - Views are reusable pieces of device-specific code that aim to represent a given data structure and its possible interactions to the User. Applications choose at runtime which Views to use based on the data types returned by the API.  (i.e. NewsArticleView, VideoObjectView).
 - Theme
  - Reusable piece of device-specific code that aims to 


Technologies:

 - NodeJS
 - Swagger Codegen
 - Apache Solr


### General Technologies ###

 - Vagrant during development to replicate execution environment of all components
 - Ansible for configuration management, component orchestration and deployment automation
 

 ### General Artifacts ###

Ontology:
 - Schema.org: http://schema.org/
 - rNews: http://dev.iptc.org/rNews-1-The-NewsItem-Class

