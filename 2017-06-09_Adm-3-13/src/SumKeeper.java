public class SumKeeper {
    private float[] A;
    private BNode[] S;
    private int sMax;

    class BNode {
        BNode(int min, int max, float value) {
            this.min = min;
            this.max = max;
            this.value = value;
        }
        int min;
        int max;
        float value;
    }

    public SumKeeper(float[] A) {
        this.A = A;
        int ln2 = (int)Math.ceil(Math.log(A.length) / Math.log(2));
        this.S = new BNode[(0x1 << ln2) - 1];
        initS(0, A.length - 1, 0);
    }

    private void initS(int min, int max, int sNode) {
        if(sNode > sMax) sMax = sNode;
        if(min >= max)
            S[sNode] = new BNode(min, max, A[min]);
        else if (min == max - 1)
            S[sNode] = new BNode(min, max, A[min] + A[max]);
        else {
            int mid = min + (max - min) / 2;
            initS(min, mid, 2 * sNode + 1);
            initS(mid + 1, max, 2 * sNode + 2);
            float sum = S[2 * sNode + 1].value + S[2 * sNode + 2].value;
            S[sNode] = new BNode(min, max, sum);
        }
    }

    public void add(int i, float y) {
        if(i - 1 > A.length) throw new IndexOutOfBoundsException();
        A[i] += y;
        addS(i, y, 0);
    }

    private void addS(int i, float y, int sNode) {
        if(sNode > sMax) return;
        S[sNode].value += y;
        int mid = S[sNode].min + (S[sNode].max - S[sNode].min) / 2;
        if(mid >= i) {
            addS(i, y, 2 * sNode + 1);
        } else {
            addS(i, y, 2 * sNode + 2);
        }
    }

    public float partialSum(int i) {
        return partialSum(i, 0);
    }

    private float partialSum(int i, int sNode) {
        if(sNode > sMax) return A[i];
        int mid = S[sNode].min + (S[sNode].max - S[sNode].min) / 2;
        if(S[sNode].max == i) {
            return S[sNode].value;
        } else if(mid >= i) {
            return partialSum(i, 2 * sNode + 1);
        } else {
            return S[2 * sNode + 1].value + partialSum(i, 2 * sNode + 2);
        }
    }
}
