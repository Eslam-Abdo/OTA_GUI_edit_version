#include "STD_TYPES.h"
#include "BIT_MATH.h"

#include "RCC_interface.h"
#include "GPIO_interface.h"
#include "STK_interface.h"
#include "USART_INTERFACE.h"

#include "FPEC_interface.h"


void Parser_voidParseRecord(uint8* Copy_u8BufData);
void clear_data(uint8* data_cleared);
void GetNewRecordLine(void);

volatile uint8  u8RecBuffer[60] = {0}  ;
volatile uint8  u8RecCounter    = 0;
volatile uint8  u8TimeOutFlag   = 0;
volatile uint8  u8BLWriteReq    = 1;

typedef void (*Function_t)(void);
Function_t addr_to_call = 0;



void func(void)
{
#define SCB_VTOR   *((volatile u32*)0xE000ED08) 

	SCB_VTOR = 0x08002400;

	addr_to_call = *(Function_t*)(0x08002404);
	addr_to_call();
}

int main()
{
	RCC_voidInitSysClock(); /* Enable HSI */
	RCC_voidEnableClock(RCC_APB2,APB2_GPIOA_EN);  /*ENABLE PORTA AS IO PINS*/
	RCC_voidEnableClock(RCC_APB2,APB2_USART1_EN); /*ENABLE USART1 */
	RCC_voidEnableClock(RCC_AHB ,AHB_FLITF_EN); /*ENABLE FPEC */
	
	
	RCC_voidEnableClock(RCC_APB2,APB2_GPIOB_EN);  /*ENABLE PORTB AS IO PINS*/
	RCC_voidEnableClock(RCC_APB1,APB1_USART3_EN); /*ENABLE USART3 */
	
	
	STK_voidInit();
	
   USART_voidInit(UART1,115200);
	
	//USART_voidInit(UART3,115200);	
	 STK_voidSetIntervalSingle((5*1000*1000),func); /* 35 sec */
	
	uint8 Local_u8RecStatus;
	
	//GetNewRecordLine();
	
	while(u8TimeOutFlag == 0)
	{
		GetNewRecordLine();
		
		if (u8RecBuffer[u8RecCounter] != 255)
		{
			 STK_voidStopInterval();
					
			if (u8BLWriteReq == 1)
			{
				FPEC_voidEraseAppArea();
				u8BLWriteReq = 0;
			}
			
			/* Parse */
			Parser_voidParseRecord(u8RecBuffer);
			USART_voidTransmit(UART1 ,"ok",STRING);
			//USART_voidTransmit(UART1 ,"\n",STRING);
		}
		else
		{
			/* No file to burn */
		}
			
		STK_voidSetIntervalSingle((5*1000*1000),func); /* 5 sec */
			
	}
	
}


void clear_data(uint8* data_cleared)
{
	u8 LOC_u8Iterator1 = 0 ;

	for( LOC_u8Iterator1 = 0 ; LOC_u8Iterator1 < 60 ; LOC_u8Iterator1++ ){

		data_cleared[ LOC_u8Iterator1 ] = 0 ;

	}
}

void GetNewRecordLine(void)
{
	clear_data(u8RecBuffer);
	u8RecCounter = 0;
	u8RecBuffer[u8RecCounter] = USART_charReceive(UART1);
	while(u8RecBuffer[u8RecCounter] != 255)
	{
		if (u8RecBuffer[u8RecCounter] == '\n')
		{
			break;
		}
		u8RecCounter ++;
		u8RecBuffer[u8RecCounter] = USART_charReceive(UART1);
	}
}

