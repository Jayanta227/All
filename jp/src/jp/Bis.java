import java.lang.Math;
import java.util.*;

public class Bis{
    float llim[]=new float[20];
    float ulim[]=new float[20];
    float fun[]=new float[20];
    int order=2;
    float mpoint[]=new float[20];
    float fx[];
    
    void input_taking(){
        fx = new float[3];
        fx[0]=3;
        fx[1]=-2;
        fx[2]=-10;
    }
    float fun_cal(float x){
        int order=this.order;
        float y=(float)0;
        for(float f : fx){
            y=y+f*(float)(Math.pow(x,order));
            order=order-1;
        }
        return(y);
 
    }
    
    void root_cal(){
        float ll= 1;
        float ul= 3;
        float mp;
        mp=(ll+ul)/2;
        float fn=fun_cal(mp);
        float new_mp=0;
        
        if(fn==0){
            System.out.println(fn);
        }
        else if(fun_cal(ll)*fun_cal(ul)<0){
            for(int i=0;i<20;i++){
                mp=(ul+ll)/2;
                if(fun_cal(mp)*fun_cal(ll)<0){
                    ul=mp;
                    new_mp=(ul+ll)/2;
                    fn=fun_cal(new_mp);
                }
                //else if(fun_cal(new_mp)==0){
                //    exit();
                //}
                else if(fun_cal(mp)*fun_cal(ul)<0){
                    ll=mp;
                    new_mp=(ul+ll)/2;
                    fn=fun_cal(new_mp);
                }
                llim[i]=ll;
                ulim[i]=ul;
                mpoint[i]=new_mp;
                fun[i]=fn;
            }
        }
    }
    public static void main(String args[]){
        Bis bis = new Bis();
        bis.input_taking();
        //System.out.println(bis.fun_cal((float)2.189254788));
        bis.root_cal();
        System.out.println("llim\t\tulim\t\tmpoint\t\tfun");
        for (int i=0;i<20;i++){
            System.out.printf("%.5f\t\t%.5f\t\t%.5f\t\t%.5f\n",bis.llim[i],bis.ulim[i],bis.mpoint[i],bis.fun[i]);
        }
    }
    
}