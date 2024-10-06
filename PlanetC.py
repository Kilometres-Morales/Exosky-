#lalande
from astroquery.gaia import Gaia
from astropy.coordinates import SkyCoord, ICRS, solar_system_ephemeris, get_sun
import astropy.units as u
from astropy.time import Time
import matplotlib.pyplot as plt

#define coordinates
RA_VALUE = 165.84
DEC_VALUE = 35.97
DISTANCE_VALUE = 8.3

lalande_21185_b_coord = SkyCoord(ra=RA_VALUE*u.deg, dec=DEC_VALUE*u.deg, distance=DISTANCE_VALUE*u.pc, obstime=Time("2024-10-01T00:00:00"))

search_radius = 20 * u.deg  # Example search radius around Proxima Centauri b

#query for stars around
query = f"""
SELECT ra, dec, phot_g_mean_mag 
FROM gaiadr3.gaia_source 
WHERE CONTAINS(
    POINT('ICRS', ra, dec),
    CIRCLE('ICRS', {lalande_21185_b_coord.ra.deg}, {lalande_21185_b_coord.dec.deg}, {search_radius.to(u.deg).value})
)=1
"""

# Launch the Gaia job
job = Gaia.launch_job(query)
result_table = job.get_results()

proxima_icrs = lalande_21185_b_coord.transform_to(ICRS())

with solar_system_ephemeris.set('jpl'):
    sun_position = get_sun(proxima_icrs.obstime)

#shift all stars to exoplanet's perspective
star_ra_shifted = result_table['ra'] - sun_position.ra.deg
star_dec_shifted = result_table['dec'] - sun_position.dec.deg

def calculate_star_sizes(magnitudes, min_size=1, max_size=50):
    """
    calculates size bazed on brightness
    """
    # Invert the magnitudes to get sizes (lower magnitude -> larger size)
    sizes = max_size - (magnitudes - magnitudes.min()) / (magnitudes.max() - magnitudes.min()) * (max_size - min_size)
    return sizes

# Get the star sizes based on their brightness
star_sizes = calculate_star_sizes(result_table['phot_g_mean_mag'])

# Step 6: Plot the night sky from Proxima Centauri b's perspective, with star size proportional to brightness
plt.figure(figsize=(10, 10))
plt.scatter(star_ra_shifted, star_dec_shifted, s=star_sizes, color='white', label="Stars (scaled by brightness)")
plt.gca().set_facecolor('black')
plt.xlabel("Shifted RA (degrees)")
plt.ylabel("Shifted Dec (degrees)")
plt.title(f"Night Sky from Lalande 21185-b (RA: {RA_VALUE}, Dec: {DEC_VALUE})")
plt.legend()
plt.show()