package hy.testhon.hytest_autoui;
import org.testng.Assert;
import org.testng.annotations.Test;

public class BStackLocalTest extends SeleniumTest {

    @Test
    public void test() throws Exception {
        driver.get("https://kolkata.bugbash.live/");

        Assert.assertTrue(driver.getTitle().contains("BrowserStack Local"));
    }
}
