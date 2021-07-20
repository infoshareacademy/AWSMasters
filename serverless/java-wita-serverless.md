```
package app;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyRequestEvent;
import com.amazonaws.services.lambda.runtime.events.APIGatewayProxyResponseEvent;

import java.util.HashMap;
import java.util.Map;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class Counter implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {

        Map<String, String> headers = new HashMap<>();
        headers.put("Content-Type", "application/json");
        headers.put("X-Custom-Header", "application/json");

        String birthDate = input.getQueryStringParameters().get("day")
                + " " + input.getQueryStringParameters().get("month")
                + " " + input.getQueryStringParameters().get("year");

        SimpleDateFormat myFormat = new SimpleDateFormat("dd MM yyyy");
        Date date = new Date();
        try {
            date = myFormat.parse(birthDate);
        } catch (ParseException e) {
        }

        Date now = new Date();
        long diff = TimeUnit.DAYS.convert(now.getTime() - date.getTime(), TimeUnit.MILLISECONDS);

        APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent()
                .withHeaders(headers);

        String output = String.format("{ \"Number of days from your birth\": \"%s\" }", diff);

        return response.withStatusCode(200).withBody(output);

    }
}
```