# ============================================================
# MIRCF — Reproducibility Makefile
# ============================================================
# Usage:
#   make reproduce   -> execute notebook + generate artifacts
#   make verify      -> verify checksums + outputs
#   make lint        -> run pre-commit locally
#   make clean       -> remove generated artifacts
# ============================================================

PYTHON := python
NOTEBOOK := notebooks/MIRCF_Section6_Reproduction.ipynb
EXECUTED := executed.ipynb
OUTPUT_DIR := outputs
CHECKSUMS := checksums.txt

.PHONY: help reproduce verify lint clean

help:
	@echo "Available targets:"
	@echo "  make reproduce   Execute notebook and generate outputs"
	@echo "  make verify      Verify outputs and checksums"
	@echo "  make lint        Run pre-commit on all files"
	@echo "  make clean       Remove generated artifacts"

# ------------------------------------------------------------
# Reproduce all paper figures and tables
# ------------------------------------------------------------
reproduce:
	@echo "▶ Creating outputs directory"
	mkdir -p $(OUTPUT_DIR)

	@echo "▶ Executing MIRCF notebook"
	jupyter nbconvert \
		--to notebook \
		--execute $(NOTEBOOK) \
		--output $(EXECUTED)

	@echo "▶ Verifying outputs directory is non-empty"
	test -d $(OUTPUT_DIR)
	test "$$(ls -A $(OUTPUT_DIR) | grep -v readme.md)" \
		|| (echo "ERROR: outputs directory empty" && exit 1)

	@echo "▶ Generating checksums"
	find $(OUTPUT_DIR) -type f -print0 | sort -z | xargs -0 sha256sum > $(CHECKSUMS)

	@echo "✔ Reproduction complete"

# ------------------------------------------------------------
# Verify reproducibility against committed checksums
# ------------------------------------------------------------
verify:
	@echo "▶ Verifying checksums"
	$(PYTHON) scripts/verify_checksums.py

	@echo "✔ Checksum verification passed"

# ------------------------------------------------------------
# Run all pre-commit hooks locally
# ------------------------------------------------------------
lint:
	@echo "▶ Running pre-commit"
	pre-commit run --all-files

# ------------------------------------------------------------
# Clean generated artifacts (safe)
# ------------------------------------------------------------
clean:
	@echo "▶ Cleaning generated files"
	rm -f $(EXECUTED)
	rm -f $(CHECKSUMS)
	find $(OUTPUT_DIR) -type f ! -name 'readme.md' -delete

	@echo "✔ Clean complete"
