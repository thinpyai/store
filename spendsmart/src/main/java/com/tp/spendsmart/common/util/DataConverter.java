package com.tp.spendsmart.common.util;

import org.springframework.beans.BeanUtils;

import java.lang.reflect.InvocationTargetException;
import java.util.List;
import java.util.stream.Collectors;

public class DataConverter<E, T> {

    public static <S, D> D convert(S src, Class<D> type) {

        if (src == null) {
            return null;
        }
        try {
            D dst = type.getDeclaredConstructor().newInstance();
            BeanUtils.copyProperties(src, dst);
            return dst;
        } catch (IllegalAccessException | InvocationTargetException ex) {
//            throw new DataConvertException(messageId("error.dataconvert"), ex, src);
            return null;

        } catch (ReflectiveOperationException ex) {
//            throw new IllegalArgumentException(messageId("error.dataconvert"), ex);
            return null;
        }
    }

    public static <S, D> List<D> convertList(List<S> src, Class<D> type) {
        if (src == null) {
            return null;
        }
        List<D> out = src.stream().map(t -> convert(t, type)).collect(Collectors.toList());

        return out;
    }
}
