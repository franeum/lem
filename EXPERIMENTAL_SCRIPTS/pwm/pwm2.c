#include "m_pd.h"  
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

/* mraa header */
#include "mraa/pwm.h"

/* PWM declaration */
#define PWM 13

/* PWM period in us */
#define PWM_FREQ 200

static t_class *pwm2_class;  
 
typedef struct _pwm2 {  
  	t_object x_obj;
	volatile sig_atomic_t flag;
	int state;
 	mraa_result_t status;
	mraa_pwm_context pwm2;
} t_pwm2;  



/* gestisce l'uscita */

void sig_handler(t_pwm2 *x, int signum)
{
    if (signum == SIGINT) {
        fprintf(stdout, "Exiting...\n");
        x->flag = 0;
    }
}

void pwm2_free(t_pwm2 *x)
{

    /* release gpio's */
    x->status = mraa_pwm_close(x->pwm2);

    //! [Interesting]
    /* deinitialize mraa for the platform (not needed most of the times) */
    mraa_deinit();
}

void pwm2_float(t_pwm2 *x, t_floatarg f)  
{
  //(void)x; // silence unused variable warning
  //x->state = 1 - x->state;
  post("%f", f);
  x->status = mraa_pwm_write(x->pwm2, f);
}

void pwm2_bang(t_pwm2 *x)
{
  post("bang");
  x->status = mraa_pwm_write(x->pwm2, 0.95);
}

void *pwm2_new(void)  
{  
  t_pwm2 *x = (t_pwm2 *)pd_new(pwm2_class);  
  x->flag = 1;
  x->state = 0;

    x->status = MRAA_SUCCESS;

    	/* install signal handler */
    	//signal(SIGINT, sig_handler);

    /* initialize mraa for the platform (not needed most of the times) */
    mraa_init();
    x->pwm2 = mraa_pwm_init(PWM);
    //! [Interesting]
    /* initialize GPIO pin */
    //x->gpio_1 = mraa_gpio_init(GPIO_PIN_1);
    x->status = mraa_pwm_period_us(x->pwm2, PWM_FREQ);
    
    x->status = mraa_pwm_enable(x->pwm2, 1);
    
    
    /* set GPIO to output */
    //x->status = mraa_gpio_dir(x->gpio_1, MRAA_GPIO_OUT);
    

  return (void *)x;  
}  
 
void pwm2_setup(void) {  
  pwm2_class = class_new(gensym("pwm2"),  
    (t_newmethod)pwm2_new, NULL,
    sizeof(t_pwm2), CLASS_DEFAULT, 0);  
  class_addfloat(pwm2_class, pwm2_float);  
  class_addbang(pwm2_class, pwm2_bang);
}
