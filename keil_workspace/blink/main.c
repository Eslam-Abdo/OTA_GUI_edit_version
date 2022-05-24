/*********************************************************************************/
/* Author    : Islam Abdo                                                        */
/* Version   : V01                                                               */
/* Date      : 25 SEP 2020                                                       */
/*********************************************************************************/

/******************** 			 BLINK 		   ***********************************/
#include "STD_TYPES.h"
#include "BIT_MATH.h"


#include "RCC_interface.h"
#include "GPIO_interface.h"
#include "STK_interface.h"


int main(void)
{
	/* Initialize Clock System  */
	RCC_voidInitSysClock();
	/* Enable GPIOC Clock */
	RCC_voidEnableClock(RCC_APB2,APB2_GPIOC_EN);
	/* led on stm board */
	GPIO_voidSetPinDirection(GPIOC, PIN13, OUTPUT_SPEED_10MHZ_PP);
	/* Enable systik timer*/
	STK_voidInit();

	while(1)
	{
		GPIO_voidTogglePinValue(GPIOC, PIN13);
		STK_voidDelay_ms(200);
		// GPIO_voidSetPinValue(GPIOC, PIN13,LOW);
	}
	return 0;
}
