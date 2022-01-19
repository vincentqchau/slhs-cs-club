public class HuffmanNode implements Comparable<HuffmanNode> {

    private boolean isLeaf;
    private int sum;
    private char character;
    private HuffmanNode left, right;

    public HuffmanNode(char letter, int sum) {

        this.character = letter;
        this.sum = sum;
        isLeaf = true;

    }

    public HuffmanNode(HuffmanNode left, HuffmanNode right) {
        this.left = left;
        this.right = right;
        if(left!=null) sum+=left.getFreq();
        if(right!=null) sum+=right.getFreq();
    }

    public HuffmanNode getLeft() {
        return left;
    }

    public HuffmanNode getRight() {
        return right;
    }

    public void setLeft(HuffmanNode x) {
        left = x;
    }

    public void setRight(HuffmanNode x) {
        right = x;
    }

    public int getFreq() {
        return sum;
    }

    public char getCharacter() {
        return character;
    }

    public boolean isLeaf() {
        return isLeaf;
    }

    public int compareTo(HuffmanNode o) {
        return sum-o.sum;
    }

}