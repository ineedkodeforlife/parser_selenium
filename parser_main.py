from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


# Создайте экземпляр веб-драйвера
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
#------------------------------------------------------------------------------------------------#
driver.get('https://www.trademap.org/Index.aspx')
driver.find_element('id', 'ctl00_MenuControl_button1').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_label_RadioButton_TradeType_Export').click()
time.sleep(1)

driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_Input').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_Input').send_keys('Bbrazil')
time.sleep(3)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_Button_TimeSeries').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_GridViewPanelControl_ImageButton_Text').click()
time.sleep(3)
#------------------------------------------------------------------------------------------------#
driver.get('https://www.trademap.org/Index.aspx')

driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_Input').click()
time.sleep(2)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_Input').clear()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_Input').send_keys('China')
time.sleep(2)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_Button_TimeSeries').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_GridViewPanelControl_ImageButton_Text').click()
time.sleep(1)
#------------------------------------------------------------------------------------------------#
driver.get('https://www.trademap.org/Index.aspx')

driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_Input').click()
time.sleep(2)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Product_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_Input').clear()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_Input').send_keys('Iraq')
time.sleep(2)
driver.find_element('id', 'ctl00_PageContent_RadComboBox_Country_c0').click()
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_Button_TimeSeries').click()
time.sleep(1)
select_element = driver.find_element('id', 'ctl00_NavigationControl_DropDownList_MirrorDirect')
select = Select(select_element)
select.select_by_value('M')
time.sleep(1)
driver.find_element('id', 'ctl00_PageContent_GridViewPanelControl_ImageButton_Text').click()
time.sleep(1)
driver.close()



