# Expansion of Deforestation in the Cerrado of Maranhão, Brazil (2001–2023)

This repository contains the code and data used in the article:

> Correia, L. F. C. S.; Rocha, T. V. S. M.; Bezerra, D. S.; Silva Junior, C. H. L.; Costa, S. S. (2026). **Expansão do desmatamento no cerrado maranhense entre os anos de 2001 – 2023** (*Expansion of deforestation in the Cerrado (Brazilian savanna) of Maranhão State, Brazil (2001–2023)*). *Revista Tocantinense de Geografia*, 15(35), 45–67. https://doi.org/10.70860/rtg.v15i35.19356

Using PRODES Cerrado data (INPE), the study examines the temporal evolution of absolute and relative deforestation in the Cerrado of Maranhão by biome, microregion and municipality. Deforestation fell until 2013 and rose sharply from 2020; it spread over the whole Cerrado of Maranhão rather than only the south of the state.

* **English summary:** [`report_en.pdf`](report_en.pdf) — a short companion report in English, generated from the notebooks.

## Authors

* **Luís Fernando Cirqueira da Silva Correia** (lead author) — Universidade Federal do Maranhão (UFMA) — [0009-0004-4350-1478](https://orcid.org/0009-0004-4350-1478) — *luis.correia@discente.ufma.br*
* **Thomas Victor de Sousa Malheiros Rocha** — UFMA — [0009-0000-2623-7944](https://orcid.org/0009-0000-2623-7944)
* **Denilson da Silva Bezerra** — UFMA — [0000-0002-9567-7828](https://orcid.org/0000-0002-9567-7828)
* **Celso Henrique Leite Silva Junior** — UFMA — [0000-0002-1052-5551](https://orcid.org/0000-0002-1052-5551)
* **Sérgio Souza Costa** — UFMA — [0000-0002-0232-4549](https://orcid.org/0000-0002-0232-4549) — *sergio.costa@ufma.br*

## Repository structure

| Path | What it produces |
|------|------------------|
| `analise_bioma.ipynb` | Deforestation totals for the Cerrado of Maranhão and the annual increment and its year-on-year change (Figure 4). |
| `analise_microregioes.ipynb` | Deforestation by microregion, 2000 and 2023 (Table 1); exports the data behind Figure 5. |
| `analise_municipios.ipynb` | Deforestation by municipality: absolute ranking (Table 3) and relative ranking (Table 4); exports the data behind Figure 6. |
| `analise_grade_micro.ipynb` | Deforestation on a regular 10 × 10 km grid (Figure 7); exports the grid for map composition. |
| `calculo_area_ti.ipynb` | Deforestation inside one Indigenous Land (Krikati), as a check of the TerraBrasilis value in Table 5. **Needs input data that is not in this repository** (see below). |
| `report_en.ipynb`, `report_en.pdf`, `build_report.py` | English companion report and the script that rebuilds it. |
| `tables.html` | HTML version of the municipal tables. |
| `dados/` | Input data (see below). |
| `temp/` | Shapefiles exported by the notebooks for map composition. Created automatically and ignored by git. |

Tables 2 and 5 of the article were taken from the TerraBrasilis portal and are not computed here.

### Data

| File | Source |
|------|--------|
| `dados/csv/terrabrasilis_cerrado_5_18_2024,_11_26_39 AM.csv` | Annual deforestation by municipality, PRODES Cerrado, downloaded from [TerraBrasilis](https://terrabrasilis.dpi.inpe.br/) (INPE) on 18 May 2024. Biennial until 2012, annual from 2013. |
| `dados/desmatamento/microregiao_ma_cerrado_desmatamento.zip` | Share of each microregion's Cerrado area deforested by 2000 and from 2001 to 2023, computed from PRODES in Google Earth Engine. |
| `dados/desmatamento/grade_cerrado_ma_prodes.zip` | Regular grid over the Cerrado of Maranhão with the share of each cell deforested up to 2000 (`d2000`) and from 2001 to 2023 (`d001_23`), computed from PRODES. |
| `dados/limites/MA_Microrregioes_2022.zip`, `MA_Municipios_2022.zip` | IBGE 2022 territorial boundaries. |
| `dados/limites/cerrado_maranhense.zip` | Boundary of the Cerrado biome in Maranhão. |

Two inputs are not in this repository:

* `calculo_area_ti.ipynb` reads the Indigenous Land polygons (FUNAI) and the yearly PRODES polygons for the Cerrado of Maranhão from a local folder. Its saved outputs are kept, but it cannot be re-run from a fresh clone. It is not needed for any result of the article.
* `analise_grade_micro.ipynb` can draw the outlines of selected Indigenous Lands on one of its maps (`dados/limites/tis_selecionadas.zip`). Without that file the map is drawn without them; nothing else changes.

Figure 8 of the article (deforestation from 2015 to 2023 on the grid) was not produced by these notebooks.

## Getting started

The notebooks were verified to reproduce with **Python 3.12** (see `.python-version`).

```bash
git clone https://github.com/LambdaGeo/analise-cerrado-ma.git
cd analise-cerrado-ma
python3.12 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
jupyter notebook
```

To run a notebook non-interactively from top to bottom:

```bash
jupyter nbconvert --to notebook --execute --inplace analise_municipios.ipynb
```

### Rebuild the English report (optional)

The report is printed to PDF with headless Chromium, which needs a few extra packages:

```bash
pip install -r requirements-report.txt
playwright install chromium
python build_report.py
```

The report checks every value quoted in its text against the analysis and stops if they differ.

## How to cite

If you use this code or data, please cite the article (DOI: [10.70860/rtg.v15i35.19356](https://doi.org/10.70860/rtg.v15i35.19356)). Citation metadata for the software is available in [`CITATION.cff`](CITATION.cff).

## License

The source code in this repository is released under the [MIT License](LICENSE).

The data in `dados/` derive from INPE (PRODES, TerraBrasilis) and IBGE and remain subject to their terms of use; please cite the original sources when reusing them.
