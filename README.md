<!-- Animated Minimalist Header -->
<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Space+Grotesk&weight=600&size=24&pause=1000&color=4285F4&center=true&vCenter=true&width=800&lines=System.Architecture(Sai_Varun_Degala);Building+intelligence+at+the+intersection+of+Code+and+Biology;Graph+Databases+%7C+AI+%26+ML+%7C+Global+Scale" alt="Typing SVG" />
</div>

<div align="center">
  <img src="binary_portrait.gif" alt="Varun Sai Degala" width="160" style="border-radius: 20%; box-shadow: 4px 4px 0px #4285F4;" />
  <br><br>
  <img src="https://img.shields.io/badge/Google_Gemini-Campus_Ambassador-4285F4?style=flat-square&logo=google-gemini&logoColor=white" />
  <img src="https://img.shields.io/badge/Domain-AI_%26_Biomedical-FF6F00?style=flat-square&logo=tensorflow&logoColor=white" />
</div>

<br>

### 🧠 1. The Knowledge Graph (Cypher / Neo4j)
*How my background maps together:*

```cypher
MATCH (varun:Engineer {name: 'Sai Varun Degala'})
MERGE (bio:Foundation {field: 'Biomedical Engineering'})
MERGE (ai:Specialization {field: 'Artificial Intelligence & ML'})

// The Core Trajectory
CREATE (varun)-[:EVOLVED_FROM]->(bio)
CREATE (varun)-[:ARCHITECTS_IN]->(ai)

// The Projects
CREATE (varun)-[:BUILT {scale: 'Global'}]->(uniride:App {name: 'UniRide', audience: 'Everyone'})
CREATE (varun)-[:ENGINEERED {stack: ['FastAPI', 'Neo4j']}]->(medgraph:System {name: 'MedGraph Nexus'})
CREATE (varun)-[:DEVELOPED {focus: 'Privacy'}]->(finete:Agent {name: 'Finete.AI'})

RETURN varun, ai, medgraph, uniride
