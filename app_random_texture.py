# coding: utf-8

## Imports ####################################

import streamlit as st  ## importing streamlit

import numpy as np  # importing libraries
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

###############################################

st.set_page_config(layout="centered")
st.title("🎨 Texture Arts Generator")

style_list = [
    "Perlin-like Blur", "Sinusoidal Gradient", 
    "RGB Pattern Blend", "Mandelbrot Fractal", 
    "Soft Paint Strokes", "Sharp Digital Blocks",
    "Gradient Vibes", "Retro Pixel Art", "Uzumaki", 
    "Starfield Glow", "Ripples on Water"
    ]
style = st.selectbox(
    "Choose a texture style", style_list)

fig, ax = plt.subplots(figsize=(4,4))

# ## 4 math arts
# ### Perlin-like Color Field

if style == style_list[0]:

    np.random.seed(42)
    data = np.random.rand(200, 200)

    sigma = st.slider("Blur Sigma", 1, 30, 10) 

    blurred = gaussian_filter(data, sigma=sigma)

    ax.imshow(blurred, cmap='Blues')
    plt.title("Perlin-like Color Field")
    plt.axis('off')
    st.pyplot(fig)


# ### Sinusoidal Gradient Patch
elif style == style_list[1]:
    
    freq = st.slider("Frequency", 1, 10, 5)
    
    x = np.linspace(0, freq * np.pi, 400)
    y = np.linspace(0, freq * np.pi, 400)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) + np.cos(Y)

    ax.imshow(Z, cmap='Spectral')
    plt.title("Sinusoidal Gradient Patch")
    plt.axis('off')
    st.pyplot(fig)


# ### RGB Pattern Blend
elif style == style_list[2]:
 
    width, height = 256,256

    R = np.random.rand(height, width)
    G = np.cos(np.linspace(0, 10, width))[None, :]
    B = np.sin(np.linspace(0, 10, height))[:, None]

    img = np.stack([R, G.repeat(height, 0), B.repeat(width, 1)], axis=2)
    ax.imshow(img)
    plt.axis('off')
    plt.title("RGB Pattern Blend")
    st.pyplot(fig)


# ### Mandelbrot Fractal Patch

elif style == style_list[3]:
    
    def mandelbrot(c, max_iter):
        z = 0
        for i in range(max_iter):
            z = z*z + c
            if abs(z) > 2:
                return i
        return max_iter

    w, h = 300, 300
    img = np.zeros((h, w))
    for x in range(w):
        for y in range(h):
            c = complex((x - w/2) / 100, (y - h/2) / 100)
            img[y, x] = mandelbrot(c, 50)

    ax.imshow(img, cmap='twilight_shifted')
    plt.title("Mandelbrot Fractal Patch")
    plt.axis('off')
    st.pyplot(fig)


# ## Soft Blurry Paint Strokes

elif style == style_list[4]:
 
    np.random.seed(0)
    noise = np.random.rand(100,100)

    sigma = st.slider("Blur Sigma", 6, 24, 20) 

    blurred = gaussian_filter(noise, sigma=sigma)

    ax.imshow(blurred, cmap='plasma')  # Try 'magma', 'cividis', 'twilight'
    plt.title("Soft Blurry Paint Strokes")
    plt.axis('off')
    st.pyplot(fig)


# ## Sharp Digital Blocks

elif style == style_list[5]:
    
    x = np.linspace(0, 10, 300)
    y = np.linspace(0, 10, 300)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)

    Z_quantized = np.floor(Z * 5) / 5  # Increase 5 → more steps, lower → blockier

    ax.imshow(Z_quantized, cmap='viridis')
    plt.axis('off')
    plt.title('Sharp Digital Blocks')
    st.pyplot(fig)


# ## Gradient vibes

elif style == style_list[6]:

    np.random.seed(1)

    sigma_grad_v = st.slider("Blur Sigma", 20, 50, 80) 

    noise1 = gaussian_filter(np.random.rand(300, 300), sigma=sigma_grad_v)
    noise2 = gaussian_filter(np.random.rand(300, 300), sigma=sigma_grad_v)
    combined = (noise1 + noise2) / 2

    ax.imshow(combined, cmap='plasma')  # Or 'inferno', 'coolwarm', 'gist_stern'
    plt.axis('off')
    plt.title("Gradient vibes")
    st.pyplot(fig)


# ## Retro Pixel Art Patches

elif style == style_list[7]:
 
    np.random.seed(3)
    small_grid = np.random.rand(16, 16)

    ax.imshow(small_grid, cmap='rainbow', interpolation='nearest')  # 'interpolation' = blocky effect
    plt.axis('off')
    plt.title('Retro Pixel Art Patches')
    st.pyplot(fig)


# ## Uzumaki

elif style == style_list[8]:
    
    theta = np.linspace(0, 6 * np.pi, 12000)
    r = theta**0.85  # Tighter swirl

    x = r * np.cos(theta + 0.4 * np.sin(2 * theta))
    y = r * np.sin(theta + 0.4 * np.sin(2 * theta))
    colors = np.cos(theta * 3)  # Adds variation in swirl ring coloring

    fig, ax = plt.subplots(figsize=(4, 4))

    # 🟠 Set orange background
    fig.patch.set_facecolor('#f97316')  # Tailwind's orange-500
    ax.set_facecolor('#f97316')

    ax.scatter(x, y, c=colors, cmap='twilight_shifted', s=0.5, alpha=0.85)
    ax.axis('off')

    ax.set_title('Uzumaki (Swirl)', color='black', backgroundcolor='white', pad=20)
    plt.axis('off')
    st.pyplot(fig)


# ## Starfield with Glow

elif style == style_list[9]:
 
    size = 512
    stars = np.zeros((size, size))

    # Add bright points
    for _ in range(500):
        x, y = np.random.randint(0, size, 2)
        stars[y, x] = np.random.rand() * 5

    # Create glow with blur

    sigma = st.slider("Blur Sigma", min_value=1.0, max_value=2.5, value=1.5, step=0.01)

    glow = gaussian_filter(stars, sigma=sigma)

    ax.imshow(glow, cmap='magma')
    plt.axis('off')
    plt.title('Starfield with Glow')
    st.pyplot(fig)


# ## Circular ripples on water

elif style == style_list[10]:
    slider_ = st.slider('Ripple size', 4.0, 6.0, 5.0, 0.01)

    x = np.linspace(-slider_, slider_, 400)
    y = np.linspace(-slider_, slider_, 400)
    X, Y = np.meshgrid(x, y)

    Z = np.sin(X**2 + Y**2) + np.cos(3 * np.sqrt(X**2 + Y**2))

    ax.imshow(Z, cmap='Blues', alpha=0.8)
    plt.axis('off')
    plt.title('Circular ripples on water')
    st.pyplot(fig)




