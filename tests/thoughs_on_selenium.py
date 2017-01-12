
from selenium import webdriver
import time

def get_element_by_id_prot(driver,element_id):
    try:
        e = driver.find_element_by_id(element_id)
        return e
    except:
        return None

driver = None
try:
    driver = webdriver.Chrome()
    driver.get("chrome://extensions")
    iframes = driver.find_elements_by_tag_name("iframe")
    print "found", len(iframes), "iframes"
    for i in iframes:
        driver.switch_to_default_content()
        driver.switch_to_frame(i)
        print "switched to iframe", i
        e = get_element_by_id_prot(driver,"dev-toggle")
        if e is None:
            # raise Exception("dev toggle not found")
            print "dev toggle not found!"
            continue
        print "got the element",e
        e.click()
        print "clicked it!"
        time.sleep(3)
        eb = get_element_by_id_prot(driver,"load-unpacked")
        if eb is None:
            raise Exception("load unpacked not found")
        time.sleep(2)
        print "about to click"
        print "methods on eb", dir(eb)
        eb.click()
        print "after button click..."

        print "sleeping to allow time for dialog..."
        time.sleep(5)

    print "done with iframes..."
except:
    print "failed in some way :("
    import traceback
    traceback.print_exc()
finally:
    print "in finally"
    if driver is not None:
        driver.quit()

print "done"
