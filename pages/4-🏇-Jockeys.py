from utils import data as data, contentPage as cp

df = data.get_data("jockeys")
cp.simple_page(
    "Jockeys",
    "🏇",
    df,
    "Datos básicos de todos los jockeys registrados en las carreras de caballos"
)
