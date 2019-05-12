## System Overview

### Deployment Diagram

All components will be deployed to Data Acquisition Gateway.

![Component Deployment Diagram][component-deployment-diagram]

### Component Diagram

Primary API library implementation will be done in C++.
Because:

1. Almost all parts of underlying Data Acquisition Framework are written in C++,
   including utility libraries.
   We can leverage such libraries to implement API libraries on top of it.
2. Console Utilities to be provided will be implemented in C++.

![Library Component Diagram][library-component-diagram]


[component-deployment-diagram]: images/architecture/component-deployment.png "Component Deployment Diagram"
[library-component-diagram]: images/architecture/library-component.png "Libraries"
