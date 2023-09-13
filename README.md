# Slidey Demo
## Overview
This project is a web chat application that uses OpenAI, Streamlit, and PandasAI. It allows users to upload CSV datasets, interact with them, and perform various data analysis tasks, including histogram generation and graph creation.

## Setup
### 1. Create a Virtual Environment and Install Dependencies

```bash
virtualenv slidey_demo
```

```bash
source slidey_demo/bin/activate
```

```bash
pip install -r requirements.txt
```


### 2. Update the Image Path in `app.py`
In the `app.py` file, make sure to update the path to the temporary image location within your local directory. Find and modify line 25 as follows:
```Python
st.image("...slidey_demo/exports/charts/temp_chart.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
```


### 3. Run the Streamlit Application for Demo
```bash
streamlit app run.py
```

