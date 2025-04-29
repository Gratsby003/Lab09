from database.DB_connect import DBConnect


class DAO():
    def __init__(self):
        pass

    @classmethod
    def query_airport(self,valore):
        cnx = DBConnect.get_connection()
        cursor=cnx.cursor()
        query='SELECT LEAST(flights.ORIGIN_AIRPORT_ID, flights.DESTINATION_AIRPORT_ID) AS airport1,GREATEST(flights.ORIGIN_AIRPORT_ID, flights.DESTINATION_AIRPORT_ID) AS airport2, AVG(flights.DISTANCE) AS avg_distance FROM extflightdelays.flights AS flights GROUP BY airport1, airport2 HAVING AVG(flights.DISTANCE) > %s;'
        cursor.execute(query,[int(valore)])
        lista=cursor.fetchall()
        return lista
