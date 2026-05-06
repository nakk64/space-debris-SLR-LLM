
# Envisat Space Debris SLR Tracker

This project focuses on Space Situational Awareness (SSA) by analyzing Satellite Laser Ranging (SLR) tracking data for the Envisat satellite (a large piece of space debris). The pipeline parses raw CRD format tracking data, detects statistical anomalies (potential orbital decay or measurement errors), and leverages a local AI model (TinyLLaMA) to provide an expert analysis report.

## Features
- **Custom CRD Parser**: Recursively reads and extracts TDT timestamps and light-travel ranges from ILRS `.fr2` files.
- **Statistical Anomaly Detection**: Automatically calculates the median range and flags any observations that deviate by more than 3 standard deviations (3σ).
- **Automated Visualization**: Generates scatter plots tracking Envisat's range over time, highlighting detected anomalies.
- **Local AI Analysis**: Integrates with `llama.cpp` to feed data summaries to a local TinyLLaMA model, producing an automated Markdown report of the orbital behavior.
- **Containerized Environment**: Includes a Dockerized Jupyter environment (`envisat-analysis/`) for reproducible execution.

## Prerequisites
To run this project locally, you need:
- Python 3.8+
- Jupyter Notebook
- Python Packages: `pandas`, `numpy`, `matplotlib`
- [llama.cpp](https://github.com/ggerganov/llama.cpp) installed locally with the `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` model (or update the path in the script to point to your preferred GGUF model).

## Project Structure
- `envisat/`: Place your raw ILRS `.fr2` tracking files here (can be organized in subfolders by year).
- `processed/`: Output directory where parsed CSVs, combined datasets, plots, and analysis reports are saved.
- `Untitled.ipynb`: The main Jupyter Notebook containing the parsing, plotting, and LLaMA inference pipeline.
- `envisat-analysis/`: Docker setup (`Dockerfile`, `docker-compose.yml`) for running a containerized analysis environment.

## Usage
1. **Prepare Data**: Ensure your `.fr2` CRD files are located inside the `envisat/` directory.
2. **Configure Model Path**: Open `Untitled.ipynb` and ensure the `MODEL_PATH` and `LLAMA_CLI` variables point to your local `llama.cpp` installation.
3. **Run Pipeline**: Execute the cells in `Untitled.ipynb`. 
4. **View Results**: Check the `processed/` folder (or project root) for:
   - `envisat_all_parsed.csv` (the combined dataset)
   - `envisat_range_plot.png` (the generated visualization)
   - `envisat_analysis_report.md` (the AI-generated analysis report)
   - `envisat_full_analysis_report.pdf` (the comprehensive system-generated PDF report)

## Docker Environment (Optional)
If you prefer a containerized environment, navigate to the `envisat-analysis/` folder and run:
```bash
docker-compose up --build
```
This will spin up a Jupyter Data Science notebook with all required Python dependencies installed.

# space-debris-SLR-LLM
Analyzes Satellite Laser Ranging (SLR) data for Envisat to track orbital range over time, detect anomalies, and use a local TinyLLaMA model to assess potential orbital decay or perturbations in this large LEO debris object.

 2f78a98f6eb260381af282d85847d2f60cbca98a
