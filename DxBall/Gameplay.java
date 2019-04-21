package DxBall;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.Timer;
import javax.swing.JPanel;

public class Gameplay extends JPanel implements KeyListener,ActionListener{
	private int score=0;
	private int xpos=350;
	private int ypos=600;
	private int bxpos=300;
	private int bypos=585;
	private int bxdir=-2;
	private int bydir=-1;
	private int totalbricks=15;
	private Timer time;
	private int delay=3;
	private boolean play1=false;
	private Bricks b2;
	 Gameplay()
	 {
		 b2= new Bricks();
		 addKeyListener(this);
		 setFocusable(true);
		 time = new Timer(delay,this);
		 time.start();
		 setFocusTraversalKeysEnabled(false);
	 } 
	 public void paint(Graphics g)
	 {
		 
		 g.setColor(Color.black);
		 g.fillRect(5, 5, 690, 690);
		 b2.draw1((Graphics2D) g);
		 g.setColor(Color.white);
		 g.fillRect(0, 0, 5, 695);
		 g.fillRect(690, 0, 5, 695);
		 g.fillRect(0, 0, 700, 5);
		 
		 g.setColor(Color.GREEN);
		 g.fillOval(bxpos,bypos, 15, 15);
		 
		 g.setColor(Color.red);
		 g.fillRect(xpos-50, ypos, 100,10 );
		 
		 g.drawString("Score: "+score, 600, 30);
		 
		 if(bypos>=600)
			{
				play1=false;
				g.drawString("The End", 350, 350);
				g.drawString("Score: " +score, 350, 380);
				//break a;
			}
		 g.dispose();
	 }
	 public void keyPressed(KeyEvent e) {
			if(e.getKeyCode()==KeyEvent.VK_LEFT || e.getKeyCode()==KeyEvent.VK_SPACE)
			{
				play1=true;
				moveleft();
			}
			if(e.getKeyCode()==KeyEvent.VK_RIGHT || e.getKeyCode()==KeyEvent.VK_0)
			{
				play1=true;
				moveright();
			}
		}
	 public void actionPerformed(ActionEvent e) {
		time.start();
		a:if(play1)
		{
			if(new Rectangle(bxpos,bypos,15,15).intersects(new Rectangle(xpos-50,ypos,100,10)) )
				{
					 //bxdir=-bxdir;
					bydir=-bydir;
				}
			bxpos+=bxdir;
			bypos+=bydir;
			if(bxpos<=5)
				bxdir= -bxdir;
			if(bypos<=0)
				bydir=-bydir;
			if(bxpos>=680)
				bxdir=-bxdir;
			if(bypos>=600)
			{
				play1=false;
				
				break a;
			}
			for(int i = 0; i<b2.row;i++)
				for(int j=0 ; j<b2.col;j++)
					if(new Rectangle(bxpos,bypos,15,15).intersects(new Rectangle(j*b2.bsize+95, i*b2.hsize +60 , b2.bsize, b2.hsize)) )
					{
						b2.bricks[i][j]=0;
						score+=5;
					}
		}
		
		repaint();
		
	} 
	
	public void keyReleased(KeyEvent e) {}
	public void keyTyped(KeyEvent e) {}
	public void moveleft()
	{
		
		if(xpos<=95)
			xpos=95;
		else
			xpos-=40;
	}
	public void moveright()
	{
		
		if(xpos>=600)
			xpos=600;
		else
			xpos+=40;
	}
}
