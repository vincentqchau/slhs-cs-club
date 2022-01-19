import java.util.HashMap;
import java.util.PriorityQueue;

public class HuffmanTree {

    private PriorityQueue<HuffmanNode> queue;
    private HuffmanNode root;
    
    public HuffmanTree(String input) {

        queue = new PriorityQueue<HuffmanNode>();
        HashMap<Character, Integer> freq = new HashMap<Character, Integer>();
        for(int i = 0; i < input.length(); i++) {
            char curr = input.charAt(i);
            if(!freq.containsKey(curr)) freq.put(curr, 0);
            freq.put(curr, freq.get(curr)+1);
        }
        for(Character key : freq.keySet()) {
            queue.add(new HuffmanNode(key, freq.get(key)));
        }

        createTree();

    }

    private void createTree() {

        root = null;
        while(queue.size() > 1) {
            HuffmanNode left = queue.poll(), right = queue.poll();
            HuffmanNode z = new HuffmanNode(left, right);
            root = z;
            queue.add(z);
        }

    }

    public void printCode(HuffmanNode root, String s) {
        if(root.getLeft() == null && root.getRight() == null && root.isLeaf()) {
            System.out.println(root.getCharacter() + " | " + s);
        }
        if(root.getLeft() != null)
            printCode(root.getLeft(), s+"0");
        if(root.getRight() != null)
            printCode(root.getRight(), s+"1");
    }

    public HuffmanNode getRoot() {
        return root;
    }

}
