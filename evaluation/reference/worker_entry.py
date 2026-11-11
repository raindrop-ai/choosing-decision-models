"""Run the frozen native staging/inference reference in an isolated CUDA environment."""
import runpy

if __name__ == "__main__":
    runpy.run_module("decision_lab.worker_entry", run_name="__main__")
