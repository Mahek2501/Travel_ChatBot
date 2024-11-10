# One-Day Tour Planning Assistant

## Overview
The **One-Day Tour Planning Assistant** is a conversational, AI-driven tool that helps users design a personalized itinerary for a one-day trip in any city. This assistant leverages **Ollama** to create an interactive and adaptive experience, allowing users to outline preferences, adjust details, and receive a customized, optimized itinerary in real-time.

## Key Features
- **Interactive Chat-Based Interface**: Users specify preferences like city, budget, interests, and schedule through a user-friendly chat interface. 
- **Personalized Memory Persistence**: By storing user preferences across sessions, the assistant personalizes future itineraries based on historical data, providing a progressively more tailored experience.
- **Real-Time Itinerary Adjustment**: The assistant dynamically adapts the plan as users add new constraints, ensuring flexibility and convenience throughout the planning process.
- **Optimized Travel Routes**: Itineraries are crafted to balance user preferences, time, and budget. For example, taxi options are recommended when feasible within the budget.
- **Contextual Weather and Attraction Status Integration**: The assistant factors in current weather and attraction statuses to help users avoid potential disruptions.
- **Visual Itinerary & Map**: A comprehensive itinerary includes a visual map, optimized travel routes, time allocations, and estimated costs.

## Components

### LLM-Based Agents
- **User Interaction Agent**: Engages with the user, gathering essential trip information and preferences.
- **Itinerary Generation Agent**: Curates an initial itinerary tailored to user inputs.
- **Optimization Agent**: Refines the itinerary, adjusting paths based on the user’s budget and time constraints.
- **Weather & News Agents**: Checks weather and local events that may impact the itinerary.
- **Memory Agent**: Stores and retrieves user preferences using a graph database to deliver a consistent, personalized experience.

### Database
- **Graph Database (Neo4j)**: Efficiently stores user data in triplet format, maintaining context across sessions and evolving preferences.

### Frontend
- **Streamlit Interface**: Provides an intuitive, chat-based frontend where users can log in, interact with the assistant, view past conversations, and make updates to their itineraries seamlessly.

## Setup & Requirements

### Software Requirements
- **Python** 3.8 or higher
- **Ollama**
- **Neo4j** for graph-based memory
- **Streamlit** for frontend

### Python Libraries
- `FastAPI` for microservices
- `Transformers` for LLMs
- `Outlines` for function calling
- Additional dependencies listed in `requirements.txt`

### Installation
1. Clone this repository and install dependencies:
   ```bash
   pip install -r requirements.txt
