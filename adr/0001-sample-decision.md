# 0001. Store Application Logs in Centralized ELK Stack

*Status: accepted*
*Date: 2026-03-16*

## Context

Our application generates logs from multiple microservices running in
different environments (development, staging, production).  At
present, logs are stored on local disks and are hard to collect for
troubleshooting.  Engineers need a unified view of logs to diagnose
issues and perform root cause analysis.

## Decision

We will deploy a centralized logging stack using Elasticsearch,
Logstash, and Kibana (ELK).  All services will forward logs to
Logstash, which will process and send them to Elasticsearch.  Kibana
will provide a dashboard for querying and visualizing logs.

## Consequences

- Simplifies log aggregation and search across services and
  environments.
- Requires additional infrastructure to host and maintain the ELK
  stack.
- Increases observability and speeds up incident response.

## Alternatives

- **Continue local storage** – Does not solve the issue of
  fragmented logs.
- **Use a managed logging service (e.g. AWS CloudWatch)** – Could be
  considered in the future but is currently cost‑prohibitive for
  on‑prem deployments.
