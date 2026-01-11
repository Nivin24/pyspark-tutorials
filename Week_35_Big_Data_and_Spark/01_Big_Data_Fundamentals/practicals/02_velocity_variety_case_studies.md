# Practical 02 – Velocity and Variety Case Studies

Goal: Practice mapping real-world scenarios to the 5Vs, with focus on **Velocity** and **Variety** [web:7][web:11].

## 1. Instructions

For each scenario below:

- Identify which Vs are most important.
- Decide whether batch, near real-time, or real-time processing is needed.
- Describe a high-level data pipeline (no tools yet, just concepts).

## 2. Scenarios

### Scenario A – Clickstream analytics

- A large e-commerce site logs every page view, search, and click as events.

Questions:

- Which Vs dominate (Volume, Velocity, Variety, Veracity, Value)? [web:10]
- What kind of latency is acceptable for analytics?
- Would you design this as a pure batch system, a streaming system, or hybrid?

### Scenario B – IoT sensor network

- Thousands of sensors send readings every few seconds (temperature, pressure, status).

Questions:

- Which Vs dominate here?
- How would you handle noisy/outlier readings (Veracity)? [web:15]
- Where would you store raw vs aggregated data?

### Scenario C – Financial transactions

- A bank processes card transactions worldwide, needs fraud flags quickly.

Questions:

- Which Vs are critical?
- What are the latency requirements?
- Why is Veracity especially important? [web:11]

### Scenario D – Social media analytics

- You want to track trending hashtags and basic sentiment.

Questions:

- Which Vs dominate (Variety is high: text, emojis, media)?
- Would you process full content in real time, or summaries?

## 3. Table summary

Fill in a summary table after writing your answers:

| Scenario  | Dominant Vs                  | Latency Needs     | Batch/Streaming/Hybrid | Notes |
|----------|------------------------------|-------------------|------------------------|-------|
| A        |                              |                   |                        |       |
| B        |                              |                   |                        |       |
| C        |                              |                   |                        |       |
| D        |                              |                   |                        |       |

## 4. Link to later weeks

- These case studies will later map to concrete tools:
  - Kafka / streaming engines for high Velocity.
  - Hadoop/Spark for Volume and Variety [web:6][web:8].
- Keep this file as a design reference for Week 35 Hadoop/Spark folders.
