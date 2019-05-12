# Overview

All ThingsPro Gateways (e.g., UC-8112-LX-CG) come pre-installed with a *Data Acquisition Framework*.
As indicated by the name, the *Data Acquisition Framework* is set of services that help you develop *Data Acquisition* applications.

The *Data Acquisition Framework* typically consists of the following services:

**Broker Service**, which dispatches subscribed Tags to individual sub-services

**Storage Service**, which stores Tags of interest into *Log Files*

**Upload Service**, which uploads *Log Files* to remote servers

Note: Refer to the *ThingsPro User's Manual* for additional details on the **Modbus Management Framework**.

![System Overview][tutorial-overview]

This tutorial explains the usage of the `libmxidaf` API. You can use the `libmxidaf` API to acquire data,
log, and tag values from other devices or sensors for your data-acquisition applications.

Use the `libmxidaf` API to:

- Publish Tags to the Data Acquisition Framework.
- Subscribe to Tags in the Data Acquisition Framework.
- Read Tags from the Modbus Management Framework.
- Write the Modbus Tag values into the Modbus Management Framework.

When you import a Tag from the *Modbus Management Framework* or through the `libmxidaf` API into a **Broker Service**,
it is dispatched to the **Storage Service** or to applications called *subscribe functions* through `libmxidaf`.
If a Tag is configured for logging, the **Storage Service** saves it to a *Log File*.

Note: The code snippets used in this tutorial have been simplified for clarity. Refer to [Reference](reference.md) for the complete code.

## libmxidaf

The `libmxidaf` API provides interfaces in C and Python.

The structure of a `Tag` is modeled on the basic structure of a device reading and consists of the following three components:

- Value of Reading(`value`)
- Time of Reading(`at`), in UTC
- Unit of Reading(`unit`)

[tutorial-overview]: images/overview.png "Overview"
