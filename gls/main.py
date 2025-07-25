import numpy as np
import matplotlib.pyplot as plt
from lenstronomy.ImSim.image_model import ImageModel
from lenstronomy.PointSource.point_source import PointSource
from lenstronomy.LensModel.lens_model import LensModel
from lenstronomy.Data.imaging_data import ImageData
from lenstronomy.Data.psf import PSF
from lenstronomy.Util.image_util import add_poisson, add_background


def main():
    # Define lensing parameters
    lens_mass_kg = 2e15 * 1.989e30  # mass in kg
    source_distance_pc = 1039  # parsecs

    # Convert mass to solar masses
    lens_mass = lens_mass_kg / 1.989e30

    # Convert source distance to arcsec Einstein radius (simplified!)
    distance_to_observer_pc = 1e6  # 1 Mpc
    radial_distance = lens_mass / distance_to_observer_pc
    angular_distance_arcsec = source_distance_pc / distance_to_observer_pc * radial_distance * (180 / np.pi) * 3600

    # Lens model
    lens_model = LensModel(lens_model_list=['POINT_MASS'])
    point_source = PointSource(point_source_type_list=['LENSED_POSITION'])
    psf = PSF(psf_type='GAUSSIAN', fwhm=0.1)

    # Image grid
    num_pix = 100
    ra_at_xy_0, dec_at_xy_0 = -2.5, -2.5
    transform_pix2angle = np.array([[1, 0], [0, 1]]) * 0.05
    image_data = ImageData(image_data=np.zeros((num_pix, num_pix)),
                           ra_at_xy_0=ra_at_xy_0,
                           dec_at_xy_0=dec_at_xy_0,
                           transform_pix2angle=transform_pix2angle)

    # Model
    image_model = ImageModel(data_class=image_data,
                             psf_class=psf,
                             lens_model_class=lens_model,
                             source_model_class=None,
                             point_source_class=point_source)

    # Parameters
    kwargs_lens = [{'theta_E': angular_distance_arcsec}]
    kwargs_ps = [{'ra_image': [0], 'dec_image': [0], 'point_amp': [100]}]

    # Generate image
    lensed_image = image_model.image(kwargs_lens=kwargs_lens, kwargs_ps=kwargs_ps)

    # Add noise
    exp_time = 150
    background_rms = 0.3
    poisson = add_poisson(lensed_image, exp_time=exp_time)
    background = add_background(lensed_image, sigma_bkd=background_rms)
    image_noisy = lensed_image + poisson + background

    # Plot original
    plt.figure(figsize=(5, 5))
    plt.imshow(np.log10(np.abs(lensed_image)), origin='lower', cmap='gist_heat_r')
    plt.title("Original Lensed Image")
    plt.colorbar(label="Log Flux")
    plt.show()

    # Plot noisy
    plt.figure(figsize=(5, 5))
    plt.imshow(np.log10(np.abs(image_noisy)), origin='lower', cmap='CMRmap')
    plt.title("Reconstructed Lensed Image (Red Hue)")
    plt.colorbar(label="Log Flux")
    plt.show()


if __name__ == "__main__":
    main()
