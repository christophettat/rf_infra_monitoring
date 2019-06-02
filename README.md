# How to make RobotFramework test execution aware of test infrastructure (or other) dependencies
## what are we trying to solve?
It may happen that your system under relies on an infrastrucre or on subcomponents that are not in your control.
This is typically the case when automating the test of large and/or distributed system,running in a shared infrastructure.

Wouldn't it be great if the tests were able to pause and wait that all dependencies are met or be flagged in case infrastructure disruption was found during its exection? 

This demo will propose a design for this.
## High level design

