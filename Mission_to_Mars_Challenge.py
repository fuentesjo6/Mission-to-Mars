
from bs4 import BeautifulSoup as soup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd




# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)




# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)




html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')




# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title





# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images




#Set up URL to visit site we are scraping
url = 'https://spaceimages-mars.com'
browser.visit(url)





# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()



# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')





img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel





img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url





df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


df.to_html()

browser.quit()


# ### Visit the NASA Mars News Site¶

# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

slide_elem.find('div', class_='content_title')


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# ### Mars Facts

# In[31]:


df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)

#full_image_element = browser.find_by_tag('Open')[1]
#full_image_element.click

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

links = browser.find_by_css("a.product-item h3")

for image in range(len(links)):
    
    try:
        print('gottem')
    
        hemisphere = {}
        # 3. Write code to retrieve the image urls and titles for each hemisphere.

        # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[image].click()

        # Next, we find the sample image anchor tag and extract the href
        sample_elem = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']

        # Get the hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text

        # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)

        browser.back()
        
    except Exception as e:
        print('whoops!', e)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

