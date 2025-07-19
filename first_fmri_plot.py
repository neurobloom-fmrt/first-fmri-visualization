#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nilearn import plotting, datasets, image

# --- Step 1: Load a sample motor activation image ---
img = datasets.load_sample_motor_activation_image()

# --- Step 2: Create a "contrast" image ---
# (Just an example: subtracting a smoothed version from the original)
img_smooth = image.smooth_img(img, fwhm=6)  # blurred/smoothed image
img_contrast = image.math_img("img1 - img2", img1=img, img2=img_smooth)

# --- Step 3: Plot both images side by side ---
plotting.plot_stat_map(
    img,
    bg_img=None,  # No background to avoid errors
    title='Original Activation',
    threshold=3.0,
    display_mode='ortho'
)

plotting.plot_stat_map(
    img_contrast,
    bg_img=None,
    title='Contrast (Original - Smoothed)',
    threshold=2.0,
    display_mode='ortho'
)

# --- Step 4: Show the plots ---
plotting.show()


# In[1]:


from nilearn import plotting, datasets, image

# --- Step 1: Load a sample motor activation image ---
img = datasets.load_sample_motor_activation_image()

# --- Step 2: Create a "contrast" image ---
img_smooth = image.smooth_img(img, fwhm=6)
img_contrast = image.math_img("img1 - img2", img1=img, img2=img_smooth)

# --- Step 3: Plot and save the original image ---
plotting.plot_stat_map(
    img,
    bg_img=None,
    title='Original Activation',
    threshold=3.0,
    display_mode='ortho',
    output_file='original_activation.png'  # <-- Saves image
)

# --- Step 4: Plot and save the contrast image ---
plotting.plot_stat_map(
    img_contrast,
    bg_img=None,
    title='Contrast (Original - Smoothed)',
    threshold=2.0,
    display_mode='ortho',
    output_file='contrast_activation.png'  # <-- Saves image
)

print("Images saved as 'original_activation.png' and 'contrast_activation.png'")

