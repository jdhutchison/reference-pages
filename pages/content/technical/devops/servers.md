---
title: Servers
weight: 1
---


| Server           |IP              | Provider | Used for...           |
|------------------|----------------|----------|-----------------------|
| tigerbear        | 168.235.95.114 | Ramnode  | Sync, ops             |
| bluebear         | 108.61.168.93  | Vultr    | PSFau, AD             |
| moonbear         | 168.235.72.133 | Ramnode  | DNW, Courses, EQH, SS |
| sunbear          | 207.148.77.71  | Vultr    | DiM, DiP?             |
| brownbear        | 78.141.203.10  | Vultr    | PSFuk                 |



Tigerbear internal services
---------------------------

| Service          | Port | Run by   | UID      |
|------------------|------|----------|----------|
| Grafana          | 3000 | Docker   | 988      |
| Loki             | 3100 | Docker   | 988      |
| Vault            | 3200 | Docker   | 986      |
| Prometheus       | 9090 | Docker   | 988      |
| Radicale         |      | PHP      | www-data |

