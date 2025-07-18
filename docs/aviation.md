# Global Constants

| Parameter     | Value |
| ------------- | ----- |
| Days per year | 366   |

# Model Inputs

## Input Data

| Parameter                             | Value              | Unit              | Source                                                                                                                                     |
| ------------------------------------- | ------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Passengers per year                   | $5 \times 10^9$    | passengers/year   | [ATAG Facts & Figures](https://atag.org/facts-figures)                                                                                     |
| Revenue Passenger Kilometers per year | $9 \times 10^{12}$ | passenger-km/year | [IATA Market Analysis](https://www.iata.org/en/iata-repository/publications/economic-reports/air-passenger-market-analysis-december-2024/) |

## Model Parameters

| Parameter                  | Value | Unit                                       |
| -------------------------- | ----- | ------------------------------------------ |
| Aircraft flights per day   | 3     | flights $\cdot$ day^-1^                    |
| Average seats per aircraft | 250   | seats[@raymerAircraftDesignConceptual2018] |

# Model Equations

The model uses two fundamental equations to calculate key aviation metrics:

## Passengers per Day

$$
\begin{equation}
\text{passengers per day} = \frac{\text{passengers per year}}{\text{days per year}} \label{equation:passengers-per-day}
\end{equation}
$$

## Required Global Fleet Size

$$
\begin{equation}
\text{Required Global Fleet} = \frac{\text{passengers per day}}{\text{seats per aircraft} \times \text{flights per aircraft per day}} \label{equation:required-fleet}
\end{equation}
$$

# Model Description

This simple model calculates the theoretical minimum number of aircraft required to transport all global passengers based on:

- Annual passenger volume
- Daily passenger distribution (assuming uniform distribution)
- Aircraft utilization (flights per day)
- Aircraft capacity (seats per aircraft)

The model assumes perfect efficiency with no consideration for factors such as:

- Route optimization
- Aircraft positioning
- Maintenance downtime
- Load factors
- Seasonal variations
