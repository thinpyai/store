package com.tp.spendsmart.common.exception;

import shinetsu.intra.base.message.IntraAppMessage;


public class DataConvertException extends InvalidOperationException {

    private static final long serialVersionUID = 1L;
    

    public DataConvertException(final IntraAppMessage msgId, Object... args) {
        super(msgId, args);
    }


    public DataConvertException(final IntraAppMessage msgId, Throwable cause, Object... args) {
        super(msgId, cause, args);
    }

    public DataConvertException(Throwable cause) {
        super(cause);
    }
}
