simple Practise4
{
    parameters:
        @display("i=block/routing");
        @display("i=,cornflowerblue");
     gates:
         input in[];
         output out7;
         output out8;   
}
simple Practise3
{
    parameters:
        @display("i=block/routing");
        @display("i=,green");
    gates:
        input in[];
        output out5;
        output out6;
}

simple Practise2
{
    parameters:
        @display("i=block/routing");
        @display("i=,gold");
    gates:
        input in[];
        output out3;
        output out4;
}
simple Practise1
{
    parameters:
        @display("i=block/routing");
        @display("i=,cyan");
    gates:
        input in[];
        output out1;
        output out2;
}
network n25
{
    parameters:
        @display("bgb=1000,1000");
    types:
        channel c extends ned.DelayChannel
        {
           delay = 100ms;
        }
        channel c1 extends ned.IdealChannel
        {
            @display("ls=,0");//hide connection
        }
    submodules:
        sink: Practise1 {
            parameters:
                @display("i=block/sink;p=500,500");
        }
        m1: Practise1 {
            parameters:
                @display("p=600,500");
        }
        m2: Practise1 {
            parameters:
                @display("p=450,586.6");
        }
        m3: Practise1 {
            parameters:
                @display("p=450,413.4");
        }
        m4: Practise2 {
            parameters:
                @display("p=700,500");
        }
        m5: Practise2 {
            parameters:
                @display("p=600,673.20");
        }
        m6: Practise2 {
            parameters:
                @display("p=400,673.2");
        }
        m7: Practise2 {
            parameters:
                @display("p=300,500");
        }
        m8: Practise2 {
            parameters:
                @display("p=400,326.7949");
        }
        m9: Practise2 {
            parameters:
                @display("p=600,326.79");
        }
         m10: Practise3 {
            parameters:
                @display("p=800,500");
        }
        m11:Practise3{
            parameters:
                @display("p=759.8,650");
        }
         m12: Practise3 {
            parameters:
                @display("p=650,759.8");
        }
         m13: Practise3 {
            parameters:
                @display("p=500,800");
        }
         m14: Practise3 {
            parameters:
                @display("p=350,759.8");
        }
         m15: Practise3 {
            parameters:
                @display("p=240.2,650");
        }
         m16: Practise3 {
            parameters:
                @display("p=200,500");
        }
         m17: Practise3 {
            parameters:
                @display("p=240.2,350");
        }
         m18: Practise3 {
            parameters:
                @display("p=350,240.2");
        }
         m19: Practise3 {
            parameters:
                @display("p=500,200");
        }
         m20: Practise3 {
            parameters:
                @display("p=650,240.2");
        }
         m21: Practise3 {
            parameters:
                @display("p=759.8,350");
        }
         m22: Practise4 {
            parameters:
                @display("p=900,500");
        }
        m23: Practise4 {
            parameters:
                @display("p=886.37,603.52");
        }
        m24: Practise4 {
            parameters:
                @display("p=846.41,700");
        } 
        m25: Practise4 {
            parameters:
                @display("p=782.84,782.84");
        }
        m26: Practise4 {
            parameters:
                @display("p=700,846.41");
        }
        m27: Practise4 {
            parameters:
                @display("p=603.52,886.37");
        }
        m28: Practise4 {
            parameters:
                @display("p=500,900");
        }
        m29: Practise4 {
            parameters:
                @display("p=396.47,886.37");
        }
        m30: Practise4 {
            parameters:
                @display("p=300,846.41");
        }
        m31: Practise4 {
            parameters:
                @display("p=217.15,782.84");
        }
        m32: Practise4 {
            parameters:
                @display("p=153.59,700");
        }
        m33: Practise4 {
            parameters:
                @display("p=113.62,603.52");
        }
        m34: Practise4 {
            parameters:
                @display("p=100,500");
        }
        m35: Practise4 {
            parameters:
                @display("p=113.62,396.47");
        }
        m36: Practise4 {
            parameters:
                @display("p=153.58,300");
        }
        m37: Practise4 {
            parameters:
                @display("p=217.15,217.15");
        }
        m38: Practise4 {
            parameters:
                @display("p=300,153.58");
        }
        m39: Practise4 {
            parameters:
                @display("p=396.47,113.62");
        }
        m40: Practise4 {
            parameters:
                @display("p=500,100");
        }
        m41: Practise4 {
            parameters:
                @display("p=603.52,113.62");
        }
        m42: Practise4 {
            parameters:
                @display("p=700,153.58");
        }
        m43: Practise4 {
            parameters:
                @display("p=782.84,217.15");
        }
        m44: Practise4 {
            parameters:
                @display("p=846.41,300");
        }
        source: Practise4 {
            parameters: 
                @display("i=block/source;p=886.37,396.47");
        }
    connections:
        m1.out1--> c --> m2.in++;
        m2.out1 --> c --> m3.in++;
        m3.out1 --> c --> m1.in++;
        m4.out3 --> c --> m5.in++;
        m5.out3 --> c --> m6.in++;
        m6.out3 --> c --> m7.in++;
        m7.out3 --> c --> m8.in++;
        m8.out3 --> c --> m9.in++;
        m9.out3 --> c --> m4.in++;
         m10.out5 -->c--> m11.in++;
        m11.out5 -->c--> m12.in++;
        m12.out5 -->c--> m13.in++;
        m13.out5 -->c--> m14.in++;
        m14.out5 -->c--> m15.in++;
        m15.out5 -->c--> m16.in++;
        m16.out5 -->c--> m17.in++;
        m17.out5 -->c--> m18.in++;
        m18.out5 -->c--> m19.in++;
        m19.out5 -->c--> m20.in++;
        m20.out5 -->c--> m21.in++;
        m21.out5 -->c--> m10.in++;
        m22.out7 -->c--> m23.in++;
        m23.out7 -->c--> m24.in++;
        m24.out7 -->c--> m25.in++;
        m25.out7 -->c--> m26.in++;
        m26.out7 -->c--> m27.in++;
        m27.out7 -->c--> m28.in++; 
        m28.out7 -->c--> m29.in++;
        m29.out7 -->c--> m30.in++;
        m30.out7 -->c--> m31.in++;
        m31.out7 -->c--> m32.in++;
        m32.out7 -->c--> m33.in++;
        m33.out7 -->c--> m34.in++;
        m34.out7 -->c--> m35.in++;
        m35.out7 -->c--> m36.in++;
        m36.out7 -->c--> m37.in++;
        m37.out7 -->c--> m38.in++;
        m38.out7 -->c--> m39.in++;
        m39.out7 -->c--> m40.in++;
        m40.out7 -->c--> m41.in++;
        m41.out7 -->c--> m42.in++;
        m42.out7 -->c--> m43.in++; 
        m43.out7 -->c--> m44.in++;
        m44.out7 -->c--> source.in++;
        source.out7 -->c--> m22.in++;
        
        

        m1.out2 --> c1 --> sink.in++;
        m2.out2 --> c1 --> sink.in++;
        m3.out2 --> c1 --> sink.in++;
        sink.out2-->c1-->m1.in++;
        sink.out1-->c1-->m2.in++;
       // sink.out2-->c1-->m3.in++;
        m4.out4 --> c1 --> m1.in++;
        m5.out4 --> c1 --> m1.in++;
        m6.out4 --> c1 --> m2.in++;
        m7.out4 --> c1 --> m2.in++;
        m8.out4 --> c1 --> m3.in++;
        m9.out4 --> c1 --> m3.in++;
        m10.out6--> c1 --> m4.in++;
        m11.out6--> c1 --> m4.in++;
        m12.out6--> c1 --> m5.in++;
        m13.out6--> c1 --> m5.in++;
        m14.out6--> c1 --> m6.in++;
        m15.out6--> c1 --> m6.in++;
        m16.out6--> c1 --> m7.in++;
        m17.out6--> c1 --> m7.in++;
        m18.out6--> c1 --> m8.in++;
        m19.out6--> c1 --> m8.in++;
        m20.out6--> c1 --> m9.in++;
        m21.out6--> c1 --> m9.in++;
        m22.out8--> c1 -->m10.in++;
        m23.out8--> c1 -->m10.in++;
        m24.out8--> c1 -->m11.in++;
        m25.out8--> c1 -->m11.in++;
        m26.out8--> c1 -->m12.in++;
        m27.out8--> c1 -->m12.in++;
        m28.out8--> c1 -->m13.in++;
        m29.out8--> c1 -->m13.in++;
        m30.out8--> c1 -->m14.in++;
        m31.out8--> c1 -->m14.in++;
        m32.out8--> c1 -->m15.in++;
        m33.out8--> c1 -->m15.in++;
        m34.out8--> c1 -->m16.in++;
        m35.out8--> c1 -->m16.in++;
        m36.out8--> c1 -->m17.in++;
        m37.out8--> c1 -->m17.in++;
        m38.out8--> c1 -->m18.in++;
        m39.out8--> c1 -->m18.in++;
        m40.out8--> c1 -->m19.in++;
        m41.out8--> c1 -->m19.in++;
        m42.out8--> c1 -->m20.in++;
        m43.out8--> c1 -->m20.in++;
        m44.out8--> c1 -->m21.in++;
        source.out8-->c1-->m21.in++;
}

