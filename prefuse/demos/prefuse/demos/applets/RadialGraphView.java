package prefuse.demos.applets;

import prefuse.util.ui.JPrefuseApplet;


public class RadialGraphView extends JPrefuseApplet {

    public void init() {
    	String gr = this.getParameter("graph");
    	String[][] tempgraph = new String[10][500];
    	int[][] graph = new int[10][500];
    	int l=0,m=0;
    	for(int i=0;i<gr.length();i++){
    		if(gr.charAt(i)!= ' ' && gr.charAt(i) != '|'){
    			tempgraph[l][m] = tempgraph[l][m].concat(Character.toString(gr.charAt(i)));
    			}
    		else if(gr.charAt(i)==' '){
    			m=m+1;
    			}
    		else if(gr.charAt(i)=='|'){
    			m=0;
    			l+=1;
    			}
    		}
    	for(int i=0;i<l;i++){
    		for(int f=0;f<tempgraph[i].length;f++){
    			graph[i][f] = Integer.parseInt(tempgraph[i][f]);
    			}
    		}
        this.setContentPane(
            prefuse.demos.RadialGraphView.demo("/socialnet.xml", "name",graph));
    }
    
} // end of class RadialGraphView
