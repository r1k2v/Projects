



#include <stdio.h>
#include <string.h>
#include <omnetpp.h>

#include "m25_m.h"
class Practise4: public cSimpleModule
{
protected:
   virtual A *generateMessage();
   virtual void initialize();
   virtual void handleMessage(cMessage *msg);
public:
   int i=0;

};
Define_Module(Practise4);
void Practise4::initialize()
{
    if (strcmp("source",getName())==0)
    {
       // cMessage *msg = new cMessage("Rahul");
        A *msg = generateMessage();
        scheduleAt(simTime()+5.0, msg);
    }
}

void Practise4::handleMessage(cMessage *msg)
{

    A *ttmsg = check_and_cast<A *>(msg);
    if ((ttmsg->getDestination())%23==0){
    if (strcmp("m24",getName())==0){
    send(msg,"out8");
    }
    else{
        send(msg,"out7");
    }
    }
    if ((ttmsg->getDestination())%23==1){
       if (strcmp("m28",getName())==0){
       send(msg,"out8");
       }
       else{
           send(msg,"out7");
       }
       }
    if ((ttmsg->getDestination())%23==2){
           if (strcmp("m33",getName())==0){
           send(msg,"out8");
           }
           else{
               send(msg,"out7");
           }
           }
    if ((ttmsg->getDestination())%23==3){
           if (strcmp("m39",getName())==0){
           send(msg,"out8");
           }
           else{
               send(msg,"out7");
           }
           }
    if ((ttmsg->getDestination())%23==4){
           if (strcmp("m23",getName())==0){
           send(msg,"out8");
           }
           else{
               send(msg,"out7");
           }
           }
    if ((ttmsg->getDestination())%23==5){
               if (strcmp("m27",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==6){
               if (strcmp("m32",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==7){
               if (strcmp("m38",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==8){
               if (strcmp("m44",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==9){
               if (strcmp("m22",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==10){
               if (strcmp("m26",getName())==0){
               send(msg,"out8");
               }
               else{
                   send(msg,"out7");
               }
               }
    if ((ttmsg->getDestination())%23==11){
                   if (strcmp("m31",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==12){
                   if (strcmp("m37",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==13){
                   if (strcmp("m43",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==14){
                   if (strcmp("m25",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==15){
                   if (strcmp("m30",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==16){
                   if (strcmp("m36",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==17){
                   if (strcmp("m42",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==18){
                   if (strcmp("m29",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==19){
                   if (strcmp("m35",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==20){
                   if (strcmp("m41",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==21){
                   if (strcmp("m34",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
    if ((ttmsg->getDestination())%23==22){
                   if (strcmp("m40  ",getName())==0){
                   send(msg,"out8");
                   }
                   else{
                       send(msg,"out7");
                   }
                   }
   Practise4::initialize();
}

A *Practise4::generateMessage()
{

    int dest = intuniform(22,44);
    dest++;

    char msgname[20];
    sprintf(msgname, "m_no->%d", i);

    // Create message object and set source and destination field.
    A *msg = new A(msgname);
   // msg->setSource(src);
    msg->setDestination(dest);
    i++;
    return msg;
}
class Practise3: public cSimpleModule
{
protected:
   virtual void handleMessage(cMessage *msg);

};
Define_Module(Practise3);

void Practise3::handleMessage(cMessage *msg)
{

    A *ttmsg = check_and_cast<A *>(msg);
    if ((ttmsg->getDestination())%12==0){
    if (strcmp("m12",getName())==0){
    send(msg,"out6");
    }
    else{
        send(msg,"out5");
    }
    }
    if ((ttmsg->getDestination())%12==1){
       if (strcmp("m15",getName())==0){
       send(msg,"out6");
       }
       else{
           send(msg,"out5");
       }
       }
    if ((ttmsg->getDestination())%12==2){
           if (strcmp("m19",getName())==0){
           send(msg,"out6");
           }
           else{
               send(msg,"out5");
           }
           }
    if ((ttmsg->getDestination())%12==3){
           if (strcmp("m11",getName())==0){
           send(msg,"out6");
           }
           else{
               send(msg,"out5");
           }
           }
    if ((ttmsg->getDestination())%12==4){
           if (strcmp("m14",getName())==0){
           send(msg,"out6");
           }
           else{
               send(msg,"out5");
           }
           }
    if ((ttmsg->getDestination())%12==5){
               if (strcmp("m18",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==6){
               if (strcmp("m10",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==7){
               if (strcmp("m13",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==8){
               if (strcmp("m16",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==9){
               if (strcmp("m17",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==10){
               if (strcmp("m20",getName())==0){
               send(msg,"out6");
               }
               else{
                   send(msg,"out5");
               }
               }
    if ((ttmsg->getDestination())%12==11){
                  if (strcmp("m21",getName())==0){
                  send(msg,"out6");
                  }
                  else{
                      send(msg,"out5");
                  }
                  }

}


class Practise2 : public cSimpleModule
{

  protected:
    virtual void handleMessage(cMessage *msg);

};

Define_Module(Practise2);


void Practise2::handleMessage(cMessage *msg)
{
    A *ttmsg = check_and_cast<A *>(msg);
    if ((ttmsg->getDestination())%6==0){
    if (strcmp("m6",getName())==0){
    send(msg,"out4");
    }
    else{
        send(msg,"out3");
    }
    }
    if ((ttmsg->getDestination())%6==1){
       if (strcmp("m7",getName())==0){
       send(msg,"out4");
       }
       else{
           send(msg,"out3");
       }
       }
    if ((ttmsg->getDestination())%6==2){
           if (strcmp("m4",getName())==0){
           send(msg,"out4");
           }
           else{
               send(msg,"out3");
           }
           }
    if ((ttmsg->getDestination())%6==3){
           if (strcmp("m8",getName())==0){
           send(msg,"out4");
           }
           else{
               send(msg,"out3");
           }
           }
    if ((ttmsg->getDestination())%6==4){
           if (strcmp("m5",getName())==0){
           send(msg,"out4");
           }
           else{
               send(msg,"out3");
           }
           }
    if ((ttmsg->getDestination())%6==5){
              if (strcmp("m6",getName())==0){
              send(msg,"out4");
              }
              else{
                  send(msg,"out3");
              }
              }
}

class Practise1: public cSimpleModule
{
protected:
    virtual void handleMessage(cMessage *msg);
};
Define_Module(Practise1);

void Practise1::handleMessage(cMessage *msg)
{
    A *ttmsg = check_and_cast<A *>(msg);
    if ((ttmsg->getDestination())%3==0){
    if(strcmp("sink",getName())==0)
        delete msg;
    else{
        if(strcmp("m2",getName())==0){
         send(msg,"out2");
        }
        else{
        send(msg,"out1");
        }
    }
    }
    if ((ttmsg->getDestination())%3==1){
       if(strcmp("sink",getName())==0)
           delete msg;
       else{
           if(strcmp("m3",getName())==0){
            send(msg,"out2");
           }
           else{
           send(msg,"out1");
           }
       }
       }
    if ((ttmsg->getDestination())%3==2){
       if(strcmp("sink",getName())==0)
           delete msg;
       else{
           if(strcmp("m1",getName())==0){
            send(msg,"out2");
           }
           else{
           send(msg,"out1");
           }
       }
       }
}








