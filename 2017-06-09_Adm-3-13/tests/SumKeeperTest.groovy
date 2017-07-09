/**
 * Created by brandon on 7/9/17.
 */
class SumKeeperTest extends GroovyTestCase {

    void testAdd() {
        float[] list = [7.0, 8.0, 2.5, 16.3, 800.5, 40.0] as float[]
        SumKeeper s = new SumKeeper(list)
        s.add(4, 5.0f)
        float result = s.partialSum(4)
        assertTrue(Math.abs(result - 839.3f) < 0.001f)
    }
}
