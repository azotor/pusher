import math

class Collision:

    @staticmethod
    def rectangToRectangle( rectALeft, rectATop, rectAWidth, rectAHeight, rectBLeft, rectBTop, rectBWidth, rectBHeight ):
        
        rectARight = rectALeft + rectAWidth
        rectABottom = rectATop + rectAHeight

        rectBRight = rectBLeft + rectBWidth
        rectBBottom = rectBTop + rectBHeight

        if(
            rectBRight >= rectALeft and
            rectBLeft <= rectARight and
            rectBBottom >= rectATop and
            rectBTop <= rectABottom
        ): return True

        return False
    
    @staticmethod
    def circleToCircle( circleAX, circleAY, circleARadius, circleBX, circleBY, circleBRadius ):

        distance = math.sqrt( ( circleAX - circleBX ) ** 2 + ( circleAY - circleBY ) ** 2 )

        if distance < circleARadius + circleBRadius :
            return True

        return False


    @staticmethod
    def circleToRect( circleX, circleY, circleRadius, rectLeft, rectTop, rectWidth, rectHeight ) -> bool :

        rectCenterX = rectLeft + rectWidth / 2
        rectCenterY = rectTop + rectHeight / 2
        rectRadius = math.sqrt( rectWidth ** 2 + rectHeight ** 2 ) / 2

        circleLeft = circleX - circleRadius
        circleTop = circleY - circleRadius

        return Collision.rectangToRectangle( circleLeft, circleTop, circleRadius * 2, circleRadius * 2, rectLeft, rectTop, rectWidth, rectHeight ) and Collision.circleToCircle( circleX, circleY, circleRadius, rectCenterX, rectCenterY, rectRadius )