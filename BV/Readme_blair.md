**----Papers----**


The MODIS Aerosol Algorithm, Products, and Validation
[https://journals.ametsoc.org/doi/full/10.1175/JAS3385.1]
* Eight thousand MODIS aerosol retrievals collocated with AERONET measurements confirm that one standard deviation of MODIS optical thickness retrievals fall within the predicted uncertainty of  ±0.05 ± 0.15 \tau over land
* The accuracy of the MODIS retrievals suggests that the product can be used to help narrow the uncertainties associated with aerosol radiative forcing of global climate.
* Aerosols are one of those important geophysical parameters that determine the earth?s energy balance and hydrological cycle


Applying SPOT data to estimate the aerosol optical depth and air quality
[https://ac.els-cdn.com/S1364815201000470/1-s2.0-S1364815201000470-main.pdf?_tid=29fa1c1b-6c6b-4fea-bd08-e214cc54a0c0&acdnat=1548192920_58abd234103bd93bb6d519fe529d3538]
* assume lambertarian surface
* optical depth can vary from temporal changes in surface canopy
* optical depth can be used to estimate atmospheric turbidity


Analysis of the Aerosol Optical Depth and theAir Quality in Qingdao, China
[https://pdfs.semanticscholar.org/c91c/24188996ec39b32c5d50f7bd389826442db1.pdf]
* Correlation between air quality and optical depth varies seasonally
* Researches have proved the capability of MODIS AOD to monitor the air quality. (source?)
* more accurate over land than over ocean


Estimating the impact of the 2004 Alaskan forest fires on episodic particulate matter pollution over the eastern United States through assimilation of satellite-derived aerosol optical depths in a regional air quality model
[https://agupubs-onlinelibrary-wiley-com.ezproxy.library.ubc.ca/doi/full/10.1029/2007JD009767]
* This paper is mostly about modeling and doesnt seem directly relevant to project

Comparing MODIS and AERONET  aerosol optical depth over China
[https://www.researchgate.net/publication/232869270_Comparing_MODIS_and_AERONET_aerosol_optical_depth_over_China]
* MODIS over estimation for small AOD and under estimation for large AOD
* used wavelengths at 0.47,0.55, and 0.66 micro m (0.55 from MODIS was slightly more accurate)
* non linear results due to surface reflectance
* even though MODIS has cloud screening it is still a possible source of error



Evaluation of the Moderate Resolution Imaging Specroradiometer aerosol products at two Aerosol Robotic Network stations in China
[https://agupubs-onlinelibrary-wiley-com.ezproxy.library.ubc.ca/doi/full/10.1029/2007JD008474]
* "Although AOD retrievals from the MODIS agree with AERONET AOD measurements within the expected error range, AOD is generally overestimated on clean days and underestimated for high aerosol loading events."
* surface reflectance and largely increase the optical depth error
* Data with the MODIS C005 algorithms (Level 2) appears to perform better in eliminating surface reflectance errors.
* surface dust from storms engrosses AOD error and over estimates poor air quality
* since dust is less spherical (non spherical assumption) it can be more easily filtered out of the Data
* Since water is less reflective it is easier to estimate AOD
* MODIS C004 has largest error in February and smallest in summer





**---To Do---**
1. Find ground data source
* Read and look into data and sort it
 [https://eospso.gsfc.nasa.gov/sites/default/files/publications/AERONETpamphlet_508_sm.pdf]
* read AERONET data with this helper function [https://gist.github.com/robintw/569ce05e01f405c7e9744d651123fbb6#file-read_aeronet-py] hint: looks like a csv file

2. Pick a measurement site
* needs to be somewhere near and urban centre with population density and or industry
* How about UCLA (34.070N,118.443W)? should be limited with clouds and large enough urban centre
*picked table mtn. CO, because it was nearish Denver and has a long measuting time. hopefully will catch forest fire signal


3. Get aod, deom and cloud frac file from modis

4. AERONET notes (AErosol RObotic NETwork) (https://aeronet.gsfc.nasa.gov/)
*established by NASA and LOA-PHOTONS (CNRS) and expanded by other national agenciese
* data levels  Level 1.0 (unscreened), Level 1.5 (cloud-screened), and Level 2.0 (cloud screened and quality-assured)
*AS OF 2014 uses CIMEL Electronique CE318 multiband sun photometer
*two basic measurements, either direct sun or sky, both
*10 second measurement 
*processing  Aerosol Optical Depth (AOD) retrieval. 2. AOD cloud screening. 3. Seaprism processing. 4. Sky Radiance data (Almucantars and Principal Planes) inversion.
* calibration? (https://aeronet.gsfc.nasa.gov/new_web/system_descriptions_calibration.html)

4.5 Moderate Resolution Imaging Spectroradiometer  (MODIS) (Aqua sat)
*Collection 6
* 3km res
*Cloud masked 

*Validation Strategy (https://modis-atmos.gsfc.nasa.gov/sites/default/files/ModAtmo/MODIS_Atmos_Webinar-2_Munchak_3kmaerosol.pdf)
**3	km	shows	slight	high	bias	and	a	bit	more	uncertainty		
**	Revised	expected	error	for	3	km	land	product:	±0.05	+	0.2*AOD
**Only	the	AOD	at	550	nm	has	been	studied	in	depth	at	this	point
*Aerosol optical thickness (AOT) is analagous to AOD
* Cloud cover from MODIS And near IR channels (https://modis.gsfc.nasa.gov/data/dataprod/mod06.php) -Indication of cloud shadowing on a scene is also provided Cloud fraction provided by IR channels
*Colection 6 is a joint product that automatically slects wither Dark target or deep blue algorithm for better data

*The individual Land or Ocean SDS is generally preferred because
- it contains more wavelengths
- gives more information about quality
- at level 3 it gives a quality weighted product that screens
out anomalies, Land_And_Ocean Is useful if you need both together but may not
give the same results as Land or Ocean
(https://cimss.ssec.wisc.edu/dbs/China2011/Day2/Lectures/MODIS_A-Kleidman_MODIS_AerosolProducts.pdf)
*Fine Fraction over land should be seen as a qualitative
indicator not as a quantitative measurement.

*