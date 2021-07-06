#include "m_pd.h"  
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/* mraa header */
#include "mraa/gpio.h"

/* gpio declaration */
#define GPIO_PIN_1 22

static t_class *blinky_class;  
 
typedef struct _blinky {  
  	t_object x_obj;
	volatile sig_atomic_t flag;
	t_int state;
 	mraa_result_t status;
    	mraa_gpio_context gpio_1;
} t_blinky;  



/* gestisce l'uscita */

void sig_handler(t_blinky *x, t_int signum)
{
    if (signum == SIGINT) {
        fprintf(stdout, "Exiting...\n");
        x->flag = 0;
    }
}

void blinky_free(t_blinky *x)
{

    /* release gpio's */
    x->status = mraa_gpio_close(x->gpio_1);

    //! [Interesting]
    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();
}

void blinky_bang(t_blinky *x)  
{
  //(void)x; // silence unused variable warning
  x->state = 1 - x->state;
  x->status = mraa_gpio_write(x->gpio_1, x->state);
  if (x->state == 1) 
    post("ACCESA");
  else
    post("SPENTA");
}  
 
void *blinky_new(void)  
{  
  t_blinky *x = (t_blinky *)pd_new(blinky_class);  
  x->flag = 1;
  x->state = 0;

    x->status = MRAA_SUCCESS;

    	/* install signal handler */
    	//signal(SIGINT, sig_handler);

    /* initialize mraa for the platform (not needed most of the times) */
    mraa_init();

    //! [Interesting]
    /* initialize GPIO pin */
    x->gpio_1 = mraa_gpio_init(GPIO_PIN_1);

    /* set GPIO to output */
    x->status = mraa_gpio_dir(x->gpio_1, MRAA_GPIO_OUT);
    
   /* 
    while (flag) {
        state = 1 - state;


        usleep(50000);
    }*/



  return (void *)x;  
}  
 
void blinky_setup(void) {  
  //blinky_class = class_new(gensym("blinky"), (t_newmethod)blinky_new, (t_method)blinky_free, sizeof(t_blinky), CLASS_DEFAULT, 0);  
  blinky_class = class_new(gensym("blinky"), (t_newmethod)blinky_new, (t_method)blinky_free, sizeof(t_blinky), 0, A_GIMME, 0); 
  //ltc_class = class_new(gensym("neum.ltc~"), (t_newmethod)ltc_new, (t_method)ltc_free, sizeof(t_ltc), 0, A_GIMME, 0);
  class_addbang(blinky_class, blinky_bang);  
}
