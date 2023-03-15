package com.okex.open.api.config;

import com.okex.open.api.constant.APIConstants;
import com.okex.open.api.enums.I18nEnum;

public class APIConfiguration {

    /**
     * The user's api key provided by OKEx.
     */
    private String apiKey;
    /**
     * The user's secret key provided by OKEx. The secret key used to sign your request data.
     */
    private String secretKey;
    /**
     * The Passphrase will be provided by you to further secure your API access.
     */
    private String passphrase;



    /**
     * Rest api endpoint url.
     */
    private String domain;
    private String xSimulatedTrading;



    /**
     * Host connection timeout.
     */
    private long connectTimeout;
    /**
     * The host reads the information timeout.
     */
    private long readTimeout;
    /**
     * The host writes the information timeout.
     */
    private long writeTimeout;
    /**
     * Failure reconnection, default true.
     */
    private boolean retryOnConnectionFailure;

    /**
     * The print api information.
     */
    private boolean print;

    /**
     * internationalization  {@link I18nEnum}
     */
    private I18nEnum i18n;

    public APIConfiguration() {
        this(null);
    }

    public APIConfiguration(String endpoint) {
        super();
        this.apiKey = null;
        this.secretKey = null;
        this.passphrase = null;
        this.domain = domain;
        this.xSimulatedTrading = null;
        this.connectTimeout = APIConstants.TIMEOUT;
        this.readTimeout = APIConstants.TIMEOUT;
        this.writeTimeout = APIConstants.TIMEOUT;
        this.retryOnConnectionFailure = true;
        this.print = false;
        this.i18n = I18nEnum.ENGLISH;
    }

    public String getApiKey() {
        return apiKey;
    }

    public void setApiKey(String apiKey) {
        this.apiKey = apiKey;
    }

    public String getSecretKey() {
        return secretKey;
    }

    public void setSecretKey(String secretKey) {
        this.secretKey = secretKey;
    }

    public String getPassphrase() {
        return passphrase;
    }

    public void setPassphrase(String passphrase) {
        this.passphrase = passphrase;
    }

    public String getDomain() {
        return domain;
    }

    public void setDomain(String domain) {
        this.domain = domain;
    }

    public String getxSimulatedTrading() {
        return xSimulatedTrading;
    }

    public void setxSimulatedTrading(String xSimulatedTrading) {
        this.xSimulatedTrading = xSimulatedTrading;
    }
    public long getConnectTimeout() {
        return connectTimeout;
    }

    public void setConnectTimeout(long connectTimeout) {
        this.connectTimeout = connectTimeout;
    }

    public long getReadTimeout() {
        return readTimeout;
    }

    public void setReadTimeout(long readTimeout) {
        this.readTimeout = readTimeout;
    }

    public long getWriteTimeout() {
        return writeTimeout;
    }

    public void setWriteTimeout(long writeTimeout) {
        this.writeTimeout = writeTimeout;
    }

    public boolean isRetryOnConnectionFailure() {
        return retryOnConnectionFailure;
    }

    public void setRetryOnConnectionFailure(boolean retryOnConnectionFailure) {
        this.retryOnConnectionFailure = retryOnConnectionFailure;
    }

    public boolean isPrint() {
        return print;
    }

    public void setPrint(boolean print) {
        this.print = print;
    }

    public I18nEnum getI18n() {
        return i18n;
    }

    public void setI18n(I18nEnum i18n) {
        this.i18n = i18n;
    }
}
